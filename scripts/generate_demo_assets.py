"""Generate receipts, dashboard HTML, and a PNG screenshot."""

from __future__ import annotations

import json
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from caseproof.validator import validate_packet  # noqa: E402

FIXTURES = ROOT / "fixtures"
RECEIPTS = ROOT / "receipts"
DOCS = ROOT / "docs"
ASSETS = DOCS / "assets"
DEMO = ROOT / "demo"

SCENARIOS = [
    {
        "fixture": "hold_missing_evidence.json",
        "title": "Scenario 1: HOLD",
        "subtitle": "Evidence is missing",
        "meaning": "The case may be valid, but it is not review-ready.",
    },
    {
        "fixture": "allow_review_refund_case.json",
        "title": "Scenario 2: REVIEW",
        "subtitle": "Ready for a person",
        "meaning": "The agent can open a human review task. It cannot approve the case.",
    },
    {
        "fixture": "block_policy_bypass.json",
        "title": "Scenario 3: BLOCK",
        "subtitle": "Policy is bypassed",
        "meaning": "The agent tries to auto-approve a case that requires review.",
    },
    {
        "fixture": "block_stage_skip.json",
        "title": "Scenario 4: BLOCK",
        "subtitle": "A Maestro stage was skipped",
        "meaning": "The case jumped from evidence collection to recommendation.",
    },
]


def load_receipts() -> list[dict]:
    receipts = []
    for scenario in SCENARIOS:
        packet = json.loads((FIXTURES / scenario["fixture"]).read_text(encoding="utf-8"))
        receipt = validate_packet(packet)
        receipt.update(scenario)
        receipts.append(receipt)
    return receipts


def write_receipts(receipts: list[dict]) -> None:
    RECEIPTS.mkdir(exist_ok=True)
    for receipt in receipts:
        name = Path(receipt["fixture"]).stem + "_receipt.json"
        (RECEIPTS / name).write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    index = {
        "project": "CaseProof AI",
        "scenario_count": len(receipts),
        "decisions": {r["fixture"]: r["decision"] for r in receipts},
        "claim_ceiling": "synthetic public-safe Maestro case validation only",
    }
    (RECEIPTS / "demo_receipt_index.json").write_text(json.dumps(index, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def decision_class(decision: str) -> str:
    if decision == "BLOCK":
        return "block"
    if decision == "HOLD":
        return "hold"
    return "allow"


def write_dashboard(receipts: list[dict]) -> None:
    DEMO.mkdir(exist_ok=True)
    cards = []
    for receipt in receipts:
        finding_items = "".join(
            f"<li><code>{escape(f['code'])}</code> {escape(f['message'])}</li>" for f in receipt["findings"][:4]
        )
        if not finding_items:
            finding_items = "<li>No blocking findings. Human review remains required.</li>"
        cards.append(
            f"""
      <section class="card {decision_class(receipt['decision'])}">
        <p class="eyebrow">{escape(receipt['title'])}</p>
        <h2>{escape(receipt['subtitle'])}</h2>
        <p>{escape(receipt['meaning'])}</p>
        <div class="decision">{escape(receipt['decision'])}</div>
        <ul>{finding_items}</ul>
      </section>
            """
        )
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CaseProof AI Demo</title>
  <style>
    :root {{
      --ink: #18202a;
      --muted: #5f6b7a;
      --line: #d9e1ea;
      --paper: #f7f9fb;
      --blue: #1769aa;
      --green: #1f8a4c;
      --amber: #a76800;
      --red: #b3261e;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Arial, Helvetica, sans-serif;
      color: var(--ink);
      background: white;
    }}
    header {{
      padding: 34px 42px 26px;
      border-bottom: 1px solid var(--line);
      background: #f2f6f9;
    }}
    h1 {{ margin: 0 0 8px; font-size: 34px; }}
    .lead {{ max-width: 760px; margin: 0; color: var(--muted); font-size: 17px; line-height: 1.5; }}
    main {{ padding: 28px 42px 38px; }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(280px, 1fr));
      gap: 18px;
      max-width: 1060px;
    }}
    .card {{
      border: 1px solid var(--line);
      border-left: 6px solid var(--blue);
      border-radius: 8px;
      padding: 20px;
      min-height: 250px;
      background: white;
    }}
    .card.hold {{ border-left-color: var(--amber); }}
    .card.allow {{ border-left-color: var(--green); }}
    .card.block {{ border-left-color: var(--red); }}
    .eyebrow {{ margin: 0 0 8px; color: var(--muted); font-size: 13px; text-transform: uppercase; font-weight: 700; }}
    h2 {{ margin: 0 0 10px; font-size: 22px; }}
    p {{ line-height: 1.45; }}
    .decision {{ margin: 14px 0; font-weight: 700; font-size: 18px; }}
    ul {{ margin: 0; padding-left: 20px; color: var(--muted); line-height: 1.5; }}
    footer {{ padding: 0 42px 28px; color: var(--muted); }}
  </style>
</head>
<body>
  <header>
    <h1>CaseProof AI</h1>
    <p class="lead">A small gate for Maestro cases. It asks whether an agent-handled case has enough evidence, policy fit, and stage history to be sent to a person.</p>
  </header>
  <main>
    <div class="grid">
{''.join(cards)}
    </div>
  </main>
  <footer>External business actions stay disabled. The only allowed action is human review.</footer>
</body>
</html>
"""
    (DEMO / "index.html").write_text(html, encoding="utf-8")


def write_png(receipts: list[dict]) -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    try:
        from PIL import Image, ImageDraw, ImageFont
    except Exception as exc:  # pragma: no cover
        (ASSETS / "caseproof_dashboard_desktop.txt").write_text(f"Pillow unavailable: {exc}\n", encoding="utf-8")
        return

    def font(size: int):
        for name in ("arial.ttf", "Arial.ttf", "DejaVuSans.ttf"):
            try:
                return ImageFont.truetype(name, size)
            except Exception:
                pass
        return ImageFont.load_default()

    width, height = 1200, 760
    img = Image.new("RGB", (width, height), "#ffffff")
    draw = ImageDraw.Draw(img)
    font_title = font(42)
    font_h = font(25)
    font_body = font(17)
    font_small = font(14)
    draw.rectangle((0, 0, width, 145), fill="#f2f6f9")
    draw.text((42, 32), "CaseProof AI", fill="#18202a", font=font_title)
    draw.text((42, 92), "A human-review gate for AI-handled UiPath Maestro cases.", fill="#5f6b7a", font=font_body)

    colors = {"HOLD": "#a76800", "BLOCK": "#b3261e", "ALLOW_HUMAN_REVIEW_ONLY": "#1f8a4c"}
    positions = [(42, 185), (620, 185), (42, 455), (620, 455)]
    for receipt, (x, y) in zip(receipts, positions):
        draw.rectangle((x, y, x + 520, y + 220), outline="#d9e1ea", width=2)
        draw.rectangle((x, y, x + 8, y + 220), fill=colors.get(receipt["decision"], "#1769aa"))
        draw.text((x + 24, y + 22), receipt["title"], fill="#5f6b7a", font=font_small)
        draw.text((x + 24, y + 50), receipt["subtitle"], fill="#18202a", font=font_h)
        draw.text((x + 24, y + 90), receipt["decision"], fill=colors.get(receipt["decision"], "#1769aa"), font=font_h)
        if receipt["findings"]:
            line = receipt["findings"][0]["message"]
        else:
            line = "No blocking findings. Human review remains required."
        draw.text((x + 24, y + 135), line[:62], fill="#5f6b7a", font=font_body)
    draw.text((42, 718), "External action: disabled. Allowed action: open human review task.", fill="#5f6b7a", font=font_body)
    img.save(ASSETS / "caseproof_dashboard_desktop.png")


def main() -> int:
    receipts = load_receipts()
    write_receipts(receipts)
    write_dashboard(receipts)
    write_png(receipts)
    print("CASEPROOF_DEMO_ASSETS_GENERATED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
