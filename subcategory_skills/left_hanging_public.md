---
sub_category_id: left_hanging_public
sub_category_name: LEFT HANGING IN PUBLIC
niche: human_fails
references:
  - "@cliportey"
  - "@MrPurifiedWater"
audio_stem: public/audio/stems/left_hanging_public_music_bed.mp3
audio_stem_bpm: 110
audio_stem_volume: 0.11
compositor: src/remotion/MrPurifiedWaterShort.tsx
anti_stutter_codec: OffthreadVideo
keyframe_interval_gop: 15
frame_rate: 30.0_cfr
---

# Sub-Category Skill: `left_hanging_public` ("LEFT HANGING IN PUBLIC")

> **MANDATORY FOR AI PIPELINE:** Subtitles are strictly disabled (`showSubtitles: false`). Every clip must follow the 3-beat causal arc: Buildup ➔ Climax ➔ Payoff/Reaction. Stuttering is permanently prevented via Remotion `<OffthreadVideo>` and dense `-g 15` CFR 30fps encoding.

---

## 1. Core Narrative & Edit Philosophy
A **"LEFT HANGING IN PUBLIC"** compilation hooks viewers with visceral retention psychology:
- **Buildup (`0` to `T_cause`, natural audio):** Raw ambient room/environment sound builds authenticity without voiceover clutter.
- **The Climax (`T_cause`):** Person extends hand for high-five/fist bump with huge smile -> Other person looks away or ignores -> Person awkwardly covers by fixing hair or stretching.
- **The Payoff / Reaction (`T_payoff`):** Clean emotional resolution (laughter, shock, relief, celebration).

---

## 2. Reference Architecture
- **Canvas:** `1080x1920` (9:16 vertical), `30 fps` constant frame rate.
- **Top 240px Header Banner:**
  - Line 1: `Ranking Best Of` (`Of` in `#FFEB3B`)
  - Line 2: `LEFT HANGING IN PUBLIC` (`#FF2D55`)
  - Line 3: `(Secondhand Cringe)` (`#00D2FF`)
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
- **Track Genre:** Dry Comedic Funk / Quirk Beat
- **Stem File:** `public/audio/stems/left_hanging_public_music_bed.mp3`
- **Volume Mixing:** `0.11` volume bed in Remotion props so natural sound effects and reactions cut through cleanly.
- **Fade Dynamics:** `0.5s` linear fade-in, `1.5s` fade-out into the sonic outro.

---

## 5. 5-Rank Benchmark Breakdown Table

| Rank | Level | Story Arc | Climax Action | Payoff / Reaction |
| :---: | :---: | :--- | :--- | :--- |
| **5** | Level 1 | **Sideline High-Five Ghost** | Fan in front row reaches out palm as NBA player walks by. | Player looks dead ahead, ignores hand; fan slowly turns hand into a wave. |
| **4** | Level 2 | **Press Conference Fist Bump** | Journalist raises fist bump to coach after interview. | Coach looks at fist with confused grimace, grabs his microphone instead. |
| **3** | Level 3 | **World Leaders Double Handshake Fail** | President extends open hand for photo op on world stage. | Other prime minister looks down, misses hand, turns away to wave at crowd. |
| **2** | Level 4 | **Live TV Broadcast Handshake to Hug** | News anchor goes for handshake; co-host goes for hug. | Face collides into shoulder, hands flail awkwardly for 4 painful seconds on live air. |
| **1** | Level 5 | **Award Ceremony Stage Walk-Off** | Celebrity walks onto Oscar/Grammy stage and offers high-five to presenter. | Presenter completely walks past him; celebrity awkwardly smooths hair and looks at floor. |

---

## 6. QA Verification Gate
- [ ] 0 black frames detected in 1fps contact sheet.
- [ ] 0 third-party watermarks or channel repost logos.
- [ ] Integrated Loudness: `-14.0 ± 1.0 LUFS`.
- [ ] True Peak: `<= -1.5 dBTP`.
- [ ] Contact sheet: `output/left_hanging_public_qa_sheet.jpg` verified.

---

## 7. YouTube Shorts SEO & Upload Package
- **Hook Title:** `Ranking The Worst Left Hanging Moments Ever 💀✋ #shorts #cringe #awkward`
- **Description:**
  ```text
Ranking people who got left hanging on live television! The second-hand embarrassment is off the charts! 💀✋

All footages used in this video are not mine; full credit goes to the respective owners.

#shorts #viral #lefthanging #awkward #cringe #funny #handshake #fails #instantregret
  ```
- **Optimal Upload Window:** 19:00 – 21:30 IST / 09:30 – 12:00 EST.
