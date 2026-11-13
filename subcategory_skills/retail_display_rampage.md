# Subcategory Production Skill: retail_display_rampage

## Overview
- **Subcategory ID**: `retail_display_rampage`
- **Niche**: Workplace Disasters / Fails
- **Visual Staging**: 1080x1920 9:16 vertical short format, LevelZero0ne ranking structure (Rank 5 -> Rank 1).
- **Audio Bed**: Pizzicato Comedy Theme (`Garden Of Magic` by soundroll, `public/audio/stems/retail_display_rampage_music_bed.mp3`) mixed at volume 0.11 so natural CCTV / ambient shelf crashes remain crisp and punchy.
- **Mastering**: Loudnorm filter (`-14.8 LUFS`, True Peak `-1.5 dBFS`).

## Benchmark 5-Clip Table

| Rank | Level | Source ID | Cause | Payoff | Reaction | Audio Cue |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **5** | Level 1 | `dlMLiwliD5U` | Stocker tests wobbling beverage shelf | Row of glass bottles cascades onto floor | Shocked worker jumps back into aisle | Glass shatter + pizzicato tension |
| **4** | Level 2 | `m1hRLg2Xjck` | Toddler curious about showcase pedestal | Heavy glass display case tips over flat | Father rushes over in disbelief | Heavy crash thud |
| **3** | Level 3 | `aC3qKL_rvoc` | Customer squats backwards near electronics | Backside clips curved screen TV domino row | $7,000 worth of flat screens topple in chain reaction | Multi-stage TV smash |
| **2** | Level 4 | `06dDKU5xPIg` | Customer pulls bottom single can from giant stack | Whole supermarket pyramid undergoes catastrophic failure | Guy holds head in sheer horror | Metal can avalanche rumble |
| **1** | Level 5 | `OF_Gs3JJ7gQ` | Shopper reaches into honey jar display tower | Multi-tier golden honey pyramid collapses across aisle | Store staff freeze in absolute amazement | Massive liquid shatter cascade |

## Workflow Steps Executed
1. **Harvesting & Sourcing**: Sourced 10+ real CCTV & viral shop display disaster clips.
2. **Visual Inspection**: 2fps contact sheets generated and examined with `read_file` to filter out severe trauma, animated cartoons, or watermarks.
3. **Clip Trimming**: Encoded 5 full-story clips with cause, apex collapse, and aftermath intact at CFR 30fps (`libx264`, `yuv420p`, `aac 192k 48kHz`).
4. **Cue Sheet Construction**: Populated `cue_sheet_retail_display_rampage.json` with exact frame offsets, punchline text, and headers.
5. **Remotion Rendering**: Rendered `output/retail_display_rampage_raw.mp4` with concurrency 6x.
6. **Loudness Mastering & QA**: Audio mastered to YouTube Shorts standard (`-14.8 LUFS`, True Peak `-1.5 dBFS`), followed by 1fps contact sheet verification confirming 0 black frames and complete story arcs.
