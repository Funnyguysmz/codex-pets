#!/usr/bin/env python3
"""Create a pose-only guide with the raised knee on the image's left side."""

from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
OUT_LEFT = ROOT / "references/opposite-knee-screen-left-guide.png"
OUT_RIGHT = ROOT / "references/opposite-knee-screen-right-guide.png"
W = H = 768
BG = (0, 255, 0, 255)
GRAY = (210, 210, 215, 255)
EDGE = (40, 40, 48, 255)
RED = (235, 55, 55, 255)   # image-left moving leg
BLUE = (45, 105, 240, 255) # image-right support leg


def limb(draw, pts, color, width=44):
    draw.line(pts, fill=EDGE, width=width + 10, joint="curve")
    draw.line(pts, fill=color, width=width, joint="curve")
    r = width // 2
    for x, y in pts[:-1]:
        draw.ellipse((x-r-5, y-r-5, x+r+5, y+r+5), fill=EDGE)
        draw.ellipse((x-r, y-r, x+r, y+r), fill=color)


def base_figure():
    img = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.ellipse((302, 75, 442, 215), fill=GRAY, outline=EDGE, width=8)
    d.polygon([(345, 190), (445, 225), (455, 420), (315, 420), (310, 245)], fill=GRAY, outline=EDGE)
    d.polygon([(442, 125), (505, 155), (442, 180)], fill=GRAY, outline=EDGE)
    d.ellipse((300, 385, 458, 468), fill=GRAY, outline=EDGE, width=8)
    limb(d, [(430, 250), (505, 330), (535, 430)], GRAY, 28)
    limb(d, [(330, 250), (285, 345), (315, 435)], GRAY, 28)
    d.line([(552, 135), (552, 690)], fill=EDGE, width=18)
    d.line([(552, 135), (552, 690)], fill=(132, 84, 48, 255), width=12)
    return img, d


left_img, left_draw = base_figure()
limb(left_draw, [(422, 430), (450, 555), (458, 674), (505, 690)], BLUE, 48)
limb(left_draw, [(342, 430), (238, 492), (278, 595), (225, 630)], RED, 48)

right_img, right_draw = base_figure()
limb(right_draw, [(342, 430), (315, 555), (305, 674), (260, 690)], RED, 48)
limb(right_draw, [(422, 430), (525, 492), (485, 595), (540, 630)], BLUE, 48)

OUT_LEFT.parent.mkdir(parents=True, exist_ok=True)
left_img.convert("RGB").save(OUT_LEFT, quality=100)
right_img.convert("RGB").save(OUT_RIGHT, quality=100)
print(OUT_LEFT)
print(OUT_RIGHT)
