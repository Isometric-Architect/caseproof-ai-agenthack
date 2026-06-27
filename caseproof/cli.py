"""Command line interface for CaseProof AI."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .validator import validate_packet


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a CaseProof Maestro case packet.")
    parser.add_argument("packet", type=Path, help="Path to a JSON packet")
    parser.add_argument("--pretty", action="store_true", help="Print indented JSON")
    args = parser.parse_args()

    packet = json.loads(args.packet.read_text(encoding="utf-8"))
    receipt = validate_packet(packet)
    if args.pretty:
        print(json.dumps(receipt, indent=2, sort_keys=True))
    else:
        print(json.dumps(receipt, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

