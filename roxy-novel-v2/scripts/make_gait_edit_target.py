#!/usr/bin/env python3
"""Build a pose-only edit target; never use this image as a final pet row."""

from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "qa/candidates/running-right-final/frames/running-right/00.png"
OUTPUT = ROOT / "references/gait-edit-target.png"
CELL_W, CELL_H = 192, 208
MAGENTA = (255, 0, 255, 255)
RIGHT = (35, 115, 255, 245)  # anatomical right leg
LEFT = (245, 55, 55, 245)  # anatomical left leg
OUTLINE = (35, 35, 45, 255)


POSES = [
    {"right": [(100, 143), (112, 168), (132, 196), (147, 199)], "left": [(88, 143), (78, 164), (59, 190), (47, 197)], "order": ["left", "right"]},
    {"right": [(100, 143), (104, 171), (111, 198), (125, 200)], "left": [(88, 143), (76, 166), (65, 190), (56, 198)], "order": ["left", "right"]},
    {"right": [(100, 143), (99, 172), (100, 198), (113, 200)], "left": [(88, 143), (91, 163), (89, 184), (101, 191)], "order": ["right", "left"]},
    {"right": [(100, 143), (92, 171), (84, 197), (97, 200)], "left": [(88, 143), (112, 160), (119, 183), (132, 191)], "order": ["right", "left"]},
    {"right": [(100, 143), (80, 164), (59, 190), (47, 197)], "left": [(88, 143), (110, 168), (132, 196), (147, 199)], "order": ["right", "left"]},
    {"right": [(100, 143), (76, 166), (65, 190), (56, 198)], "left": [(88, 143), (104, 171), (111, 198), (125, 200)], "order": ["right", "left"]},
    {"right": [(100, 143), (91, 163), (89, 184), (101, 191)], "left": [(88, 143), (99, 172), (100, 198), (113, 200)], "order": ["left", "right"]},
    {"right": [(100, 143), (112, 160), (119, 183), (132, 191)], "left": [(88, 143), (92, 171), (84, 197), (97, 200)], "order": ["left", "right"]},
]


def draw_limb(draw: ImageDraw.ImageDraw, points, color):
    draw.line(points, fill=OUTLINE, width=17, joint="curve")
    draw.line(points, fill=color, width=12, joint="curve")
    for x, y in points[:-1]:
        draw.ellipse((x - 7, y - 7, x + 7, y + 7), fill=OUTLINE)
        draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=color)


def main():
    source = Image.open(SOURCE).convert("RGBA")
    strip = Image.new("RGBA", (CELL_W * len(POSES), CELL_H), MAGENTA)
    for index, pose in enumerate(POSES):
        cell = Image.new("RGBA", (CELL_W, CELL_H), MAGENTA)
        cell.alpha_composite(source)
        overlay = Image.new("RGBA", (CELL_W, CELL_H), (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        for name in pose["order"]:
            draw_limb(draw, pose[name], RIGHT if name == "right" else LEFT)
        cell.alpha_composite(overlay)
        strip.alpha_composite(cell, (index * CELL_W, 0))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    strip.convert("RGB").save(OUTPUT, quality=100)
    print(OUTPUT)


if __name__ == "__main__":
    main()
