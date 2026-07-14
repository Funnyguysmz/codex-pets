# Running-right attempt 1

Result: rejected before decode/assembly.

Five generated candidates were reviewed by the isolated row worker. Four contained eight right-facing poses with mostly stable scale, but all four failed the same hard gait gate: they did not show unmistakable opposite foot contacts and opposite passing-leg phases. One candidate also clipped the final staff. The fifth output was a mannequin-style pose guide rather than a deliverable Roxy row.

Root condition changed for the next attempt: stop asking one prompt to invent all eight phases from prose. Generate four explicit anatomical gait anchors first, then provide those anchors as mandatory pose-family evidence for a new coherent eight-frame row.

The four-pose anchor strategy was also rejected after two bounded attempts: both repeated the same screen-side leg instead of swapping contact and passing phases. Strategy changed again instead of prompt-tuning: preserve the valid eight-phase mannequin pose guide from the first worker as a pose-only reference, and require one-to-one pose transfer into a newly generated complete Roxy row.

Whole-strip pose transfer and a three-quarter-view row were then rejected: both still erased the second-half leg-role swap. Final bounded strategy: create four single-pose Roxy gait anchors as references only, then synthesize one complete coherent eight-frame row from those four role-explicit anchors. None of the single anchors is eligible for direct atlas insertion.
