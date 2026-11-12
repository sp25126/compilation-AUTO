# Subcategory Production Skill: Public Love Confessions (`public_love_confessions`)

## 1. Niche Psychology & Algorithmic Hook Architecture
- **Niche:** `wholesome_romance` / Compilation Ranking Shorts
- **Audience Emotion:** Heart-racing tension -> vicarious embarrassment/secondhand vulnerability -> explosive relief & collective celebration.
- **Hook Strategy:** Immediately open on a bold, high-stakes public spectacle (medieval royal herald in front porch or front steps serenade). The viewer stays glued to witness whether the confession is accepted and how intensely the crush reacts.
- **Progression Dynamic:**
  - **Level 1 (Rank 5):** The Quirky Solo Gesture (costumed royal herald with scroll & crown).
  - **Level 2 (Rank 4):** The Front Porch Steps Serenade (harmony vocals + bouquet + airborne hug).
  - **Level 3 (Rank 3):** The Acoustic Classroom Ambush (live guitar singing + stunned joy).
  - **Level 4 (Rank 2):** The Choreographed Courtyard Flash Mob (synchronized umbrella reveal).
  - **Level 5 (Rank 1):** The Packed Arena Proposal (2,000 cheering students + court floor leap).

---

## 2. Benchmark 5-Clip Table

| Rank | Level | Source Title & URL/ID | Cause / The Setup | Climax / Bold Gesture | Payoff / Reaction | Duration | QA Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **5** | **Level 1** | `r_eofkmueqhoza1` (Reddit r/MadeMeSmile) | Girl answers front door | Herald in blonde powdered wig unrolls "PROM?" scroll | Places golden crown on her head; laughter & embrace | 7.5s (225f) | **PASS** (Zero watermarks, 1080x1920 vertical) |
| **4** | **Level 2** | `yt_prH` (@Joshua Arizmendi) | Friends serenade girl on steps | Boy emerges with huge yellow rose bouquet | Girl covers face in shock/tears, jumps into his arms | 7.5s (225f) | **PASS** (Zero watermarks, 1080x1920 vertical) |
| **3** | **Level 3** | `yt_hA3` (@Jason Pitts) | Classroom quiet during study session | Guy brings acoustic guitar, sings confession directly to her | Girl screams "YES!", drops down laughing, emotional hug | 8.0s (240f) | **PASS** (Zero watermarks, 1080x1920 vertical) |
| **4** | **Level 4** | `yt_xAjOUVzpKJA` (@Alhambra High School) | High school courtyard dance troupe | 5 dancers snap open umbrellas spelling "P R O M ?" | Guy walks out with umbrella & flowers; she leaps to hug him | 8.0s (240f) | **PASS** (Zero watermarks, blur-fill 1080x1920) |
| **1** | **Level 5** | `yt_a7i2zp` (@Buena Park High School) | Packed arena pep rally (2,000 students) | Giant banner unfurls: "LINA, WILL YOU MARRY ME?" & knee drop | Lina leaps through the air into his arms on court floor | 7.5s (224f) | **PASS** (Zero watermarks, blur-fill 1080x1920) |

---

## 3. Audio & Music Design (Earshot Standard)
- **Unique Stem:** `public/audio/stems/public_love_confessions_music_bed.mp3`
  - Track: *Grouplove - Tongue Tied (Mastered Instrumental)*
  - Audio Spec: 48.0s bed, 48kHz, 192kbps stereo, 1.0s exponential fade-in, 2.0s fade-out.
  - **Volume:** Set strictly to `0.11` in Remotion props.
- **Natural Clip Audio:** Kept at `1.0` gain. Voices, acoustic singing, guitar strums, crowd cheers, classroom gasps, and gym arena roars remain crystal clear and punchy.
- **Outro:** Earshot sonic brand trigger at frame 1154 with LevelZero0ne logo badge.

---

## 4. Visual QA & Formatting Gates
- **Resolution:** 1080x1920 vertical canvas @ 30.0 fps (yuv420p).
- **Subtitles:** Explicitly disabled (`showSubtitles: false`) per user rules.
- **Visual Artifacts:** 0 watermarks, 0 TikTok/CBS overlays, 0 news badges, 0 black frames.
- **Widescreen Action Handling:** Widescreen spectacle moments (umbrella spellout & gymnasium arena banner) rendered using high-fidelity blur-fill background framing to avoid cropping critical visual storytelling elements.

---

## 5. Remotion Render & Mastering Command Reference
```bash
# Remotion Render
npx remotion render RankingShort output/public_love_confessions_raw.mp4 --props=cue_sheet_public_love_confessions.json --concurrency=2 --overwrite

# Broadcast EBU R128 Audio Mastering
ffmpeg -i output/public_love_confessions_raw.mp4 -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:v copy -c:a aac -b:a 320k -y output/public_love_confessions_mastered.mp4

# Loudness Verification
ffmpeg -i output/public_love_confessions_mastered.mp4 -af "ebur128=peak=true" -f null -

# 1fps Final Contact Sheet
ffmpeg -y -i output/public_love_confessions_mastered.mp4 -vf "fps=1,scale=260:-1,tile=8x6" -frames:v 1 -q:v 3 output/public_love_confessions_qa_sheet.jpg
```
