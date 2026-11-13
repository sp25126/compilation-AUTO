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
- **Buildup (`0` to `T_cause`, natural audio):** Raw ambient room/arena sound builds authenticity without voiceover clutter.
- **The Climax (`T_cause`):** Subject carelessly tosses/strikes an object -> Improbable trajectory or multiple ricochets -> Lands or scores perfectly with zero intentional skill, pure 100% luck.
- **The Payoff / Reaction (`T_payoff`):** Clean emotional resolution (stunned silence, erupting crowd laughter, disbelieving apologies, ecstatic celebrations).

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
  ffmpeg -y -i raw_input.mp4 -vf "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -pix_fmt yuv420p -r 30 -g 15 -keyint_min 15 -sc_threshold 0 -c:a aac -ar 48000 -b:a 192k normalized_clip.mp4
  ```

---

## 4. Audio Stem & Music Bed Design
- **Track Genre:** High-Energy Upbeat Phonk / Electronic Beat
- **Stem File:** `public/audio/stems/accidental_trickshots_music_bed.mp3`
- **Volume Mixing:** `0.11` volume bed in Remotion props so natural sound effects and reactions cut through cleanly.
- **Fade Dynamics:** `0.5s` linear fade-in, `1.5s` fade-out into the sonic outro.

---

## 5. 5-Rank Benchmark Breakdown Table

| Rank | Level | Story Arc | Climax Action | Payoff / Reaction | Frames (Dur) |
| :---: | :---: | :--- | :--- | :--- | :---: |
| **5** | Level 1 | **Casual Bedroom Bottle Flip** | Careless casual water bottle toss onto carpet. | Bottle flips in mid-air and sticks the upright landing; subject freaks out running in disbelief. | 195 (6.5s) |
| **4** | Level 2 | **APF Asian 9-Ball Open Fluke** | Pro player hits break shot, cue ball ricochets off 2 rails. | Double-rail carom hits 9-ball directly into corner pocket; player and referee laugh at the 1 in 10,000 fluke. | 225 (7.5s) |
| **3** | Level 3 | **Tyler Herro Full-Court Bank Swish** | Tyler Herro launches an 80-foot outlet pass across the basketball court. | Pass hits the backboard and swishes straight through the hoop; Miami Heat bench erupts in pandemonium. | 225 (7.5s) |
| **2** | Level 4 | **PGA Sungjae Im Water Hazard Double Skip** | Golfer hits severe slice heading straight into deep lake hazard. | Ball skips twice across the water surface like a flat stone and rolls safely onto the green near the pin. | 240 (8.0s) |
| **1** | Level 5 | **Kristian Karlsson WTT Impossible Net Post Curve** | Desperation lunge in world championship table tennis rally. | Ball curves entirely around the outside of the net post and clips the table corner line; opponent freezes stunned as Karlsson apologizes in shock. | 240 (8.0s) |

---

## 6. QA Verification Gate
- [x] 0 black frames detected in 1fps contact sheet.
- [x] 0 third-party watermarks or channel repost logos.
- [x] Integrated Loudness: `-14.0 ± 1.0 LUFS`.
- [x] True Peak: `<= -1.5 dBTP`.
- [x] Contact sheet: `output/accidental_trickshots_qa_sheet.jpg` verified.

---

## 7. YouTube Shorts SEO & Upload Package
- **Hook Title:** `Ranking Accidental Trickshots That Defied Physics 🤯🎱 #shorts #viral #amazing`
- **Description:**
  ```text
  Ranking the luckiest accidental trickshots in history! That 1 in a billion curve shot at Level 5 is genuinely impossible! 🎱💥

  All footages used in this video are not mine; full credit goes to the respective owners.

  #shorts #viral #trickshot #luck #physics #impossible #clutch #satisfying #sports #tabletennis #golf #nba
  ```
- **Optimal Upload Window:** 19:00 – 21:30 IST / 09:30 – 12:00 EST.
