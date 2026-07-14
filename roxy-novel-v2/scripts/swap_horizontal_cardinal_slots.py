#!/usr/bin/env python3
"""Swap the already-approved 090/270 look cells and matching blind-sheet panels.

This repairs a slot-mapping error without altering or regenerating character art.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image


CELL_WIDTH = 192
CELL_HEIGHT = 208
LABEL_HEIGHT = 28
ROW_090 = 9
ROW_270 = 10
COLUMN = 4
BLIND_PAIR_ROW = 3


def swap_atlas_cells(atlas_path: Path) -> tuple[str, str]:
    before = hashlib.sha256(atlas_path.read_bytes()).hexdigest()
    with Image.open(atlas_path) as opened:
        atlas = opened.convert("RGBA")
    if atlas.size != (1536, 2288):
        raise SystemExit(f"expected 1536x2288 atlas, got {atlas.size}")

    x0 = COLUMN * CELL_WIDTH
    box_090 = (x0, ROW_090 * CELL_HEIGHT, x0 + CELL_WIDTH, (ROW_090 + 1) * CELL_HEIGHT)
    box_270 = (x0, ROW_270 * CELL_HEIGHT, x0 + CELL_WIDTH, (ROW_270 + 1) * CELL_HEIGHT)
    cell_090 = atlas.crop(box_090)
    cell_270 = atlas.crop(box_270)
    atlas.paste(cell_270, box_090[:2])
    atlas.paste(cell_090, box_270[:2])
    atlas.save(atlas_path)
    after = hashlib.sha256(atlas_path.read_bytes()).hexdigest()
    return before, after


def swap_blind_panels(sheet_path: Path) -> None:
    with Image.open(sheet_path) as opened:
        sheet = opened.convert("RGB")
    expected = (2 * CELL_WIDTH, 14 * (CELL_HEIGHT + LABEL_HEIGHT))
    if sheet.size != expected:
        raise SystemExit(f"expected blind sheet {expected}, got {sheet.size}")

    y0 = BLIND_PAIR_ROW * (CELL_HEIGHT + LABEL_HEIGHT) + LABEL_HEIGHT
    left_box = (0, y0, CELL_WIDTH, y0 + CELL_HEIGHT)
    right_box = (CELL_WIDTH, y0, 2 * CELL_WIDTH, y0 + CELL_HEIGHT)
    left = sheet.crop(left_box)
    right = sheet.crop(right_box)
    sheet.paste(right, left_box[:2])
    sheet.paste(left, right_box[:2])
    sheet.save(sheet_path)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--atlas-png", required=True)
    parser.add_argument("--atlas-webp", required=True)
    parser.add_argument("--blind-sheet", required=True)
    parser.add_argument("--answer-key", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    atlas_png = Path(args.atlas_png).resolve()
    atlas_webp = Path(args.atlas_webp).resolve()
    blind_sheet = Path(args.blind_sheet).resolve()
    answer_key = Path(args.answer_key).resolve()
    report = Path(args.report).resolve()

    before, after_png = swap_atlas_cells(atlas_png)
    with Image.open(atlas_png) as opened:
        opened.convert("RGBA").save(
            atlas_webp, format="WEBP", lossless=True, quality=100, method=6, exact=True
        )
    after_webp = hashlib.sha256(atlas_webp.read_bytes()).hexdigest()
    swap_blind_panels(blind_sheet)

    key = json.loads(answer_key.read_text(encoding="utf-8"))
    key["atlas_sha256"] = after_webp
    answer_key.write_text(json.dumps(key, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(
        json.dumps(
            {
                "ok": True,
                "operation": "swap complete 090 and 270 look cells",
                "reason": "correct deterministic slot-mapping reversal; no art regenerated",
                "atlas_png_sha256_before": before,
                "atlas_png_sha256_after": after_png,
                "atlas_webp_sha256_after": after_webp,
                "blind_sheet_horizontal_4_panels_swapped": True,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
