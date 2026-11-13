---
sub_category_id: husband_wife_wholesome_surprises
sub_category_name: HUSBAND WIFE WHOLESOME SURPRISES
niche: wholesome_romance
references:
  - "@cliportey"
  - "@MrPurifiedWater"
audio_stem: public/audio/stems/husband_wife_wholesome_surprises_music_bed.mp3
audio_stem_bpm: 95
audio_stem_volume: 0.11
compositor: src/remotion/MrPurifiedWaterShort.tsx
anti_stutter_codec: OffthreadVideo
keyframe_interval_gop: 15
frame_rate: 30.0_cfr
---

# Sub-Category Skill: `husband_wife_wholesome_surprises` ("HUSBAND WIFE WHOLESOME SURPRISES")

> **MANDATORY FOR AI PIPELINE:** Subtitles are strictly disabled (`showSubtitles: false`). Every clip follows the 3-beat causal arc: Buildup ➔ Climax ➔ Payoff/Reaction. Stuttering is permanently prevented via Remotion `<OffthreadVideo>` and dense `-g 15` CFR 30fps encoding.

---

## 1. Core Narrative & Edit Philosophy
A **"HUSBAND WIFE WHOLESOME SURPRISES"** compilation hooks viewers with visceral retention psychology:
- **Buildup (`0` to `T_cause`, natural audio):** Raw ambient room/environment sound builds authenticity without voiceover clutter.
- **The Climax (`T_cause`):** Spouse brings unexpected gift/news into the room -> Target realizes what it is -> Emotional floodgates open with tears of happiness and warm embrace.
- **The Payoff / Reaction (`T_payoff`):** Clean emotional resolution (laughter, shock, relief, celebration).

---

## 2. Reference Architecture
- **Canvas:** `1080x1920` (9:16 vertical), `30 fps` constant frame rate.
- **Top 240px Header Banner:**
  - Line 1: `Ranking Best Of` (`Of` in `#FFEB3B`)
  - Line 2: `HUSBAND WIFE WHOLESOME SURPRISES` (`#FF2D55`)
  - Line 3: `(Heartwarming Edition)` (`#00D2FF`)
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
  ffmpeg -y -ss <start> -t <duration> -i raw_input.mp4 -vf "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -pix_fmt yuv420p -r 30 -g 15 -keyint_min 15 -sc_threshold 0 -c:a aac -ar 48000 -b:a 320k normalized_clip.mp4
  ```

---

## 4. Audio Stem & Music Bed Design
- **Track Genre:** Warm Emotional Cinematic Piano Background Bed
- **Stem File:** `public/audio/stems/husband_wife_wholesome_surprises_music_bed.mp3`
- **Volume Mixing:** `0.11` volume bed in Remotion props so natural sound effects and reactions cut through cleanly.
- **Mastering Standard:** EBU R128 (`-14.0 ± 1.0 LUFS`, True Peak `<= -1.5 dBTP`).

---

## 5. 5-Rank Benchmark Breakdown Table

| Rank | Level | Story Arc | Climax Action | Payoff / Reaction | Frames | Duration |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: |
| **5** | Level 1 | **Surprise Iceland Vacation** | Husband presents travel folder at airport terminal revealing tickets to Iceland | Wife realizes, beams with euphoric joy and ecstatic laughter | 210 | 7.0s |
| **4** | Level 2 | **Bedtime French Bulldog Puppy** | Husband slips tiny puppy into bed next to sleeping wife | Wife wakes up, gasps in shock, covers mouth crying happy tears cuddling pup | 225 | 7.5s |
| **3** | Level 3 | **Christmas Golden Retriever Puppy** | Husband brings golden retriever puppy with bow into living room | Wife drops to knees sobbing tears of pure joy cradling puppy | 240 | 8.0s |
| **2** | Level 4 | **Emotional Pregnancy Test Reveal** | Wife hands husband positive pregnancy test stick | Husband reads it, freezes in disbelief, tears roll down as they weep and embrace | 225 | 7.5s |
| **1** | Level 5 | **Brand New Dream Home Keys Surprise** | Husband hands wife letter inside empty house revealing they bought it | Wife breaks down in tears of pure joy and disbelief as kids jump and celebrate | 240 | 8.0s |

Total Duration: 1215 frames (40.5s @ 30fps).

---

## 6. QA Verification Gate
- [x] 0 black frames detected in 1fps contact sheet.
- [x] 0 third-party watermarks or channel repost logos.
- [x] Integrated Loudness: `-14.0 ± 1.0 LUFS`.
- [x] True Peak: `<= -1.5 dBTP`.
- [x] Contact sheet: `output/husband_wife_wholesome_surprises_qa_sheet.jpg` verified.

---

## 7. YouTube Shorts SEO & Upload Package
- **Hook Title:** `Ranking Emotional Husband & Wife Surprises 🥹❤️ #shorts #wholesome #marriage`
- **Description:**
  ```text
  Ranking the most heartwarming and emotional surprises between husbands and wives! True devotion! 🥺❤️

  All footages used in this video are not mine; full credit goes to the respective owners.

  #shorts #viral #wholesome #husbandwife #marriagegoals #love #family #emotional
  ```
- **Optimal Upload Window:** 19:00 – 21:30 IST / 09:30 – 12:00 EST.
