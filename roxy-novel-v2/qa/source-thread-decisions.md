# Source customization decisions

Authoritative follow-up task: `019f5a26-60e1-7620-a562-e8ce778cf053` (`检查宠物帧率跳变`).

Confirmed user decisions preserved by V2:

- Codex runtime trigger mapping stays fixed, but row content is user-customizable.
- Row 4 / `jumping` is intentionally a five-frame mouse-hover wave, not a physical jump.
- Row 7 / `running` is intentionally a thinking/working loop: one hand at the chin, staff lightly tapping, hat brim and cloak moving subtly.
- Row 0 / `idle` is the repaired stable blink loop that removed the single wider/fatter frame.
- These three rows must not be regenerated or reverted during the V2 running-gait and look-direction repair.

Verified source-image provenance:

- hover wave: `/Users/mac/.codex/generated_images/019f5a26-60e1-7620-a562-e8ce778cf053/exec-e9a9ebc1-6a48-403a-bc7c-cf6bcec475c5.png`
- thinking loop: `/Users/mac/.codex/generated_images/019f5a26-60e1-7620-a562-e8ce778cf053/exec-987252fc-60f1-447a-ba83-1b18c5222f14.png`
- stable idle: `/Users/mac/.codex/generated_images/019f5a26-60e1-7620-a562-e8ce778cf053/exec-9c400be1-003c-4b70-a033-267fc0827326.png`

The three generated-source SHA-256 values match the corresponding current V2 `decoded/jumping.png`, `decoded/running.png`, and `decoded/idle.png` files.
