---
sub_category_id: bench_press_ego_fails
sub_category_name: BENCH PRESS EGO FAILS
niche: gym_bloopers
references:
  - "@cliportey"
  - "@MrPurifiedWater"
audio_stem: public/audio/stems/bench_press_ego_fails_music_bed.mp3
audio_stem_bpm: 128
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
- **Buildup (`0` to `T_cause`, natural audio):** Raw ambient room/environment sound builds authenticity without voiceover clutter.
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
  ffmpeg -y -i raw_input.mp4 -vf "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -pix_fmt yuv420p -r 30 -g 15 -keyint_min 15 -sc_threshold 0 -c:a aac -ar 48000 -b:a 320k normalized_clip.mp4
  ```

---

## 4. Audio Stem & Music Bed Design
- **Track Genre:** Heavy Phonk / Bass Drop Groove
- **Stem File:** `public/audio/stems/bench_press_ego_fails_music_bed.mp3`
- **Volume Mixing:** `0.11` volume bed in Remotion props so natural sound effects and reactions cut through cleanly.
- **Fade Dynamics:** `0.5s` linear fade-in, `1.5s` fade-out into the sonic outro.

---

## 5. 5-Rank Benchmark Breakdown Table

| Rank | Level | Story Arc | Climax Action | Payoff / Reaction |
| :---: | :---: | :--- | :--- | :--- |
| **5** | Level 1 | **The Missing Clips Slide** | Lifter puts 3 plates on each side with no barbell collars. | Lifter tilts 5 degrees left; all plates slide off sequentially with loud clatter. |
| **4** | Level 2 | **The Half-Inch Bounce Rep** | Guy loads 315lbs, unrolls wrist wraps, screams at mirror. | Lowers bar 2 inches, bounces violently off sternum, gets stuck halfway up. |
| **3** | Level 3 | **The Feet-In-Air Wobble** | Lifter puts both feet up on the bench pad while lifting heavy. | Loses balance completely, rolls sideways off the bench onto the rubber floor. |
| **2** | Level 4 | **The Silent Bar of Shame Roll** | Solo lifter gets pinned under 275lbs with nobody in the gym. | Has to awkwardly roll the heavy barbell down ribs to hips and sit up gasping. |
| **1** | Level 5 | **The Pretend Warmup Attempt** | Guy walks in wearing jeans, loads 405lbs to impress girls nearby. | Unracks the bar; gravity immediately drops it flat to chest, spotters rush in panic. |

---

## 6. QA Verification Gate
- [ ] 0 black frames detected in 1fps contact sheet.
- [ ] 0 third-party watermarks or channel repost logos.
- [ ] Integrated Loudness: `-14.0 ± 1.0 LUFS`.
- [ ] True Peak: `<= -1.5 dBTP`.
- [ ] Contact sheet: `output/bench_press_ego_fails_qa_sheet.jpg` verified.

---

## 7. YouTube Shorts SEO & Upload Package
- **Hook Title:** `Ranking Worst Bench Press Ego Fails 💀🏋️ #shorts #gymfails #gym`
- **Description:**
  ```text
Ranking the most ridiculous gym ego lifts that ended in total embarrassment! Always use safety clips and a spotter! 🏋️💥

All footages used in this video are not mine; full credit goes to the respective owners.

#shorts #viral #gym #gymfails #benchpress #egolifting #workout #fitnessfails
  ```
- **Optimal Upload Window:** 19:00 – 21:30 IST / 09:30 – 12:00 EST.
