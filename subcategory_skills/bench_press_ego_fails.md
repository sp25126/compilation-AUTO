---
sub_category_id: bench_press_ego_fails
sub_category_name: BENCH PRESS EGO FAILS
niche: gym_bloopers
references:
  - "@cliportey"
  - "@MrPurifiedWater"
audio_stem: public/audio/stems/bench_press_ego_fails_music_bed.mp3
audio_stem_bpm: 130
audio_stem_volume: 0.11
compositor: src/remotion/MrPurifiedWaterShort.tsx
anti_stutter_codec: OffthreadVideo
keyframe_interval_gop: 15
frame_rate: 30.0_cfr
---

# Sub-Category Skill: `bench_press_ego_fails` ("BENCH PRESS EGO FAILS")

> **MANDATORY FOR AI PIPELINE:** Subtitles are strictly disabled (`showSubtitles: false`). Every clip must follow the 3-beat causal arc: Buildup ➔ Climax ➔ Payoff/Reaction. Stuttering is permanently prevented via Remotion `<OffthreadVideo>` and dense `-g 15` CFR 30fps encoding.

---

## 1. Core Narrative & Edit Philosophy
A **"BENCH PRESS EGO FAILS"** compilation hooks viewers with visceral retention psychology:
- **Buildup (`0` to `T_cause`, natural audio):** Raw ambient gym and barbell clinking audio builds authenticity without voiceover clutter.
- **The Climax (`T_cause`):** Lifter loads absurd weight without warmup or spotter -> Unracks with shaking elbows -> Bar pins chest -> Forced to roll the bar of shame or tilt plates off.
- **The Payoff / Reaction (`T_payoff`):** Clean emotional resolution (laughter, shock, relief, celebration).

---

## 2. Reference Architecture
- **Canvas:** `1080x1920` (9:16 vertical), `30 fps` constant frame rate.
- **Top 240px Header Banner:**
  - Line 1: `Ranking Best Of` (`Of` in `#FFEB3B`)
  - Line 2: `BENCH PRESS EGO FAILS` (`#FF2D55`)
  - Line 3: `(Bar Of Shame Edition)` (`#00D2FF`)
- **Color Progression Ladder:**
  - Rank 5 [Level 1]: `#FF2D55`
  - Rank 4 [Level 2]: `#00D2FF`
  - Rank 3 [Level 3]: `#FFEB3B`
  - Rank 2 [Level 4]: `#FFFFFF`
  - Rank 1 [Level 5]: `#FFFFFF` (Climax Finale)
- **Subtitles:** Strictly disabled (`showSubtitles: false`).
- **Watermark & Outro:** Circular `LevelZero0ne` watermark + 75-frame Earshot sonic brand outro (`public/audio/earshot_sonic_brand.mp3`).

---

## 3. Anti-Stuttering Pipeline Protocol
- **Compositor Engine:** Remotion `<OffthreadVideo>` in `src/remotion/MrPurifiedWaterShort.tsx`.
- **Pre-Processing Command:** Strict 30fps CFR re-encode with dense `-g 15` keyframe interval:
  ```bash
  ffmpeg -y -i raw_input.mp4 -vf "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -pix_fmt yuv420p -r 30 -g 15 -keyint_min 15 -sc_threshold 0 -c:a aac -ar 48000 -b:a 192k normalized_clip.mp4
  ```

---

## 4. Audio Stem & Music Bed Design
- **Track Genre:** Dark Gym Phonk / Aggressive Drift Bass Beat
- **Stem File:** `public/audio/stems/bench_press_ego_fails_music_bed.mp3`
- **Volume Mixing:** `0.11` volume bed in Remotion props so natural sound effects and reactions cut through cleanly.
- **Fade Dynamics:** `0.5s` linear fade-in, `1.5s` fade-out into the sonic outro.

---

## 5. 5-Rank Benchmark Breakdown Table

| Rank | Level | Story Arc | Cause / Buildup | Climax Action | Payoff / Reaction | Duration |
| :---: | :---: | :--- | :--- | :--- | :--- | :---: |
| **5** | Level 1 | **The 405lbs Missing Clips Dump** | Lifter attempts massive 405lb bench without barbell safety collars. | Stalls flat on chest, tilts left, all heavy plates slide off with thunderous clatter. | Barbell catapults upright with lifter sitting up in complete shock. | 7.43s (223f) |
| **4** | Level 2 | **The Solo 130kg PR Pin & Bail** | Solo 18yo lifter attempts 130kg PR with zero spotter or safeties. | Elbows flare violently, bar stalls and drops flat to chest pinning ribs. | Kicks legs in panic and rolls the heavy barbell down to bail onto the rubber floor. | 8.20s (246f) |
| **3** | Level 3 | **The Safety Bar Breakaway Dump** | Lifter loads massive yellow Eleiko bumper plates. | Safety bar gives way under load; barbell crashes violently down to the gym floor. | Lifter rolls free onto the rubber floor clutching his jaw in utter disbelief. | 8.57s (257f) |
| **2** | Level 4 | **The Textbook 355lb Roll of Shame** | Lifter fails halfway up on a heavy 355lb bench attempt alone. | Under control, slowly executes textbook roll of shame down chest, ribs, and abs. | Sits upright with the massive bar resting in his lap and smiles in huge relief. | 8.03s (241f) |
| **1** | Level 5 | **The 8-Plate Warmup Panic Heave** | Lifter in khakis attempts absurd 8-plate monster barbell to impress gym. | Bar drops immediately upon unrack, pinning sternum in catastrophic stall. | Three spotters panic-heave bar up to rack as lifter covers his head in disbelief. | 8.20s (246f) |

---

## 6. QA Verification Gate
- [x] 0 black frames detected in 1fps contact sheet.
- [x] 0 third-party watermarks or channel repost logos.
- [x] Integrated Loudness: `-14.0 ± 1.0 LUFS`.
- [x] True Peak: `<= -1.5 dBTP`.
- [x] Contact sheet: `output/bench_press_ego_fails_qa_sheet.jpg` verified.

---

## 7. YouTube Shorts SEO & Upload Package
- **Hook Title:** `Ranking Worst Bench Press Ego Fails 💀🏋️ #shorts #gymfails #gym`
- **Description:**
  ```text
  Ranking the most embarrassing bench press ego lifting fails where lifters loaded way too much weight and suffered the instant bar of shame! 🏋️‍♂️💥 Always use safety clips and a trusted spotter!

  All footages used in this video are not mine; full credit goes to the respective owners.

  #shorts #viral #gym #gymfails #benchpress #egolifting #workout #fitnessfails #gymhumor #barofshame
  ```
- **Optimal Upload Window:** 20:30 IST / 11:00 AM EST.
