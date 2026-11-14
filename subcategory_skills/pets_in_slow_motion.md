# Subcategory Skill: Pets In Slow Motion (`pets_in_slow_motion`)

## Overview & Style
Subcategory `pets_in_slow_motion` (funny_animals niche) captures high-framerate, dramatic slow-motion pet bloopers, hilarious fails, and expressive physical comedy. Pacing escalates from graceful athletic attempts to chaotic whiffs, structural slips, aerodynamic face shakes, and the ultimate food smackdown.

## Audio Design
- **Custom Soundtrack**: Unique slow-motion comedy classical/epic bed (`public/audio/stems/pets_in_slow_motion_music_bed.mp3`) at `musicVolume: 0.11`.
- **Clip Audio Fidelity**: Preserves full natural audio, breathing, paw landings, jaw snaps, and reactions without clipping.
- **Broadcast Loudness**: EBU R128 loudness master at `-13.7 LUFS`, True Peak `-1.5 dBFS`, LRA `3.3 LU`.

## Benchmark 5-Clip Roster

| Rank | Level | Source ID | Cause | Payoff | Reaction | Duration |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Rank 5** | Level 1 | `reddit_s8tw8enxhz281` | Golden retriever locks onto incoming tennis ball | Launches 5 feet into the air in vertical slow-motion | Catches ball cleanly in jaws and paws at apex | 7.0s |
| **Rank 4** | Level 2 | `SnRo-k7M1TA` | Black lab focuses intently on flying treat in studio | Jaws snap with tremendous effort, treat sails over head | Flopping ears, confused tongue lick, looks at camera | 7.0s |
| **Rank 3** | Level 3 | `r_me4s94xw4fn41` | Cat miscalculates leap to slippery glass stair railing | Front paws catch top edge, hind legs scramble on glass | Slowly slides down glass pane in pure comedy defeat | 7.0s |
| **Rank 2** | Level 4 | `39RYrucTvGo` | Wet Basset Hound braces on grass after bath | 1000 FPS head shake creates orbiting water droplet vortex | Jowls flip completely inside out, ears spin like helicopters | 7.5s |
| **Rank 1** | Level 5 | `6w2UxDdhZPk` | Golden Retriever Fritz opens mouth wide for snack | Glazed donut drops from above and smacks squarely on snoot | Donut bounces down chest as Fritz stares in total disbelief | 7.5s |

## Production Pipeline
1. **Multi-Platform Sourcing**: Harvested candidates across Reddit (`v.redd.it`) and high-resolution YouTube Shorts/clips.
2. **2fps Contact Sheet QA**: Inspected all candidate sheets with `read_file`; rejected watermarked, cropped, AI-generated, and low-res footage.
3. **Full-Story Trimming**: Cut 5 distinct verified clips preserving full Cause -> Payoff -> Reaction, normalized to CFR 30fps, 48kHz stereo AAC.
4. **Remotion Render**: Rendered `RankingShort` with custom cue sheet props (`titleHeader: "Ranking Funniest"`, `subjectHeader: "Pets In Slow Motion"`, `versionTag: "(Dramatic Fails)"`).
5. **Two-Pass Audio Mastering**: Mastered audio with `loudnorm` (`I=-14:TP=-1.8:LRA=11:linear=true`) achieving `-13.7 LUFS` and `-1.5 dBFS` True Peak.
6. **1fps Visual QA Sheet**: Verified 0 black frames, complete stories, and clean visual overlays.
