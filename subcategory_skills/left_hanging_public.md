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
- **Buildup (`0` to `T_cause`, natural audio):** Raw ambient room/broadcast sound builds authenticity without voiceover clutter.
- **The Climax (`T_cause`):** Person extends hand for high-five/fist bump with huge smile -> Other person looks away or ignores -> Hand stays frozen in mid-air.
- **The Payoff / Reaction (`T_payoff`):** Painful awkward recovery (fixing hair, clapping own hands, scratching ear, or frantic grab) with 100% natural clip reactions.

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
  ffmpeg -y -i raw_input.mp4 -vf "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -pix_fmt yuv420p -r 30 -g 15 -keyint_min 15 -sc_threshold 0 -c:a aac -ar 48000 -b:a 192k normalized_clip.mp4
  ```

---

## 4. Audio Stem & Music Bed Design
- **Track Genre:** Dry Comedic Funk / Quirk Beat
- **Stem File:** `public/audio/stems/left_hanging_public_music_bed.mp3`
- **Volume Mixing:** `0.11` volume bed in Remotion props so natural sound effects and reactions cut through cleanly.
- **Fade Dynamics:** `0.5s` linear fade-in, `1.5s` fade-out into the sonic outro.

---

## 5. 5-Rank Benchmark Breakdown Table

| Rank | Level | Source ID | Cause / The Setup | Climax Action | Payoff / Recovery | Duration (Frames) | QA Status |
| :---: | :---: | :--- | :--- | :--- | :--- | :---: | :---: |
| **5** | Level 1 | `Ft41g48Kp-0` (Arcade high five) | Guy watching punching arcade game raises palm high | Friends punch bag and celebrate without looking at him | Hand stays frozen in mid-air for 15s; smiles into camera dying inside | `6.5s` (`195f`) | **PASS** (Zero watermarks, 1080x1920) |
| **4** | Level 2 | `9WalqnrDu08` (Terry McLaurin NFL) | Receiver runs to endzone with open hand for handshake | Teammate #82 jumps right over him to celebrate with others | McLaurin smoothly claps his own hands and keeps running | `6.0s` (`180f`) | **PASS** (Zero watermarks, 1080x1920) |
| **3** | Level 3 | `2CBVPTgyZjA` (Phil Jackson Kobe) | Legendary coach Phil Jackson extends hand as Kobe walks to bench | Kobe walks right past his outstretched hand without breaking stride | Phil Jackson slowly scratches ear in deadpan awkwardness | `6.5s` (`195f`) | **PASS** (Zero watermarks, 1080x1920) |
| **2** | Level 4 | `PD03pcjKnMw` (Trump Polish Handshake) | President Trump finishes shaking Polish President's hand, reaches for First Lady | Polish First Lady walks completely past his outstretched hand | Trump stands frozen with hand in mid-air; First Lady greets Melania | `6.53s` (`196f`) | **PASS** (Zero watermarks, 1080x1920) |
| **1** | Level 5 | `TSdw4MKaxxo` (Ryan Seacrest Blind Idol) | Contestant holding white walking cane exits audition room | Ryan Seacrest enthusiastically raises hand for high-five | Blind contestant stares blankly; Seacrest frantically grabs his hand | `7.0s` (`210f`) | **PASS** (Zero watermarks, 1080x1920) |

---

## 6. QA Verification Gate
- [x] 0 black frames detected in 1fps contact sheet (`output/left_hanging_public_qa_sheet.jpg`).
- [x] 0 third-party watermarks or channel repost logos.
- [x] Integrated Loudness: `-14.5 LUFS` (Target: `-14.0 ± 1.0 LUFS`).
- [x] True Peak: `-1.7 dBFS` (Target: `<= -1.5 dBTP`).
- [x] Loudness Range: `5.7 LU` (Target: `<= 11 LU`).
- [x] Contact sheet: `output/left_hanging_public_qa_sheet.jpg` verified via visual QA.

---

## 7. YouTube Shorts SEO & Upload Package
- **Hook Title:** `Ranking The Worst Left Hanging Moments Ever 💀✋ #shorts #cringe #awkward`
- **Description:**
  ```text
  Ranking people who got left hanging on live camera! The secondhand embarrassment is off the charts 💀✋

  All footages used in this video are not mine; full credit goes to the respective owners.

  #shorts #viral #lefthanging #awkward #cringe #funny #handshake #fails #instantregret #secondhandembarrassment
  ```
- **Optimal Upload Window:** 20:00 IST / 10:30 EST.
