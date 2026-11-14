---
sub_category_id: object_collision_fails
sub_category_name: OBJECT COLLISION FAILS
niche: npc_glitches
references:
  - "@cliportey"
  - "@MrPurifiedWater"
audio_stem: public/audio/stems/object_collision_fails_music_bed.mp3
audio_stem_bpm: 128
audio_stem_volume: 0.11
compositor: src/remotion/MrPurifiedWaterShort.tsx
anti_stutter_codec: OffthreadVideo
keyframe_interval_gop: 15
frame_rate: 30.0_cfr
---

# Sub-Category Skill: `object_collision_fails` ("Ranking The Most Object Collision Fails (Physics Broken)")

> **MANDATORY FOR AI PIPELINE:** Subtitles are strictly disabled (`showSubtitles: false`). Every clip follows a high-retention 3-beat causal arc: Unaware approach ➔ Sudden physical collision with invisible barrier / unrendered mesh ➔ Physics engine recoil/rebound. Zero stuttering via Remotion `<OffthreadVideo>` and dense `-g 15` CFR 30fps encoding.

---

## 1. Core Narrative & Edit Philosophy
An **"OBJECT COLLISION FAILS"** compilation delivers comedic, viral NPC glitch energy:
- **Buildup (`0` to `T_cause`):** Subject is completely absorbed in normal real-world routines (walking with friends, staring into phone screen, entering shops) unaware of the invisible barrier ahead.
- **The Climax (`T_cause`):** Sudden, high-speed impact with transparent glass doors, invisible hitboxes, or unrendered collision meshes, causing an abrupt physical bounce.
- **The Payoff / Reaction (`T_payoff`):** Disoriented recovery, checking nose/forehead, stepping back in confusion, or looping into the exact same collision.

---

## 2. Reference Architecture
- **Canvas:** `1080x1920` (9:16 vertical), `30 fps` constant frame rate.
- **Top 240px Header Banner:**
  - Line 1: `Ranking The Most` (`Most` in `#FFEB3B`)
  - Line 2: `Object Collision Fails` (`#FF2D55`)
  - Line 3: `(Physics Broken)` (`#00D2FF`)
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
  ffmpeg -hide_banner -loglevel error -nostats -y -ss <start> -t <duration> -i <src> -r 30 -g 15 -keyint_min 15 -sc_threshold 0 -pix_fmt yuv420p -c:v libx264 -preset fast -crf 18 -c:a aac -b:a 192k -ar 48000 public/clips/object_collision_fails/rank_<N>.mp4
  ```

---

## 4. Audio Stem & Music Bed Design
- **Track Genre:** High-Energy Glitch Synth / NPC Electronic Beat
- **Stem File:** `public/audio/stems/object_collision_fails_music_bed.mp3`
- **Volume Mixing:** `0.11` volume bed in Remotion props so natural sound effects, impacts, and reactions cut through cleanly.
- **Fade Dynamics:** `0.5s` linear fade-in, `1.5s` fade-out into the sonic outro.

---

## 5. 5-Rank Benchmark Breakdown Table

| Rank | Level | Story Arc | Climax Action | Payoff / Reaction | Frames (Dur) |
| :---: | :---: | :--- | :--- | :--- | :---: |
| **5** | Level 1 | **Invisible Hitbox Doorway** | Pedestrian casually walks directly into transparent glass doorway. | Head bonks glass, stops abruptly, steps back confused. | 150 (5.0s) |
| **4** | Level 2 | **Smartphone Distraction Impact** | Pedestrian texting on smartphone collides head-first into glass barrier. | Phone nearly drops, rubs face in disbelief. | 150 (5.0s) |
| **3** | Level 3 | **Unrendered Storefront Mesh** | Full collision mesh fails to register as customer faceplants store window. | Full-body rebound, shopper pauses wondering what happened. | 150 (5.0s) |
| **2** | Level 4 | **Infinite Pathfinding Loop** | Disoriented shopper walks into identical glass wall three times consecutively. | Stuck in looping animation before finally locating door opening. | 167 (5.6s) |
| **1** | Level 5 | **Maximum Velocity Ricochet** | Streamer full sprint into sliding glass door completely breaks physics engine. | Violent rebound bounce, dramatic shock and collapse in disbelief. | 167 (5.6s) |

---

## 6. QA Verification Gate
- [x] 0 black frames detected in 1fps contact sheet.
- [x] 0 third-party watermarks or channel repost logos.
- [x] Integrated Loudness: `-14.0 ± 1.0 LUFS`.
- [x] True Peak: `<= -1.5 dBTP`.
- [x] Contact sheet: `output/object_collision_fails_qa_sheet.jpg` verified.

---

## 7. YouTube Shorts SEO & Upload Package
- **Hook Title:** `Ranking The Most Object Collision Fails (Physics Broken) 💀🚶‍♂️ #shorts #viral #funny`
- **Description:**
  ```text
  Ranking the most hilarious real-life object collision fails! That Level 5 sprint at the end proved the physics engine completely crashed! 💀💥

  All footages used in this video are not mine; full credit goes to the respective owners.

  #shorts #viral #funny #npc #glitch #physicsbroken #fails #comedy #humor #matrixglitch
  ```
- **Optimal Upload Window:** 18:30 – 21:00 IST / 09:00 – 11:30 EST.
