"""Final local pre-submit checks."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from caseproof.validator import validate_packet  # noqa: E402

REQUIRED = [
    "README.md",
    "LICENSE",
    "caseproof/validator.py",
    "demo/index.html",
    "docs/FINAL_DEVPOST_FIELDS.md",
    "docs/CLAIM_CEILING.md",
    "docs/PUBLIC_PRIVATE_BOUNDARY.md",
    "docs/assets/caseproof_dashboard_desktop.png",
    "docs/CaseProof_AI_AgentHack_Deck_Draft.pptx",
]

EXPECTED = {
    "hold_missing_evidence.json": "HOLD",
    "allow_review_refund_case.json": "ALLOW_HUMAN_REVIEW_ONLY",
    "block_policy_bypass.json": "BLOCK",
    "block_stage_skip.json": "BLOCK",
}


def run(cmd: list[str]) -> dict:
    proc = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    return {
        "cmd": cmd,
        "returncode": proc.returncode,
        "stdout": proc.stdout[-4000:],
        "stderr": proc.stderr[-4000:],
    }


def main() -> int:
    missing = [item for item in REQUIRED if not (ROOT / item).exists()]
    fixture_results = {}
    for name, expected in EXPECTED.items():
        packet = json.loads((ROOT / "fixtures" / name).read_text(encoding="utf-8"))
        receipt = validate_packet(packet)
        fixture_results[name] = receipt["decision"]
        if receipt["decision"] != expected:
            missing.append(f"unexpected decision for {name}: {receipt['decision']} != {expected}")

    pytest_result = run([sys.executable, "-m", "pytest"])
    secret_result = run([sys.executable, "scripts/secret_scan.py", "."])

    report = {
        "project": "CaseProof AI",
        "missing_or_failed": missing,
        "fixture_results": fixture_results,
        "pytest_returncode": pytest_result["returncode"],
        "secret_scan_returncode": secret_result["returncode"],
        "claim_ceiling": "public-safe local prototype only",
    }
    (ROOT / "docs" / "final_pre_submit_check.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    ok = not missing and pytest_result["returncode"] == 0 and secret_result["returncode"] == 0
    print("FINAL_PRE_SUBMIT_CHECK_PASS" if ok else "FINAL_PRE_SUBMIT_CHECK_FAIL")
    if not ok:
        print(json.dumps(report, indent=2, sort_keys=True))
        print(pytest_result["stdout"])
        print(pytest_result["stderr"])
        print(secret_result["stdout"])
        print(secret_result["stderr"])
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

