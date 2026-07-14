#!/usr/bin/env python3
"""Remap connected magenta reference backgrounds to pure green; reference use only."""

from collections import deque
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
JOBS = [
    (ROOT / "references/running-right-gait-locked-colored.png", ROOT / "references/running-right-gait-locked-colored-green.png"),
    (ROOT / "references/gait-keyposes-fourphase-approved.png", ROOT / "references/gait-keyposes-fourphase-approved-green.png"),
]


def magenta_like(rgb):
    r, g, b = rgb
    return r > 115 and b > 115 and g < 175 and min(r, b) > g * 1.18


def remap(source: Path, target: Path):
    image = Image.open(source).convert("RGB")
    w, h = image.size
    pixels = image.load()
    seen = bytearray(w * h)
    queue = deque()
    for x in range(w):
        queue.append((x, 0)); queue.append((x, h - 1))
    for y in range(h):
        queue.append((0, y)); queue.append((w - 1, y))
    while queue:
        x, y = queue.popleft()
        pos = y * w + x
        if seen[pos]:
            continue
        seen[pos] = 1
        if not magenta_like(pixels[x, y]):
            continue
        pixels[x, y] = (0, 255, 0)
        if x: queue.append((x - 1, y))
        if x + 1 < w: queue.append((x + 1, y))
        if y: queue.append((x, y - 1))
        if y + 1 < h: queue.append((x, y + 1))
    target.parent.mkdir(parents=True, exist_ok=True)
    image.save(target)
    print(target)


for src, dst in JOBS:
    remap(src, dst)
