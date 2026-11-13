# Subcategory Skill: Gymnast Routine Mishaps (`gymnast_routine_mishaps`)

## Overview
- **Category:** Sports Bloopers / Physical Comedy
- **Target Audience:** Viral YouTube Shorts, TikTok, Instagram Reels
- **Tone:** Lighthearted physical comedy, zero severe injury, authentic reactions and soft landings onto mats/snow.

## Sourcing & QA Workflow
1. **Multi-Platform Search:** Sourced candidate clips across YouTube Shorts and Reddit (`r/Gymnastics`, `r/GymFails`).
2. **2fps Visual QA:** Inspected candidate contact sheets. Filtered out blurry camera-shakes, competitive TV channel overlays, severe injury footage, and meme text banners.
3. **Pacing & Trimming:** Standardized to CFR 30fps, 48000Hz AAC audio, preserving the complete "Cause ➔ Payoff ➔ Soft Mat Impact" narrative arc.
4. **Audio Architecture:**
   - Unique Upbeat Funk & Comedy Music Bed: `public/audio/stems/gymnast_routine_mishaps_music_bed.mp3`
   - Ducked background music volume (`0.11`) to preserve gym mats impacts, bar springs, and authentic crowd reactions.
   - Mastered with FFmpeg EBU R128 (`loudnorm=I=-14:TP=-1.5:LRA=11`).

## 5-Clip Benchmark Table

| Rank | Level | Source File | Event / Mishap Type | Duration | Narrative Arc & Payoff |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Rank 5** | Level 1 | `oDWlEzckI0s.mp4` | Uneven Bar Jump | 5.52s | High bar leap overshoots slightly, landing harmlessly in soft foam pit. |
| **Rank 4** | Level 2 | `SZol8S-_aTQ.mp4` | Vault Table Slip | 6.17s | Fast sprint and handspring bounce turns into a belly slide along the safety mat. |
| **Rank 3** | Level 3 | `MZKHTRBYL-w.mp4` | Outdoor Snow Parallel Bars | 8.26s | Winter handstand L-sit swing overbalances, rolling gently into deep snow drift. |
| **Rank 2** | Level 4 | `56H5kS38mhM.mp4` | Gymnastic Rings Snapping | 6.78s | High rings inverted handstand drill drops down safely onto padded floor when loop gives way. |
| **Rank 1** | Level 5 | `r_17ugruj22hn31.mp4` | Uneven Bars High Giant Swing | 7.50s | High velocity giant swing loses fingertip grip, launching gracefully across room onto padded mat. |

## Production Specs
- **Remotion Composition:** `RankingShort`
- **Cue Sheet:** `cue_sheet_gymnast_routine_mishaps.json`
- **Raw Master:** `output/gymnast_routine_mishaps_raw.mp4`
- **Final Mastered Short:** `output/gymnast_routine_mishaps_mastered.mp4`
- **Quality Assurance Sheet:** `output/gymnast_routine_mishaps_qa_sheet.jpg`
- **Metadata:** `output/gymnast_routine_mishaps_upload_metadata.json`
- **EBU R128 Integrated Loudness:** `-13.5 LUFS` (Target: -14 ± 1 LUFS)
- **True Peak:** `-1.5 dBFS` (Target: <= -1.5 dBTP)
- **Zero Black Frames:** Verified via 1fps QA contact sheet.
