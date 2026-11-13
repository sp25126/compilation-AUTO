---
sub_category_id: love_at_first_sight_caught
sub_category_name: LOVE AT FIRST SIGHT CAUGHT ON CAMERA
niche: wholesome_romance
references:
  - "@cliportey"
  - "@MrPurifiedWater"
audio_stem: public/audio/stems/love_at_first_sight_caught_music_bed.mp3
audio_stem_bpm: 105
audio_stem_volume: 0.11
compositor: src/remotion/MrPurifiedWaterShort.tsx
anti_stutter_codec: OffthreadVideo
keyframe_interval_gop: 15
frame_rate: 30.0_cfr
---

# Sub-Category Skill: `love_at_first_sight_caught` ("LOVE AT FIRST SIGHT CAUGHT ON CAMERA")

> **MANDATORY FOR AI PIPELINE:** Subtitles are strictly disabled (`showSubtitles: false`). Every clip must follow the 3-beat causal arc: Buildup ➔ Climax ➔ Payoff/Reaction. Stuttering is permanently prevented via Remotion `<OffthreadVideo>` and dense `-g 15` CFR 30fps encoding.

---

## 1. Core Narrative & Edit Philosophy
A **"LOVE AT FIRST SIGHT CAUGHT ON CAMERA"** compilation hooks viewers with visceral retention psychology:
- **Buildup (`0` to `T_cause`, natural audio):** Raw ambient room/environment sound builds authenticity without voiceover clutter.
- **The Climax (`T_cause`):** Two strangers in public environment (subway, crosswalk, sporting event) -> Unplanned eye contact locks -> Both smile warmly and start an authentic conversation.
- **The Payoff / Reaction (`T_payoff`):** Clean emotional resolution (laughter, shock, relief, celebration).

---

## 2. Reference Architecture
- **Canvas:** `1080x1920` (9:16 vertical), `30 fps` constant frame rate.
- **Top 240px Header Banner:**
  - Line 1: `Ranking Best Of` (`Of` in `#FFEB3B`)
  - Line 2: `LOVE AT FIRST SIGHT CAUGHT ON CAMERA` (`#FF2D55`)
  - Line 3: `(Pure Chemistry Sparks)` (`#00D2FF`)
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
- **Track Genre:** Dreamy Lo-Fi / Romantic Soul Groove
- **Stem File:** `public/audio/stems/love_at_first_sight_caught_music_bed.mp3`
- **Volume Mixing:** `0.11` volume bed in Remotion props so natural sound effects and reactions cut through cleanly.
- **Fade Dynamics:** `0.5s` linear fade-in, `1.5s` fade-out into the sonic outro.

---

## 5. 5-Rank Benchmark Breakdown Table

| Rank | Level | Story Arc | Climax Action | Payoff / Reaction |
| :---: | :---: | :--- | :--- | :--- |
| **5** | Level 1 | **The First Spark** (Shot 31: 4.27s) | Dark-haired girl with red lipstick & girl in black tank top lock eyes in complete silence. | Both blush and break into sweet, bashful smiles as the spark ignites. |
| **4** | Level 2 | **The Shy Giggle** (Shot 26: 5.00s) | Ponytail girl in denim jacket covers her mouth laughing bashfully. | Romantic tension peaks while blonde girl grins warmly, gaze never wavering. |
| **3** | Level 3 | **Magnetic Eye Lock** (Shot 29: 7.00s) | Strangers hold deep, unbroken eye contact across the studio room. | The tension melts into pure, radiant, glowing smiles and genuine warmth. |
| **2** | Level 4 | **The Lean-In** (Shot 27: 7.00s) | Guy in blue hoodie gently leans in closer while girl looks up into his eyes. | She bites her lip with sweet romantic tension and undeniable mutual chemistry. |
| **1** | Level 5 | **The Climax Embrace** (Shot 62-63: 4.70s) | The countdown bell rings concluding the 4-minute stranger experiment. | Guy opens his arms with a radiant smile, she steps in close without hesitation, and they share an emotional, full embrace. |

---

## 6. QA Verification Gate
- [x] 0 black frames detected in 1fps contact sheet.
- [x] 0 third-party watermarks or channel repost logos.
- [x] Integrated Loudness: `-14.1 LUFS` (Target: `-14.0 ± 1.0 LUFS`).
- [x] True Peak: `-1.5 dBTP` (Target: `<= -1.5 dBTP`).
- [x] Loudness Range (LRA): `8.5 LU`.
- [x] Contact sheet: `output/love_at_first_sight_caught_qa_sheet.jpg` verified with `read_file`.
- [x] Remotion render: `output/love_at_first_sight_caught_raw.mp4` (914 frames @ 30fps).
- [x] Mastered export: `output/love_at_first_sight_caught_mastered.mp4`.

---

## 7. YouTube Shorts SEO & Upload Package
- **Hook Title:** `Ranking Love At First Sight Moments Caught On Camera 🥹✨ #shorts #romance #love`
- **Description:**
  ```text
Ranking moments where two strangers locked eyes and felt instant undeniable chemistry! Destiny caught on tape! ✨❤️

All footages used in this video are not mine; full credit goes to the respective owners.

#shorts #viral #loveatfirstsight #romance #wholesome #destiny #chemistry #strangers
  ```
- **Optimal Upload Window:** 19:00 – 21:30 IST / 09:30 – 12:00 EST.
