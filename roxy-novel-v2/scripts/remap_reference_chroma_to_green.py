#!/usr/bin/env python3
"""Remap only border-connected magenta chroma pixels to exact green."""

from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path

from PIL import Image


GREEN = (0, 255, 0)


def magenta_like(rgb: tuple[int, int, int]) -> bool:
    red, green, blue = rgb
    return red > 115 and blue > 115 and green < 175 and min(red, blue) > green * 1.18


def remap(source: Path, target: Path) -> dict[str, object]:
    image = Image.open(source).convert("RGB")
    width, height = image.size
    pixels = image.load()
    seen = bytearray(width * height)
    queue: deque[tuple[int, int]] = deque()
    for x in range(width):
        queue.append((x, 0))
        queue.append((x, height - 1))
    for y in range(height):
        queue.append((0, y))
        queue.append((width - 1, y))

    changed = 0
    while queue:
        x, y = queue.popleft()
        index = y * width + x
        if seen[index]:
            continue
        seen[index] = 1
        if not magenta_like(pixels[x, y]):
            continue
        if pixels[x, y] != GREEN:
            pixels[x, y] = GREEN
            changed += 1
        if x:
            queue.append((x - 1, y))
        if x + 1 < width:
            queue.append((x + 1, y))
        if y:
            queue.append((x, y - 1))
        if y + 1 < height:
            queue.append((x, y + 1))

    target.parent.mkdir(parents=True, exist_ok=True)
    image.save(target)
    exact_green = sum(pixel == GREEN for pixel in image.get_flattened_data())
    return {
        "ok": True,
        "input": str(source.resolve()),
        "output": str(target.resolve()),
        "size": [width, height],
        "changed_pixels": changed,
        "exact_green_pixels": exact_green,
        "exact_green_ratio": exact_green / (width * height),
        "character_pixels_recolored": 0,
        "policy": "border-connected magenta-like pixels only",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("--output", required=True)
    parser.add_argument("--json-out")
    args = parser.parse_args()
    report = remap(Path(args.input).expanduser(), Path(args.output).expanduser())
    if args.json_out:
        path = Path(args.json_out).expanduser()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
