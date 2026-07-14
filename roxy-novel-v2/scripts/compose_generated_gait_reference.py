#!/usr/bin/env python3
"""Normalize eight generated pose references into one guide; never a final row."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = ROOT / "references/gait-generated-cells"
OUTPUT = ROOT / "references/gait-generated-eight-pose-reference.png"
CELL_W, HEIGHT, COUNT = 256, 724, 8
TARGET_H, BASELINE = 590, 665
GREEN = (0, 255, 0, 255)


def foreground_alpha(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    pixels = list(rgba.getdata())
    cleaned = []
    for r, g, b, a in pixels:
        green_like = g > 145 and g > r * 1.28 and g > b * 1.28
        if green_like:
            cleaned.append((r, g, b, 0))
        else:
            cleaned.append((r, g, b, a))
    rgba.putdata(cleaned)
    return rgba


canvas = Image.new("RGBA", (CELL_W * COUNT, HEIGHT), GREEN)
for idx in range(COUNT):
    source = INPUT_DIR / f"{idx:02d}.png"
    image = foreground_alpha(Image.open(source))
    bbox = image.getbbox()
    if not bbox:
        raise RuntimeError(f"no foreground found: {source}")
    crop = image.crop(bbox)
    scale = min(TARGET_H / crop.height, (CELL_W - 20) / crop.width)
    size = (max(1, round(crop.width * scale)), max(1, round(crop.height * scale)))
    crop = crop.resize(size, Image.Resampling.LANCZOS)
    x = idx * CELL_W + (CELL_W - crop.width) // 2
    y = BASELINE - crop.height
    canvas.alpha_composite(crop, (x, y))

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
canvas.convert("RGB").save(OUTPUT, quality=100)
print(OUTPUT)
