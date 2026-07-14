Create one horizontal look-direction strip for Codex pet `roxy-novel-v2`, atlas row 9.

Use the attached canonical base, completed standard contact sheet, layout guide, and approved four-cardinal strip for identity, scale, registration, spacing, direction semantics, and cross-row continuity. Read `qa/look-mechanics.md` and follow its pet-specific movement and eye/prop mechanics. The approved cardinal strip is authoritative for the up, screen-right, down, and screen-left pose families. Interpolate the intermediate directions as even 22.5-degree steps between those anchors.

COHERENT SYNTHESIS LOCK: produce one unified eight-pose row. Do not paste, tile, or independently restyle individual cells. Every final cell must be drawn together with the same face construction, body proportions, line/render quality, lighting, materials, scale, baseline, and registration.

Output exactly 8 complete full-body frames in this exact left-to-right order: 000, 022.5, 045, 067.5, 090, 112.5, 135, 157.5. Degrees are clockwise: 000 is up, 090 right, 180 down, and 270 left. Neutral/front is not part of this row.

DIRECTION TARGETS — these are hard visible screen-coordinate gates at normal pet size:

1. `000`: vertical UP; no horizontal requirement.
2. `022.5`: horizontal SCREEN-RIGHT and vertical UP.
3. `045`: horizontal SCREEN-RIGHT and vertical UP.
4. `067.5`: horizontal SCREEN-RIGHT and vertical UP.
5. `090`: horizontal SCREEN-RIGHT; no vertical requirement.
6. `112.5`: horizontal SCREEN-RIGHT and vertical DOWN.
7. `135`: horizontal SCREEN-RIGHT and vertical DOWN.
8. `157.5`: horizontal SCREEN-RIGHT and vertical DOWN.

Cardinals and every intermediate quadrant must be unmistakable. Preserve identity without weakening direction evidence: use the pupils, eyelids, nose tip, face plane, head turn, and restrained neck/shoulder follow-through together.

SCREEN-COORDINATE LOCK: screen-right means the viewer's right image edge, never the character's own right. For frames 022.5 through 157.5, the pupils and nose tip must stay visibly on the screen-right side of the head center while the face plane turns right. `112.5`, `135`, and `157.5` are critical repair frames: all three must remain down-right and must not read down-left. Near-vertical cues may be restrained but cannot become ambiguous or reverse.

HARD LAYOUT AND CONTINUITY CONTRACT — DETERMINISTIC REGISTRATION: draw exactly eight separated pose groups in left-to-right direction order. Keep enough chroma-only space between neighboring poses that each complete pose can be detected without cutting through foreground. Approximate the guide's equal spacing, but do not distort a pose merely to hit an exact source-canvas coordinate; deterministic assembly will crop the eight ordered groups, then apply one shared scale and baseline.

Use the same body height, head size, hat size, shoulder width, skirt length, boot size, staff length, baseline, and planted-body position across the generated family. The visible body volume must not progressively shrink from 000 to 157.5. Never overlap neighboring poses, merge two poses into one connected group, crop foreground at the outer canvas edge, or resize one pose independently.

Keep the feet, base, or lower torso planted at the same coordinates across all eight frames. Express direction through the eyes, face, head, upper body, and physically appropriate prop movement, not by moving, rotating, or rescaling the entire sprite.

Place one centered pose in each invisible equal-width slot on flat pure green #00FF00. Change only the natural parts needed to express gaze: eyes, eyelids, head, face, neck, upper body, appendages, and constrained prop follow-through. Keep identity, silhouette, materials, palette, markings, and props consistent. Keep green and green spill completely out of the pet and all silhouette edges.

ROW-BOUNDARY LOCK: 157.5 must be one even down-right step before 180. Match the approved 180 pose's body size, baseline, planted anchor, expression, and construction while retaining an unmistakable screen-right eye/face component. This boundary must not change height, head size, body volume, or staff registration.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped; any frame changes sprite scale, body/head/hat size, baseline, or planted-body position; any right-half frame reads left; or 157.5 does not flow evenly into 180. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement/googly eyes, labels, degree text, arrows, clocks, grids, shadows, glows, scenery, detached effects, or chroma-key colors inside the pet.
