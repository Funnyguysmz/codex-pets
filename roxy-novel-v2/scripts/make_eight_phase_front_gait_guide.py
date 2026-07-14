#!/usr/bin/env python3
"""Create an eight-phase front-three-quarter gait guide; pose reference only."""

from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "references/eight-phase-front-gait-guide.png"
CELLS_DIR = ROOT / "references/eight-phase-front-gait-cells"
CW, H, N = 256, 724, 8
BG = (0, 255, 0, 255)
GRAY = (210, 210, 215, 255)
EDGE = (38, 38, 46, 255)
RED = (235, 55, 55, 255)    # anatomical/image-left leg family
BLUE = (45, 105, 240, 255)  # anatomical/image-right leg family


POSES = [
    # left (red), right (blue), draw order
    ([(110, 370), (76, 485), (48, 600), (25, 625)], [(146, 370), (165, 490), (195, 620), (226, 630)], ("left", "right")),
    ([(110, 370), (105, 475), (100, 585), (92, 610)], [(146, 370), (153, 495), (164, 620), (190, 630)], ("left", "right")),
    ([(110, 370), (43, 452), (68, 548), (36, 580)], [(146, 370), (158, 495), (170, 620), (196, 630)], ("right", "left")),
    ([(110, 370), (68, 465), (54, 580), (35, 610)], [(146, 370), (158, 495), (170, 620), (196, 630)], ("right", "left")),
    ([(110, 370), (88, 490), (58, 620), (28, 630)], [(146, 370), (180, 485), (208, 600), (232, 625)], ("right", "left")),
    ([(110, 370), (103, 495), (90, 620), (65, 630)], [(146, 370), (151, 475), (156, 585), (164, 610)], ("right", "left")),
    ([(110, 370), (98, 495), (86, 620), (60, 630)], [(146, 370), (213, 452), (188, 548), (220, 580)], ("left", "right")),
    ([(110, 370), (98, 495), (86, 620), (60, 630)], [(146, 370), (188, 465), (202, 580), (221, 610)], ("left", "right")),
]


def limb(draw, pts, color, width=28):
    draw.line(pts, fill=EDGE, width=width + 8, joint="curve")
    draw.line(pts, fill=color, width=width, joint="curve")
    r = width // 2
    for x, y in pts[:-1]:
        draw.ellipse((x-r-4, y-r-4, x+r+4, y+r+4), fill=EDGE)
        draw.ellipse((x-r, y-r, x+r, y+r), fill=color)


strip = Image.new("RGBA", (CW * N, H), BG)
CELLS_DIR.mkdir(parents=True, exist_ok=True)
for idx, (left_pts, right_pts, order) in enumerate(POSES):
    cell = Image.new("RGBA", (CW, H), BG)
    d = ImageDraw.Draw(cell)
    d.ellipse((88, 62, 166, 140), fill=GRAY, outline=EDGE, width=6)
    d.polygon([(105, 132), (157, 150), (166, 356), (91, 356), (88, 160)], fill=GRAY, outline=EDGE)
    d.polygon([(161, 86), (198, 104), (161, 124)], fill=GRAY, outline=EDGE)
    d.ellipse((88, 332, 168, 397), fill=GRAY, outline=EDGE, width=6)
    limb(d, [(153, 175), (188, 245), (198, 330)], GRAY, 18)
    limb(d, [(101, 175), (73, 255), (88, 335)], GRAY, 18)
    d.line([(211, 82), (211, 666)], fill=EDGE, width=14)
    d.line([(211, 82), (211, 666)], fill=(132, 84, 48, 255), width=8)
    points = {"left": left_pts, "right": right_pts}
    colors = {"left": RED, "right": BLUE}
    for name in order:
        limb(d, points[name], colors[name], 30)
    strip.alpha_composite(cell, (idx * CW, 0))
    cell.convert("RGB").save(CELLS_DIR / f"{idx:02d}.png", quality=100)

OUT.parent.mkdir(parents=True, exist_ok=True)
strip.convert("RGB").save(OUT, quality=100)
print(OUT)
