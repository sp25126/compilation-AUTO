---
sub_category_id: taunting_animals
sub_category_name: TAUNTING ANIMALS
niche: instant_karma
references:
  - "@cliportey"
  - "@MrPurifiedWater"
audio_stem: public/audio/stems/taunting_animals_music_bed.mp3
audio_stem_bpm: 125
audio_stem_volume: 0.11
compositor: src/remotion/MrPurifiedWaterShort.tsx
anti_stutter_codec: OffthreadVideo
keyframe_interval_gop: 15
frame_rate: 30.0_cfr
---

# Sub-Category Skill: `taunting_animals` ("TAUNTING ANIMALS")

> **MANDATORY FOR AI PIPELINE:** Subtitles are strictly disabled (`showSubtitles: false`). Every clip must follow the 3-beat causal arc: Buildup ➔ Climax ➔ Payoff/Reaction. Stuttering is permanently prevented via Remotion `<OffthreadVideo>` and dense `-g 15` CFR 30fps encoding.

---

## 1. Core Narrative & Edit Philosophy
A **"TAUNTING ANIMALS"** compilation hooks viewers with visceral retention psychology:
- **Buildup (`0` to `T_cause`, natural audio):** Raw ambient room/environment sound builds authenticity without voiceover clutter.
- **The Climax (`T_cause`):** Human arrogantly teases/pokes an animal -> Animal snaps/counter-attacks with lightning speed -> Human panics, runs away, or gets humbled.
- **The Payoff / Reaction (`T_payoff`):** Clean emotional resolution (laughter, shock, relief, celebration).

---

## 2. Reference Architecture
- **Canvas:** `1080x1920` (9:16 vertical), `30 fps` constant frame rate.
- **Top 240px Header Banner:**
  - Line 1: `Ranking Best Of` (`Of` in `#FFEB3B`)
  - Line 2: `TAUNTING ANIMALS` (`#FF2D55`)
  - Line 3: `(Never Taunt Nature)` (`#00D2FF`)
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
- **Track Genre:** Fast Funky Bass / Brazilian Phonk
- **Stem File:** `public/audio/stems/taunting_animals_music_bed.mp3`
- **Volume Mixing:** `0.11` volume bed in Remotion props so natural sound effects and reactions cut through cleanly.
- **Fade Dynamics:** `0.5s` linear fade-in, `1.5s` fade-out into the sonic outro.

---

## 5. 5-Rank Benchmark Breakdown Table

| Rank | Level | Story Arc | Climax Action | Payoff / Reaction | Source File & Timestamps |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **5** | Level 1 | **Poking the Nesting Goose** | Woman taunts geese in yard and gets chased down. | Goose launches airborne; woman sprints screaming up patio stairs. | `temp_harvest/taunting_animals/56G-yaQ7moo.mp4` [19.5s–26.5s] |
| **4** | Level 2 | **Silverback Zoo Glass Slam** | Visitor aggressively stares down and taunts silverback gorilla. | 400 lb gorilla charges at lightning speed and slams glass barrier with thunderous boom. | `temp_harvest/taunting_animals/4BFmfV0ZrLQ.mp4` [10.5s–17.5s] |
| **3** | Level 3 | **Monkey Bag Robbery** | Tourist dangles belongings near wild macaque monkeys. | Monkey snatches backpack/purse in broad daylight and runs upright like a thief. | `temp_harvest/taunting_animals/monkey_bag.mp4` [49.0s–56.5s] |
| **2** | Level 4 | **Delivery Guy Kicks Stray Dog** | Delivery driver aggressively attempts a kick at a sleeping dog. | Driver slips violently on slick pavement, lands flat on his spine; pizza destroyed while dog watches calmly. | `temp_harvest/taunting_animals/dog_pizza.mp4` [0.0s–7.0s] |
| **1** | Level 5 | **Challenging Farm Ram to Headbutt** | Guy wears helmet and challenges massive horned ram head-on. | Ram charges like a missile, delivers concussive headbutt that knocks him backwards into mud. | `temp_harvest/taunting_animals/lzsTO3YMYAU.mp4` [6.5s–14.5s] |

---

## 6. QA Verification Gate
- [x] 0 black frames detected in 1fps contact sheet (`output/taunting_animals_qa_sheet.jpg`).
- [x] 0 third-party watermarks, news logos, or channel repost overlays.
- [x] Integrated Loudness: `-14.9 LUFS` (Strictly within `-14.0 ± 1.0 LUFS` standard).
- [x] True Peak: `-1.6 dBTP` (Strictly meets `<= -1.5 dBTP` ceiling).
- [x] Dense GOP `-g 15` CFR 30fps anti-stutter encoding verified for Remotion `<OffthreadVideo>`.
- [x] Outro sonic branding verified with LevelZero0ne animated badge and subscribe CTA.

---

## 7. YouTube Shorts SEO & Upload Package
- **Hook Title:** `Ranking Instant Karma for Taunting Animals 🐒⚡ #shorts #instantkarma #animals`
- **Description:**
  ```text
Ranking people who taunted animals and faced instant regret! Never disrespect wildlife! 🐆💥

All footages used in this video are not mine; full credit goes to the respective owners.

#shorts #viral #instantkarma #animals #wildlife #fails #instantregret #monkey
  ```
- **Optimal Upload Window:** 19:00 – 21:30 IST / 09:30 – 12:00 EST.
