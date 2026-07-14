# Running-right green attempt 2 — rejected

Source: `qa/candidates/running-right-green-repair-2/source.png`

Hard failures:

- The generated background is visually green but not exact `#00FF00`; only 21 pixels are exact green. The connected background must be normalized before extraction.
- Frame 6 contains two blue ankle wraps and loses the brown leg identity.
- Frames 1/5 do not form a reliable opposite-leg pair, and frame 7 returns too early to the frame-0 wide contact silhouette instead of completing the second passing/descending phase.
- Frames 4 and 5 have no full background column between their source components; the next generation needs smaller figures and wider inter-frame gutters.

Passes retained as constraints:

- The first braid is complete and no figure touches the outer canvas.
- Whole-character scale is substantially more stable than earlier attempts; source-height CV is 1.65%.
- Frames 0 and 4 visibly exchange the blue and brown leg identities.

This candidate remains QA evidence only and must not replace `decoded/running-right.png`.
