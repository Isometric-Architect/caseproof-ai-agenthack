from __future__ import annotations

from caseproof.maestro_adapter import build_packet_from_redacted_export


def test_build_packet_from_redacted_export() -> None:
    packet = build_packet_from_redacted_export(
        {
            "case": {
                "case_id": "CP-ADAPTER-001",
                "amount_usd": 42,
                "requested_action": "approve_refund",
            },
            "maestro": {"orchestration_layer": "UiPath Maestro"},
            "evidence": [],
            "policy": {},
            "decision": {},
            "controls": {},
        }
    )
    assert packet["packet_version"] == "caseproof.v0.1"
    assert packet["case"]["case_id"] == "CP-ADAPTER-001"
    assert packet["maestro"]["orchestration_layer"] == "UiPath Maestro"

