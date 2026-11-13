---
sub_category_id: accidental_trickshots
sub_category_name: ACCIDENTAL TRICKSHOTS
niche: extreme_luck
references:
  - "@cliportey"
  - "@MrPurifiedWater"
audio_stem: public/audio/stems/accidental_trickshots_music_bed.mp3
audio_stem_bpm: 130
audio_stem_volume: 0.11
compositor: src/remotion/MrPurifiedWaterShort.tsx
anti_stutter_codec: OffthreadVideo
keyframe_interval_gop: 15
frame_rate: 30.0_cfr
---

# Sub-Category Skill: `accidental_trickshots` ("ACCIDENTAL TRICKSHOTS")

> **MANDATORY FOR AI PIPELINE:** Subtitles are strictly disabled (`showSubtitles: false`). Every clip must follow the 3-beat causal arc: Buildup ➔ Climax ➔ Payoff/Reaction. Stuttering is permanently prevented via Remotion `<OffthreadVideo>` and dense `-g 15` CFR 30fps encoding.

---

## 1. Core Narrative & Edit Philosophy
A **"ACCIDENTAL TRICKSHOTS"** compilation hooks viewers with visceral retention psychology:
- **Buildup (`0` to `T_cause`, natural audio):** Raw ambient room/environment sound builds authenticity without voiceover clutter.
- **The Climax (`T_cause`):** Subject drops or tosses an object carelessly -> Object takes multiple improbable bounces off furniture/walls -> Lands perfectly in target with zero intentional effort.
- **The Payoff / Reaction (`T_payoff`):** Clean emotional resolution (laughter, shock, relief, celebration).

---

## 2. Reference Architecture
- **Canvas:** `1080x1920` (9:16 vertical), `30 fps` constant frame rate.
- **Top 240px Header Banner:**
  - Line 1: `Ranking Best Of` (`Of` in `#FFEB3B`)
  - Line 2: `ACCIDENTAL TRICKSHOTS` (`#FF2D55`)
  - Line 3: `(Zero Skill Pure Luck)` (`#00D2FF`)
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
- **Track Genre:** High-Energy Upbeat Phonk / Electronic Beat
- **Stem File:** `public/audio/stems/accidental_trickshots_music_bed.mp3`
- **Volume Mixing:** `0.11` volume bed in Remotion props so natural sound effects and reactions cut through cleanly.
- **Fade Dynamics:** `0.5s` linear fade-in, `1.5s` fade-out into the sonic outro.

---

## 5. 5-Rank Benchmark Breakdown Table

| Rank | Level | Story Arc | Climax Action | Payoff / Reaction |
| :---: | :---: | :--- | :--- | :--- |
| **5** | Level 1 | **Desk Pen Kick Into Holder** | Student drops pen off desk, reflex-kicks it with shoe. | Pen arcs 10 feet across classroom and drops tip-down straight into teacher's pen cup. |
| **4** | Level 2 | **Kitchen Spatula Fumble** | Cook flips burger and loses grip on spatula. | Spatula flips 3 times in air, bounces off frying pan handle, lands standing upright on counter rack. |
| **3** | Level 3 | **Basketball Full-Court Backward Toss** | Gym teacher tosses ball backward over shoulder while cleaning up. | Ball flies 94 feet across court, hits backboard, swishes through net clean. |
| **2** | Level 4 | **Golf Ball Pool Bounce Hole-in-One** | Golfer hits severe slice into backyard swimming pool. | Ball skips across pool surface twice, ricochets off patio umbrella pole, rolls into cup on green. |
| **1** | Level 5 | **Ping Pong Triple Ricochet Cup Swish** | Player hits wild smash off table; opponent dodges in panic. | Ball bounces off camera tripod, off ceiling light fixture, off water bottle, and lands inside red solo cup across the room. |

---

## 6. QA Verification Gate
- [ ] 0 black frames detected in 1fps contact sheet.
- [ ] 0 third-party watermarks or channel repost logos.
- [ ] Integrated Loudness: `-14.0 ± 1.0 LUFS`.
- [ ] True Peak: `<= -1.5 dBTP`.
- [ ] Contact sheet: `output/accidental_trickshots_qa_sheet.jpg` verified.

---

## 7. YouTube Shorts SEO & Upload Package
- **Hook Title:** `Ranking Accidental Trickshots That Defied Physics 🤯🎱 #shorts #viral #amazing`
- **Description:**
  ```text
Ranking the luckiest accidental trickshots in history! That 1 in a billion bounce at Level 5 is impossible! 🎱💥

All footages used in this video are not mine; full credit goes to the respective owners.

#shorts #viral #trickshot #luck #physics #impossible #clutch #satisfying #sports
  ```
- **Optimal Upload Window:** 19:00 – 21:30 IST / 09:30 – 12:00 EST.
