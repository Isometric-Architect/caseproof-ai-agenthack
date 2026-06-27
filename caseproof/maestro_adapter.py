"""Adapter helpers for redacted UiPath Maestro case exports."""

from __future__ import annotations

from typing import Any


def build_packet_from_redacted_export(export: dict[str, Any]) -> dict[str, Any]:
    """Normalize a redacted Maestro-like export into a CaseProof packet.

    This helper is intentionally small and public-safe. It expects already
    redacted input and does not call external services.
    """

    case = export.get("case", {})
    return {
        "packet_version": "caseproof.v0.1",
        "case": {
            "case_id": case.get("case_id", "CASE-REDACTED"),
            "case_type": case.get("case_type", "refund_exception"),
            "region": case.get("region", "synthetic"),
            "amount_usd": case.get("amount_usd", 0),
            "requested_action": case.get("requested_action", "approve_refund"),
            "risk_tier": case.get("risk_tier", "medium"),
        },
        "maestro": export.get("maestro", {}),
        "evidence": export.get("evidence", []),
        "policy": export.get("policy", {}),
        "decision": export.get("decision", {}),
        "controls": export.get("controls", {}),
    }

