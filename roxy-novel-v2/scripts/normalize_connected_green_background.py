#!/usr/bin/env python3
"""Normalize only border-connected green-screen pixels to exact #00FF00."""

from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path

from PIL import Image


PURE_GREEN = (0, 255, 0)


def parse_hex_color(value: str) -> tuple[int, int, int]:
    value = value.strip().lstrip("#")
    if len(value) != 6:
        raise ValueError("target color must be #RRGGBB")
    return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))


def is_key_green(rgb: tuple[int, int, int]) -> bool:
    red, green, blue = rgb
    return (
        green >= 180
        and green - red >= 105
        and green - blue >= 105
        and green >= max(red, blue) * 2.25
    )


def normalize(
    source: Path,
    target: Path,
    target_color: tuple[int, int, int] = PURE_GREEN,
) -> dict[str, object]:
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

    normalized = 0
    rejected = 0
    while queue:
        x, y = queue.popleft()
        index = y * width + x
        if seen[index]:
            continue
        seen[index] = 1
        if not is_key_green(pixels[x, y]):
            rejected += 1
            continue

        if pixels[x, y] != target_color:
            normalized += 1
            pixels[x, y] = target_color

        if x > 0:
            queue.append((x - 1, y))
        if x + 1 < width:
            queue.append((x + 1, y))
        if y > 0:
            queue.append((x, y - 1))
        if y + 1 < height:
            queue.append((x, y + 1))

    target.parent.mkdir(parents=True, exist_ok=True)
    image.save(target)
    exact_target = sum(pixel == target_color for pixel in image.get_flattened_data())
    return {
        "ok": True,
        "input": str(source.resolve()),
        "output": str(target.resolve()),
        "size": [width, height],
        "normalized_pixels": normalized,
        "border_rejected_pixels": rejected,
        "target_color": f"#{target_color[0]:02X}{target_color[1]:02X}{target_color[2]:02X}",
        "exact_target_pixels": exact_target,
        "exact_target_ratio": exact_target / (width * height),
        "character_pixels_recolored": 0,
        "policy": "border-connected high-saturation green only",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("--output", required=True)
    parser.add_argument("--json-out")
    parser.add_argument(
        "--target-color",
        default="#00FF00",
        help="Replace border-connected green-screen pixels with this exact RGB color.",
    )
    args = parser.parse_args()

    report = normalize(
        Path(args.input).expanduser(),
        Path(args.output).expanduser(),
        parse_hex_color(args.target_color),
    )
    if args.json_out:
        report_path = Path(args.json_out).expanduser()
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
