# Roxy V2 look mechanics

Roxy is a compact humanoid mage. Her feet and lower torso remain registered to the same baseline. The eyes lead each gaze change, followed by a restrained head and neck turn; the shoulders and upper cloak follow slightly. The skull, facial proportions, braids, hat, hands, and staff must not be raster-warped. All 16 poses use one shared body scale: match the approved idle stature, head size, shoulder width, skirt length, boot size, and staff length. Row 10 may not be independently shrunk or fitted.

- `000 up`: pupils and eyelids aim upward; chin lifts slightly; more underside of the hat brim is visible; shoulders remain frontal. The staff stays planted and attached to the same hand.
- `090 screen-right`: pupils, nose, face, and head turn unmistakably toward screen-right; the screen-left cheek becomes more visible and the screen-right cheek recedes. The near braid shifts slightly outward while the far braid is partly occluded. The staff remains held and may lag subtly.
- `180 down`: pupils and eyelids aim downward; chin lowers; the hat brim overlaps more of the forehead and upper face; shoulders remain stable.
- `270 screen-left`: pupils, nose, face, and head turn unmistakably toward screen-left; the screen-right cheek becomes more visible and the screen-left cheek recedes. The near braid shifts slightly outward while the far braid is partly occluded. The staff remains held and may lag subtly.

Every 22.5-degree step uses an even motion budget: eye displacement first, then a small head turn or pitch, then minimal shoulder, braid, cloak, and hat follow-through. The staff stays continuously connected to the hand and does not jump sides. `337.5` must be one smooth step before `000`, and `157.5` must be one smooth step before `180`.

Screen axes are literal viewer/image coordinates. For every right-half pose (`022.5` through `157.5`), the visible pupils, nose tip, face plane, and head turn must retain a readable screen-right component. In particular `112.5`, `135`, and `157.5` may not drift to screen-left. For every left-half pose (`202.5` through `337.5`), those landmarks must retain a readable screen-left component; `202.5`, `225`, and `247.5` may not drift right. `292.5` must read simultaneously up and left through eyes plus head pitch/turn.

Registration targets after deterministic normalization: grounded height should remain within the same 195–198 px family, baseline at 201–202 px, no adjacent visible area jump above 6%, no adjacent height jump above 3%, and no center jump above 3 px. The cross-row boundaries `157.5 -> 180` and `337.5 -> 000` are hard gates, not exceptions.
