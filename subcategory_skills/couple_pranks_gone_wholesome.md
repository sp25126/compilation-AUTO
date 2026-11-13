---
sub_category_id: couple_pranks_gone_wholesome
sub_category_name: COUPLE PRANKS GONE WHOLESOME
niche: wholesome_romance
references:
  - "@cliportey"
  - "@MrPurifiedWater"
audio_stem: public/audio/stems/couple_pranks_gone_wholesome_music_bed.mp3
audio_stem_bpm: 115
audio_stem_volume: 0.11
compositor: src/remotion/MrPurifiedWaterShort.tsx
anti_stutter_codec: OffthreadVideo
keyframe_interval_gop: 15
frame_rate: 30.0_cfr
---

# Sub-Category Skill: `couple_pranks_gone_wholesome` ("COUPLE PRANKS GONE WHOLESOME")

> **MANDATORY FOR AI PIPELINE:** Subtitles are strictly disabled (`showSubtitles: false`). Every clip must follow the 3-beat causal arc: Buildup ➔ Climax ➔ Payoff/Reaction. Stuttering is permanently prevented via Remotion `<OffthreadVideo>` and dense `-g 15` CFR 30fps encoding.

---

## 1. Core Narrative & Edit Philosophy
A **"COUPLE PRANKS GONE WHOLESOME"** compilation hooks viewers with visceral retention psychology:
- **Buildup (`0` to `T_cause`, natural audio):** Raw ambient room/environment sound builds authenticity without voiceover clutter.
- **The Climax (`T_cause`):** Partner sets up playful prank camera -> Target is momentarily confused or startled -> Prankster reveals sweet twist or hug -> Both collapse into adorable laughter and kisses.
- **The Payoff / Reaction (`T_payoff`):** Clean emotional resolution (laughter, shock, relief, celebration).

---

## 2. Reference Architecture
- **Canvas:** `1080x1920` (9:16 vertical), `30 fps` constant frame rate.
- **Top 240px Header Banner:**
  - Line 1: `Ranking Best Of` (`Of` in `#FFEB3B`)
  - Line 2: `COUPLE PRANKS GONE WHOLESOME` (`#FF2D55`)
  - Line 3: `(Pure Chemistry Edition)` (`#00D2FF`)
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
- **Track Genre:** Acoustic Pop / Playful Wholesome Strum
- **Stem File:** `public/audio/stems/couple_pranks_gone_wholesome_music_bed.mp3`
- **Volume Mixing:** `0.11` volume bed in Remotion props so natural sound effects and reactions cut through cleanly.
- **Fade Dynamics:** `0.5s` linear fade-in, `1.5s` fade-out into the sonic outro.

---

## 5. 5-Rank Benchmark Breakdown Table

| Rank | Level | Story Arc | Climax Action | Payoff / Reaction |
| :---: | :---: | :--- | :--- | :--- |
| **5** | Level 1 | **The Invisible String Tap** | Girl pretends to pull invisible string attached to boyfriend across room. | Boyfriend plays along playfully, flying dramatically across couch into a hug. |
| **4** | Level 2 | **The Lip Balm Trick** | Girl applies lip balm and asks boyfriend if it smells weird. | Boyfriend leans in to sniff; she kisses his cheek, leaving him blushing brightly. |
| **3** | Level 3 | **The Fake Spill on New Shoes** | Boyfriend drops empty coffee cup onto girlfriend's new white sneakers. | Girl gasps in horror, realizes cup is empty, hits his chest playfully while laughing. |
| **2** | Level 4 | **The Serious Face Challenge** | Girl tries to hold deadpan serious eye contact without smiling. | Boyfriend makes one tiny eyebrow twitch; she bursts into breathless giggles and buries face in his neck. |
| **1** | Level 5 | **The Fake Ring Box Candy Reveal** | Boyfriend bends down on one knee holding jewelry box; opens it to reveal favorite sour candy. | Girl gasps, screams laughing, playfully shoves him, and hugs him tightly. |

---

## 6. QA Verification Gate
- [ ] 0 black frames detected in 1fps contact sheet.
- [ ] 0 third-party watermarks or channel repost logos.
- [ ] Integrated Loudness: `-14.0 ± 1.0 LUFS`.
- [ ] True Peak: `<= -1.5 dBTP`.
- [ ] Contact sheet: `output/couple_pranks_gone_wholesome_qa_sheet.jpg` verified.

---

## 7. YouTube Shorts SEO & Upload Package
- **Hook Title:** `Ranking Couple Pranks That Turned Wholesome 🥺❤️ #shorts #couplegoals #wholesome`
- **Description:**
  ```text
Ranking playful couple pranks that turned into the sweetest wholesome moments! True love right here! ❤️✨

All footages used in this video are not mine; full credit goes to the respective owners.

#shorts #viral #couplegoals #wholesome #relationship #love #funnycouples #cute
  ```
- **Optimal Upload Window:** 19:00 – 21:30 IST / 09:30 – 12:00 EST.
