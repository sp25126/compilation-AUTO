# Subcategory Skill: Animals Becoming Scarier (`animals_becoming_scarier`)

## Overview & Style
Subcategory `animals_becoming_scarier` is engineered for high-retention viral ranking short-form video in the funny animals / boss fight pets niche. It tracks escalating levels of normally harmless, cute, or calm pets suddenly activating unearthly, ferocious, or intimidating "boss fight" modes without staged setups, harm to animals, or cringe overlays.

## Audio Design
- **Custom Soundscape**: Dedicated comedy suspense/boss battle music bed (`public/audio/stems/animals_becoming_scarier_music_bed.mp3`) mixed at `musicVolume: 0.11` to preserve 100% natural clip dialogue, growls, squeaks, and cackles.
- **Clip Audio Fidelity**: Preserves full live foley including desert rain frog high-pitched squeaks, crab cat movements, parrot supervillain laughs, and Mr. Bubz's unearthly rumbling demonic snarl.
- **Mastering Compliance**: YouTube Shorts broadcast target of -14 LUFS (Achieved: -14.1 LUFS, True Peak: -1.5 dBTP).

## Benchmark 5-Clip Roster

| Rank | Level | Source ID | Cause | Payoff | Reaction | Duration |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Rank 5** | Level 1 | `cBkWhkAZ9ds` | Tiny round desert rain frog resting peacefully on dune sand | Puffs up into an angry dumpling and releases ferocious high-pitched battle squeaks | Stands on tip-toes challenging the viewer | 7.0s |
| **Rank 4** | Level 2 | `Dfx55uI4tYE` | Relaxed tuxedo cat lounging peacefully on granite kitchen island | Suddenly arches spine into extreme goblin curve with puffy tail | Sideways power-walks stiff-legged across the entire counter before hopping off | 7.2s |
| **Rank 3** | Level 3 | `GVlfzt0J894` | Large grey owl sitting quietly on tree branch facing away | Instantly snaps neck 180 degrees directly towards the camera lens | Locks into unblinking, glowing predator death stare and tilts head menacingly | 7.5s |
| **Rank 2** | Level 4 | `YE8PTMSFMUg` | Green parrot peeking from behind dark doorway in pink hallway | Stalks deliberately into the center of the living room with slow menacing paces | Stops, throws head back, and unleashes a chilling movie supervillain cackle | 7.5s |
| **Rank 1** | Level 5 | `xYa4N6Mb87k` | Owner holds cute lap dog affectionately: "I love you Mr. Bubz" | Eyes bulge out with demonic rage as low rumbling growl builds up | Cameraman says "I got this on camera!" and Bubz snaps straight to lens with demon hiss | 8.2s |

## Production Pipeline
1. **Source Discovery**: High-view YouTube Shorts and Reddit animal communities (`/r/Bossfight`, `/r/crabcats`, `/r/hitmanimals`, `/r/StartledCats`), filtering for genuine high-resolution footage without gaming UI or watermarks.
2. **2fps Frame Inspection**: All candidate contact sheets verified with `read_file` to filter out baked-in watermarks, text overlays, and truncated actions.
3. **Clip Normalization**: CFR 30fps x264, 48kHz AAC, crisp native audio retention, speed-adjusted where appropriate (`setpts`/`atempo`).
4. **Remotion Render**: Full LevelZero0ne hybrid ranking overlay, dynamic level badge progression, punchline text popups.
5. **Two-Pass Loudnorm**: Mastered to `-14.1 LUFS` with `-1.5 dBTP`.
6. **1fps QA Audit**: Verified 0 black frames and clean full-bleed storytelling across 1,196 frames.
