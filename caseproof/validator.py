"""Public-safe CaseProof validator.

The validator is intentionally deterministic and bounded. It evaluates synthetic
UiPath Maestro case packets and returns HOLD, BLOCK, or ALLOW_HUMAN_REVIEW_ONLY.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


ALLOW = "ALLOW_HUMAN_REVIEW_ONLY"
HOLD = "HOLD"
BLOCK = "BLOCK"

REQUIRED_MILESTONES = [
    "intake",
    "evidence_collection",
    "policy_check",
    "risk_review",
    "decision_recommendation",
]

REQUIRED_TOP_LEVEL = ["packet_version", "case", "maestro", "evidence", "policy", "decision", "controls"]


@dataclass
class Finding:
    severity: str
    code: str
    message: str


@dataclass
class Evaluation:
    findings: list[Finding] = field(default_factory=list)

    def add(self, severity: str, code: str, message: str) -> None:
        self.findings.append(Finding(severity, code, message))

    @property
    def decision(self) -> str:
        if any(f.severity == "block" for f in self.findings):
            return BLOCK
        if any(f.severity == "hold" for f in self.findings):
            return HOLD
        return ALLOW


def _as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _missing_milestones(milestones: list[str]) -> list[str]:
    observed = set(milestones)
    return [required for required in REQUIRED_MILESTONES if required not in observed]


def _evidence_index(evidence: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for item in evidence:
        evidence_id = str(item.get("id", "")).strip()
        if evidence_id:
            index[evidence_id] = item
    return index


def validate_packet(packet: dict[str, Any]) -> dict[str, Any]:
    """Validate a synthetic Maestro case packet."""

    ev = Evaluation()

    for key in REQUIRED_TOP_LEVEL:
        if key not in packet:
            ev.add("hold", "missing_top_level", f"Missing top-level field: {key}")

    case = _as_dict(packet.get("case"))
    maestro = _as_dict(packet.get("maestro"))
    evidence = [_as_dict(item) for item in _as_list(packet.get("evidence"))]
    policy = _as_dict(packet.get("policy"))
    decision = _as_dict(packet.get("decision"))
    controls = _as_dict(packet.get("controls"))

    if packet.get("packet_version") != "caseproof.v0.1":
        ev.add("hold", "packet_version", "Packet version is missing or not caseproof.v0.1")

    if "UiPath Maestro" not in str(maestro.get("orchestration_layer", "")):
        ev.add("hold", "maestro_layer_missing", "UiPath Maestro orchestration layer is not declared")

    if not maestro.get("case_url"):
        ev.add("hold", "case_url_missing", "Synthetic or real Maestro case URL is not bound")

    if not case.get("case_id"):
        ev.add("hold", "case_id_missing", "Case ID is missing")

    if str(decision.get("case_id", "")) and decision.get("case_id") != case.get("case_id"):
        ev.add("block", "case_subject_mismatch", "Decision references a different case ID")

    milestone_path = [str(stage) for stage in _as_list(maestro.get("case_stage_path"))]
    missing_milestones = _missing_milestones(milestone_path)
    if missing_milestones:
        ev.add(
            "block",
            "required_milestone_missing",
            "Required Maestro case milestone is missing: " + ", ".join(missing_milestones),
        )

    if controls.get("external_action_enabled") is True:
        ev.add("block", "external_action_enabled", "External business action is enabled before human approval")

    if controls.get("pii_redacted") is not True:
        ev.add("block", "pii_not_redacted", "Public-safe packet must mark PII as redacted")

    if controls.get("human_review_required") is not True:
        ev.add("block", "human_review_not_required", "Human review must remain mandatory")

    required_map = _as_dict(policy.get("required_evidence_by_action"))
    action = str(decision.get("agent_recommendation", case.get("requested_action", "")))
    required_evidence = [str(item) for item in _as_list(required_map.get(action))]
    evidence_by_kind = {str(item.get("kind")): item for item in evidence if item.get("present") is True}

    for kind in required_evidence:
        if kind not in evidence_by_kind:
            ev.add("hold", "required_evidence_missing", f"Required evidence kind is missing: {kind}")

    evidence_ids = _evidence_index(evidence)
    for ref in _as_list(decision.get("rationale_refs")):
        if str(ref) not in evidence_ids:
            ev.add("hold", "rationale_ref_missing", f"Decision rationale ref is not in evidence packet: {ref}")

    amount = float(decision.get("amount_usd", case.get("amount_usd", 0)) or 0)
    caps = _as_dict(policy.get("decision_caps"))
    auto_max = float(caps.get("auto_approve_max_usd", 0) or 0)
    human_min = float(caps.get("human_review_min_usd", auto_max + 1) or 0)
    route = str(decision.get("approval_route", ""))

    if amount > auto_max and route != "human_review":
        ev.add("block", "amount_requires_human_review", "Amount exceeds auto-action cap without human review route")

    if amount >= human_min and route != "human_review":
        ev.add("block", "human_review_route_missing", "Policy requires human review for this amount")

    blocked_reasons = {str(reason) for reason in _as_list(policy.get("blocked_reasons"))}
    override_reason = str(decision.get("override_reason") or "")
    if override_reason and override_reason in blocked_reasons:
        ev.add("block", "blocked_override_reason", "Decision uses a blocked policy override reason")

    confidence = float(decision.get("confidence", 0) or 0)
    if confidence < 0.5:
        ev.add("hold", "low_confidence", "Agent confidence is below review-ready threshold")

    findings = [finding.__dict__ for finding in ev.findings]
    return {
        "project": "CaseProof AI",
        "decision": ev.decision,
        "finding_count": len(findings),
        "findings": findings,
        "case_id": case.get("case_id"),
        "maestro_case_url": maestro.get("case_url"),
        "strongest_allowed_action": "open_human_review_task",
        "blocked_actions": ["auto_approve", "issue_refund", "settle_claim", "update_customer_record", "close_case"],
        "claim_ceiling": (
            "synthetic public-safe Maestro case validation only; not production approval, "
            "legal compliance certification, security certification, or field validation"
        ),
    }
