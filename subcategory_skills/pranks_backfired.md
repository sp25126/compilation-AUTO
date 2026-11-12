---
sub_category_id: pranks_backfired
sub_category_name: Pranks Gone Wrong
niche: instant_karma
references:
  - "@MrPurifiedWater"
  - "@cliportey"
audio_track: public/audio/stems/pranks_backfired_music_bed.mp3
audio_source: "FUNK UNIVERSO (Instrumental - Slowed, _PVrKT-Gp7A, 1.14M+ views)"
audio_bg_volume: 0.11
compositor: src/remotion/MrPurifiedWaterShort.tsx
cue_sheet: cue_sheet_pranks_backfired.json
---

# Sub-Category Skill: `pranks_backfired` ("Pranks Gone Wrong")

> **MANDATORY FOR AI PIPELINE:** Every rule in this file was verified through live YouTube trend research, multi-platform sourcing, 2fps visual inspection, story-preserving trimming, Remotion compositing, EBU R128 mastering (`-14.1 LUFS`, LRA `9.1 LU`, True Peak `-1.8 dBFS`), and 1fps final QA.

---

## 1. Core Production Rules
1. **Header & Composition Props (`RankingShort`):**
   - `titleHeader`: `"Ranking Best Of"`
   - `subjectHeader`: `"Pranks Gone Wrong"`
   - `versionTag`: `"(Wrong Target Edition)"`
   - `globalAudioPath`: `"public/audio/stems/pranks_backfired_music_bed.mp3"`
2. **Escalating Karma Intensity Ladder:**
   - Rank 5 (Level 1) starts with lighthearted self-inflicted classroom karma and escalates to Rank 1 (Level 5) where a mall prankster gets dropped by a clean front kick.
   - Kinetic `punchlineText` triggers at `impactFrameOffset` right as the karma lands, without obscuring the subject or action.
3. **Never Interrupt the Action:**
   - Zero white impact flashes, zero text banners over the action, and zero premature cuts. Every clip preserves **100% of Cause (Prank Attempt) -> Payoff (Backfire / Retaliation) -> Reaction (Shock / Aftermath)**.
4. **Unique Category-Matched Audio Bed & Natural Foley:**
   - Uses **FUNK UNIVERSO (Instrumental - Slowed)** (`public/audio/stems/pranks_backfired_music_bed.mp3`, 48.0s bed with 1.0s fade-in & 2.0s fade-out) mixed at `volume: 0.11` under `1.0` natural clip audio.
   - Mastered via `loudnorm=I=-14:TP=-2.0:LRA=11` (verified `-14.1 LUFS`, LRA `9.1 LU`, True Peak `-1.8 dBFS`).

---

## 2. Multi-Platform Sourcing & Rejection Log
- **Reddit (`agent-reach reddit search` + `v.redd.it` HLS):**
  - `"instantkarma prank backfired v.redd.it"`
  - `"whatcouldgowrong prank gone wrong v.redd.it"`
  - `"justiceserved prankster v.redd.it"`
  - `"prank backfires instant karma v.redd.it"`
- **YouTube Shorts (`yt-dlp --js-runtimes node --flat-playlist --dump-json`):**
  - `"prankster gets instant karma shorts"`
  - `"pranks gone wrong instant regret shorts"`
  - `"messing with the wrong person prank shorts"`
  - `"scare prank gone wrong #shorts"`
- **Rejected Candidates (2fps Visual QA Gate):**
  - `r_do65kivatjs91`: TikTok `@` watermark overlay.
  - `r_8ml3srh2d6r41`: Baked-in English subtitle text across the bottom.
  - `r_ckglohk2jy331`: No audio stream (`audio=`) and low resolution (`400x224`).
  - `r_3yh5pof4ih471`: Low resolution (`264x320`) compilation.
  - `yt_TuVOv1EGayM`: Baked-in yellow title text (`"Disruptive Student in College Class"`).
  - `yt_FtdcQt4qCIg`: Duplicate of `r_lufbb43pbwhf1` at lower resolution (`400x226` vs `848x480`).

---

## 3. Verified 5-Clip Benchmark Table (Rank 5 -> Rank 1)

| Rank | Level | Source ID | Story (Cause -> Payoff -> Reaction) | Trim (`ss` / `t`) | Speed | Out Duration / Frames | `impactFrameOffset` | Punchline Text | Output File |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **5** | Level 1 | `reddit:yifcxo63psn31` | Girl in classroom tries to pull/kick classmate's chair -> her own desk chair flips backward onto floor -> classmates react | `0.0s` / `7.89s` | `1.00x` | `7.90s` (`230f`) | `150` | `INSTANT KARMA` | `public/clips/pranks_backfired/rank_5.mp4` |
| **4** | Level 2 | `reddit:5wj1tdy3uwh61` | Coworker lies in hallway to scare colleague -> she opens door, panics & hurls phone onto his head -> he curls up, she checks on him | `5.5s` / `8.5s` | `1.10x` | `7.80s` (`234f`) | `85` | `WRONG TARGET` | `public/clips/pranks_backfired/rank_4.mp4` |
| **3** | Level 3 | `reddit:n0lci1loz8451` | Prankster sprays stranger in store with water bottle -> stranger calmly grabs him & marches him out | `0.0s` / `10.5s` | `1.20x` | `8.77s` (`263f`) | `65` | `HUMBLED QUICK` | `public/clips/pranks_backfired/rank_3.mp4` |
| **2** | Level 4 | `reddit:lufbb43pbwhf1` | Prankster blasts airhorn in stranger's ear on street -> stranger doesn't flinch & delivers thunderous slap -> prankster holds face in shock | `11.0s` / `10.5s` | `1.25x` | `8.43s` (`253f`) | `45` | `ZERO MERCY` | `public/clips/pranks_backfired/rank_2.mp4` |
| **1** | Level 5 | `reddit:euna78lghrx71` | Prankster sprints at stranger in busy mall -> stranger casually lands a clean front kick dropping him flat -> bystanders step in | `2.0s` / `10.0s` | `1.15x` | `8.73s` (`262f`) | `110` | `FINAL BOSS` | `public/clips/pranks_backfired/rank_1.mp4` |

---

## 4. Render, Mastering & Final QA Commands
1. **Remotion Render:**
   `npx remotion render RankingShort output/pranks_backfired_raw.mp4 --props=cue_sheet_pranks_backfired.json --timeout=90000 --concurrency=2 --overwrite` (1317 frames / 43.90s @ 30fps).
2. **EBU R128 Audio Master:**
   `ffmpeg -y -v error -i output/pranks_backfired_raw.mp4 -af "loudnorm=I=-14:TP=-2.0:LRA=11" -c:v copy -c:a aac -b:a 320k output/pranks_backfired_mastered.mp4`
3. **1fps Final QA Contact Sheet:**
   `ffmpeg -y -v error -i output/pranks_backfired_mastered.mp4 -vf "fps=1,scale=260:-1,tile=7x7" -frames:v 1 -q:v 3 output/pranks_backfired_qa_sheet.jpg`
4. **Mandatory Owner Disclaimer:**
   `"All footages used in this video are not mine; full credit goes to the respective owners."`
