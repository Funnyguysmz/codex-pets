#!/usr/bin/env python3
"""Promote approved green-key frames and write an accurate mixed-method manifest."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
RETAINED_BASELINE = Path(
    "/Users/mac/Documents/Codex/2026-07-12/new-chat/work/roxy-novel/frames"
)
FRAME_COUNTS = {
    "idle": 6,
    "running-right": 8,
    "running-left": 8,
    "waving": 4,
    "jumping": 5,
    "failed": 8,
    "waiting": 6,
    "running": 6,
    "review": 6,
}


def source_for(state: str) -> tuple[Path, str]:
    if state == "running-right":
        return ROOT / "qa/candidates/rekeyed-running/frames/running-right", "stable-slots"
    if state == "running-left":
        return ROOT / "qa/candidates/rekeyed-running/frames/running-left", "stable-slots"
    return RETAINED_BASELINE / state, "components"


def normalize_green_edge_key_to_magenta(path: Path) -> int:
    """Unify visible green-screen spill to the legacy final edge-cleanup key.

    Roxy has no green foreground. This preserves alpha and does not remove or
    soften any edge; the only actual cleanup remains the single final atlas pass.
    """
    image = Image.open(path).convert("RGBA")
    pixels = list(image.get_flattened_data())
    changed = 0
    output = []
    for red, green, blue, alpha in pixels:
        if (
            alpha > 0
            and green >= 60
            and green - max(red, blue) >= 25
            and green > red * 1.18
            and green > blue * 1.12
        ):
            floor = min(red, blue)
            output.append((green, floor, green, alpha))
            changed += 1
        else:
            output.append((red, green, blue, alpha))
    image.putdata(output)
    image.save(path)
    return changed


def main() -> None:
    rows = []
    edge_key_changes: dict[str, int] = {}
    for state, count in FRAME_COUNTS.items():
        source_dir, method = source_for(state)
        target_dir = ROOT / "frames" / state
        target_dir.mkdir(parents=True, exist_ok=True)
        outputs = []
        for index in range(count):
            source = source_dir / f"{index:02d}.png"
            target = target_dir / f"{index:02d}.png"
            if not source.is_file():
                raise SystemExit(f"missing approved frame: {source}")
            shutil.copy2(source, target)
            if state in {"running-right", "running-left"}:
                edge_key_changes[f"{state}/{index:02d}"] = normalize_green_edge_key_to_magenta(target)
            outputs.append(str(target.resolve()))
        rows.append({"state": state, "frames": outputs, "method": method})

    manifest = {
        "ok": True,
        "chroma_key": {"hex": "#00FF00", "rgb": [0, 255, 0], "threshold": 96.0},
        "final_edge_cleanup_key": {
            "hex": "#FF00FF",
            "reason": "legacy retained rows contain magenta edge spill; new green-generated running rows are hue-normalized without changing alpha so the complete atlas needs one cleanup pass only",
        },
        "running_edge_key_normalization": edge_key_changes,
        "rows": rows,
    }
    path = ROOT / "frames" / "frames-manifest.json"
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(path)


if __name__ == "__main__":
    main()
