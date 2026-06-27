from __future__ import annotations

import json
from pathlib import Path

from caseproof.validator import ALLOW, BLOCK, HOLD, validate_packet


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "fixtures"


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def test_allow_review_refund_case() -> None:
    receipt = validate_packet(load_fixture("allow_review_refund_case.json"))
    assert receipt["decision"] == ALLOW
    assert receipt["strongest_allowed_action"] == "open_human_review_task"


def test_hold_missing_evidence() -> None:
    receipt = validate_packet(load_fixture("hold_missing_evidence.json"))
    assert receipt["decision"] == HOLD
    assert any(f["code"] == "required_evidence_missing" for f in receipt["findings"])


def test_block_policy_bypass() -> None:
    receipt = validate_packet(load_fixture("block_policy_bypass.json"))
    assert receipt["decision"] == BLOCK
    codes = {f["code"] for f in receipt["findings"]}
    assert "external_action_enabled" in codes
    assert "amount_requires_human_review" in codes
    assert "blocked_override_reason" in codes


def test_block_stage_skip() -> None:
    receipt = validate_packet(load_fixture("block_stage_skip.json"))
    assert receipt["decision"] == BLOCK
    assert any(f["code"] == "required_milestone_missing" for f in receipt["findings"])


def test_subject_mismatch_blocks() -> None:
    packet = load_fixture("allow_review_refund_case.json")
    packet["decision"]["case_id"] = "OTHER-CASE"
    receipt = validate_packet(packet)
    assert receipt["decision"] == BLOCK
    assert any(f["code"] == "case_subject_mismatch" for f in receipt["findings"])
