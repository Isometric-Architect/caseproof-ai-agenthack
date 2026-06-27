"""Print the CaseProof demo decisions."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from caseproof.validator import validate_packet  # noqa: E402


SCENARIOS = [
    ("hold_missing_evidence.json", "Missing evidence"),
    ("allow_review_refund_case.json", "Ready for human review"),
    ("block_policy_bypass.json", "Policy bypass"),
    ("block_stage_skip.json", "Skipped Maestro stage"),
]


def main() -> int:
    for fixture, label in SCENARIOS:
        packet = json.loads((ROOT / "fixtures" / fixture).read_text(encoding="utf-8"))
        receipt = validate_packet(packet)
        print(f"{label:24} {fixture:32} -> {receipt['decision']}")
        for finding in receipt["findings"]:
            print(f"  - {finding['code']}: {finding['message']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

