#!/usr/bin/env python3
"""Measure eight-frame directional gait stability and duplicate-pose risk."""

from __future__ import annotations

import argparse
import json
import statistics
from pathlib import Path

from PIL import Image


def visible_mask(image: Image.Image) -> Image.Image:
    return image.getchannel("A").point(lambda value: 255 if value > 16 else 0)


def centered_mask(mask: Image.Image) -> Image.Image:
    bbox = mask.getbbox()
    output = Image.new("1", mask.size)
    if bbox is None:
        return output
    crop = mask.crop(bbox).convert("1")
    left = (mask.width - crop.width) // 2
    top = (mask.height - crop.height) // 2
    output.paste(crop, (left, top))
    return output


def iou(first: Image.Image, second: Image.Image) -> float:
    a = first.convert("1")
    b = second.convert("1")
    intersection = sum(x and y for x, y in zip(a.get_flattened_data(), b.get_flattened_data()))
    union = sum(x or y for x, y in zip(a.get_flattened_data(), b.get_flattened_data()))
    return intersection / union if union else 1.0


def color_centroid(image: Image.Image, family: str) -> dict[str, object]:
    points: list[tuple[int, int]] = []
    for y in range(image.height // 2, image.height):
        for x in range(image.width):
            red, green, blue, alpha = image.getpixel((x, y))
            if alpha <= 32:
                continue
            if family == "blue":
                selected = blue >= 90 and blue > red * 1.18 and blue > green * 1.05
            else:
                selected = red >= 65 and red > green * 1.12 and red > blue * 1.22
            if selected:
                points.append((x, y))
    if not points:
        return {"pixels": 0, "centroid": None, "bbox": None}
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    return {
        "pixels": len(points),
        "centroid": [round(statistics.mean(xs), 2), round(statistics.mean(ys), 2)],
        "bbox": [min(xs), min(ys), max(xs) + 1, max(ys) + 1],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("frames_dir")
    parser.add_argument("--json-out", required=True)
    args = parser.parse_args()

    frames_dir = Path(args.frames_dir).expanduser().resolve()
    paths = [frames_dir / f"{index:02d}.png" for index in range(8)]
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise SystemExit(f"missing gait frames: {', '.join(missing)}")

    frames = [Image.open(path).convert("RGBA") for path in paths]
    masks = [visible_mask(frame) for frame in frames]
    centered = [centered_mask(mask) for mask in masks]
    metrics = []
    for index, (frame, mask) in enumerate(zip(frames, masks)):
        bbox = mask.getbbox()
        area = sum(value > 0 for value in mask.get_flattened_data())
        metrics.append(
            {
                "frame": index,
                "bbox": list(bbox) if bbox else None,
                "width": 0 if bbox is None else bbox[2] - bbox[0],
                "height": 0 if bbox is None else bbox[3] - bbox[1],
                "baseline": None if bbox is None else bbox[3] - 1,
                "area": area,
                "blue_lower_body": color_centroid(frame, "blue"),
                "brown_lower_body": color_centroid(frame, "brown"),
            }
        )

    adjacent = []
    for index in range(8):
        following = (index + 1) % 8
        adjacent.append(
            {
                "pair": [index, following],
                "centered_silhouette_iou": round(iou(centered[index], centered[following]), 4),
            }
        )
    half_cycle = [
        {
            "pair": [index, index + 4],
            "centered_silhouette_iou": round(iou(centered[index], centered[index + 4]), 4),
        }
        for index in range(4)
    ]

    heights = [metric["height"] for metric in metrics]
    areas = [metric["area"] for metric in metrics]
    report = {
        "ok": True,
        "frames_dir": str(frames_dir),
        "frame_metrics": metrics,
        "height_cv": round(statistics.pstdev(heights) / statistics.mean(heights), 5),
        "area_cv": round(statistics.pstdev(areas) / statistics.mean(areas), 5),
        "adjacent_pairs": adjacent,
        "half_cycle_pairs": half_cycle,
        "review_note": "Color masks are evidence only; visually confirm anatomical leg identity and phase semantics.",
    }
    output = Path(args.json_out).expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
