#!/usr/bin/env python3
"""Draw an eight-phase lower-body guide with persistent near/far boot views."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw


WIDTH = 2048
HEIGHT = 600
SLOT = WIDTH // 8
GREEN = (0, 255, 0)
OUTLINE = (42, 39, 48)
NEAR = (241, 226, 196)
FAR = (177, 177, 169)
BROWN = (91, 60, 40)
PELVIS = (203, 202, 209)


# Each phase stores (far hip/knee/ankle/toe, near hip/knee/ankle/toe).
PHASES = [
    (((-13, 0), (-55, 130), (-90, 270), (-120, 275)), ((13, 0), (55, 130), (85, 270), (120, 275))),
    (((-13, 0), (-55, 130), (-80, 205), (-115, 225)), ((13, 0), (30, 140), (25, 280), (60, 280))),
    (((-13, 0), (0, 135), (12, 220), (45, 238)), ((13, 0), (25, 140), (25, 280), (60, 280))),
    (((-13, 0), (58, 90), (92, 180), (122, 194)), ((13, 0), (-35, 140), (-68, 280), (-102, 286))),
    (((-13, 0), (58, 130), (92, 270), (126, 275)), ((13, 0), (-48, 130), (-84, 270), (-118, 275))),
    (((-13, 0), (30, 140), (25, 280), (60, 280)), ((13, 0), (-48, 130), (-75, 205), (-108, 225))),
    (((-13, 0), (18, 140), (22, 280), (57, 280)), ((13, 0), (38, 135), (48, 220), (82, 238))),
    (((-13, 0), (-35, 140), (-68, 280), (-102, 286)), ((13, 0), (62, 90), (96, 180), (126, 194))),
]


def point(origin_x: int, origin_y: int, offset: tuple[int, int]) -> tuple[int, int]:
    return (origin_x + offset[0], origin_y + offset[1])


def limb(draw: ImageDraw.ImageDraw, points: list[tuple[int, int]], fill: tuple[int, int, int], *, near: bool) -> None:
    draw.line(points[:3], fill=OUTLINE, width=38, joint="curve")
    draw.line(points[:3], fill=fill, width=28, joint="curve")
    draw.line(points[2:], fill=OUTLINE, width=32, joint="curve")
    draw.line(points[2:], fill=fill, width=22, joint="curve")
    for x, y in points[1:3]:
        draw.ellipse((x - 18, y - 18, x + 18, y + 18), fill=OUTLINE)
        draw.ellipse((x - 12, y - 12, x + 12, y + 12), fill=fill)
    if near:
        ankle_x, ankle_y = points[2]
        draw.ellipse(
            (ankle_x - 13, ankle_y - 7, ankle_x + 13, ankle_y + 7),
            fill=BROWN,
            outline=OUTLINE,
            width=3,
        )


def main() -> None:
    output = Path(__file__).resolve().parents[1] / "references" / "eight-phase-depth-boot-guide.png"
    image = Image.new("RGB", (WIDTH, HEIGHT), GREEN)
    draw = ImageDraw.Draw(image)

    for index, (far_offsets, near_offsets) in enumerate(PHASES):
        center_x = index * SLOT + SLOT // 2
        hip_y = 170
        draw.ellipse((center_x - 48, hip_y - 38, center_x + 48, hip_y + 38), fill=PELVIS, outline=OUTLINE, width=8)
        far_points = [point(center_x, hip_y, offset) for offset in far_offsets]
        near_points = [point(center_x, hip_y, offset) for offset in near_offsets]
        limb(draw, far_points, FAR, near=False)
        limb(draw, near_points, NEAR, near=True)

        # Minimal right-facing direction cue, not a body-proportion reference.
        draw.polygon(
            [(center_x - 12, 80), (center_x + 35, 100), (center_x - 12, 120)],
            fill=PELVIS,
            outline=OUTLINE,
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output)
    print(output)


if __name__ == "__main__":
    main()
