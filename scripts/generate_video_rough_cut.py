"""Generate a silent rough-cut MP4 from static slides."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"
OUT = ASSETS / "caseproof_demo_rough_cut.mp4"

SLIDES = [
    ("CaseProof AI", "A human-review gate for high-value refund exception cases in UiPath Maestro."),
    ("The Problem", "An agent can prepare a refund case. Preparation is not approval."),
    ("Maestro Case Flow", "Intake -> Evidence -> Policy -> Risk -> Recommendation -> Human Review."),
    ("Required Evidence", "Order record, delivery proof, customer statement, policy snapshot, and rationale."),
    ("CaseProof Gate", "Studio Web or an API Workflow calls the validator before review."),
    ("Scenario 1: HOLD", "Customer statement is missing. The packet is not review-ready."),
    ("Scenario 2: REVIEW", "The packet is complete. The only allowed action is human review."),
    ("Scenario 3: BLOCK", "The agent tries to issue a refund above the auto-action cap."),
    ("Scenario 4: BLOCK", "Policy check and risk review milestones are missing."),
    ("What Runs", "python -m caseproof.cli fixtures/allow_review_refund_case.json --pretty"),
    ("What It Does Not Do", "It does not issue refunds, close cases, or update customer records."),
    ("Claim Boundary", "Synthetic public-safe prototype. Real Maestro binding is the next step."),
]


def main() -> int:
    ASSETS.mkdir(parents=True, exist_ok=True)
    try:
        from PIL import Image, ImageDraw, ImageFont
        import imageio_ffmpeg
    except Exception as exc:  # pragma: no cover
        raise SystemExit(f"video dependencies unavailable: {exc}")

    import subprocess

    def font(size: int):
        for name in ("arial.ttf", "Arial.ttf", "DejaVuSans.ttf"):
            try:
                return ImageFont.truetype(name, size)
            except Exception:
                pass
        return ImageFont.load_default()

    frames = []
    font_title = font(58)
    font_body = font(30)
    for idx, (title, text) in enumerate(SLIDES):
        path = ASSETS / f"caseproof_video_{idx:02d}.png"
        img = Image.new("RGB", (1280, 720), "#f7f9fb")
        draw = ImageDraw.Draw(img)
        draw.rectangle((0, 0, 1280, 110), fill="#0f4f6f")
        draw.text((60, 34), "CaseProof AI", fill="#ffffff", font=font_body)
        draw.text((80, 230), title, fill="#18202a", font=font_title)
        draw.text((82, 330), text, fill="#5f6b7a", font=font_body)
        draw.text((82, 620), "Allowed action: open human review task", fill="#5f6b7a", font=font_body)
        img.save(path)
        frames.append(path)

    list_file = ASSETS / "caseproof_video_frames.txt"
    list_file.write_text(
        "".join(f"file '{frame.as_posix()}'\nduration 8\n" for frame in frames) + f"file '{frames[-1].as_posix()}'\n",
        encoding="utf-8",
    )
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run(
        [ffmpeg, "-y", "-f", "concat", "-safe", "0", "-i", str(list_file), "-pix_fmt", "yuv420p", str(OUT)],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print(f"CASEPROOF_VIDEO_ROUGH_CUT_BUILT {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
