"""Build a public-safe review ZIP."""

from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent / "CASEPROOF_AI_AGENTHACK_PUBLIC_REPO_PACKAGE_20260627.zip"
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".venv", "build", "dist"}


def include(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return path.is_file() and not any(part in SKIP_DIRS for part in rel.parts)


def main() -> int:
    files = [path for path in ROOT.rglob("*") if include(path)]
    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            zf.write(path, path.relative_to(ROOT))
    digest = hashlib.sha256(OUT.read_bytes()).hexdigest()
    receipt = {
        "package": str(OUT),
        "sha256": digest,
        "file_count": len(files),
        "claim_ceiling": "public-safe review package only",
    }
    (ROOT / "docs" / "review_package_receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"CASEPROOF_REVIEW_PACKAGE_BUILT {OUT}")
    print(f"sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

