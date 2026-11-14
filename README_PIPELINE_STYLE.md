# Automated Viral Compilation Pipeline (LevelZero0ne Style)
## Developer & AI IDE Master Reference Document

> **Mandatory Rule for All AI Models:**  
> When operating on this repository, you **MUST** strictly preserve the creator's signature viral video style, architecture, anti-stutter pipeline, and EBU R128 audio standards detailed in this document. Never downgrade to generic transitions, never add unauthorized subtitles, never skip CFR encoding, and never commit media binaries.

---

## 1. Channel Identity & Video Archetype

- **Inspiration & Quality Standard:** LevelZero0ne (@MrPurifiedWater + @cliportey hybrid style).
- **Format:** YouTube Shorts / Instagram Reels / TikTok vertical video ($1080 \times 1920$ resolution, strictly $30.0\text{ fps}$).
- **Structure:** 5-Level Escalating Compilation Ladder:
  - **Rank 5 (Level 1):** The Hook / Lighthearted opening.
  - **Rank 4 (Level 2):** Momentum builder.
  - **Rank 3 (Level 3):** High stakes / Rising tension.
  - **Rank 2 (Level 4):** Catastrophic blunder / Intense reaction.
  - **Rank 1 (Level 5):** The Boss Climax / Unbelievable viral peak.
- **Narrative Arc per Clip:** Single continuous shot with a complete 3-beat story arc:
  $$\text{Buildup} \longrightarrow \text{Trigger / Cause } (T_{\text{cause}}) \longrightarrow \text{Climax / Payoff } (T_{\text{payoff}})$$
  *Zero choppy montages or alternating cuts within a single rank.*

---

## 2. Visual Staging & Compositor Standards (`MrPurifiedWaterShort.tsx`)

1. **Header Badge:**
   - 3-line centered header text at top:
     - Line 1: `RANKING THE BEST` or `RANKING FUNNIEST` (Small yellow accent)
     - Line 2: `SUBJECT NAME` (Bold uppercase white with drop shadow)
     - Line 3: `(VERSION TAG)` (Subtle grey parenthetical)
   - **Prohibited:** Never add opaque rectangular solid pills or banners covering footage. Maintain clean cinematic full-bleed vertical framing.
2. **Subtitles Policy:**
   - `showSubtitles: false` is **permanently enforced**. Because the compilations rely on 100% natural clip audio and comedic SFX rather than an AI synthetic voiceover, on-screen caption pills look cluttered and are disabled.
3. **Branding & Transitions:**
   - **Clip 1:** Quick, subtle LevelZero0ne / Mew coin pop without black screen pauses.
   - **Rank Indicators:** Dynamic rank countdown ($5 \to 1$) with subtle kinetic bounce.
   - **Outro:** Full 75-frame ($2.5\text{s}$) Earshot sonic brand loop with coin lockup.

---

## 3. Strict Media Pre-Encoding Mandate (The Anti-Stutter Rule)

Raw internet downloads (TikTok, Reddit, YouTube) use Variable Frame Rates (VFR) and long keyframe intervals (GOP 120-250), which cause severe frame drops and stuttering in Remotion's headless Chromium canvas.

**Every clip MUST be pre-encoded prior to Remotion compositing:**
```bash
ffmpeg -y -ss <start_time> -t <duration> -i <source_file> \
  -r 30 -g 15 -keyint_min 15 -sc_threshold 0 \
  -pix_fmt yuv420p -c:v libx264 -preset fast -crf 18 \
  -c:a aac -b:a 192k -ar 48000 \
  public/clips/<sub_category_id>/rank_<rank>.mp4
```
- `-r 30`: Enforces strict Constant Frame Rate ($30.0\text{ fps}$).
- `-g 15 -keyint_min 15 -sc_threshold 0`: Dense keyframe injection (I-frame every 0.5s) ensuring zero frame-seeking lag.
- `-pix_fmt yuv420p`: Universal browser color space.
- `-ar 48000`: Studio-standard $48\text{ kHz}$ audio.

---

## 4. Forensic Audio Architecture (EBU R128 Standards)

Every video must meet broadcast mobile compliance:
- **Integrated Loudness ($I$):** Mastered strictly to **$-14.0 \pm 1.0\text{ LUFS}$**.
- **True Peak ($TP$):** Clamped strictly to **$\le -1.5\text{ dBTP}$** (guarantees zero digital clipping or speaker distortion on mobile phones).
- **Loudness Range ($LRA$):** Maintained between $5.0$ and $15.0\text{ LU}$.
- **Music Bed Mixing:** Unique genre-specific background music bed (e.g. `public/audio/stems/<id>_music_bed.mp3`) mixed at a subtle **$11\%$ volume (`0.11`)** underneath $100\%$ natural clip audio.

**Two-Pass Mastering Command:**
```bash
# Pass 1: Measure
ffmpeg -hide_banner -nostats -i output/raw.mp4 -af "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json" -f null -

# Pass 2: Apply Linear Loudnorm
ffmpeg -hide_banner -y -i output/raw.mp4 \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=<I>:measured_TP=<TP>:measured_LRA=<LRA>:measured_thresh=<thresh>:offset=<offset>:linear=true" \
  -c:v copy -c:a aac -b:a 320k output/mastered.mp4
```

---

## 5. Automated Quality Assurance Gate

Before declaring any compilation complete:
1. **0 Black Frames:** Verify frame-by-frame via FFmpeg `blackdetect=d=0.5:pic_th=0.98:pix_th=0.10` or a 1fps contact sheet.
2. **0 Watermarks:** No TikTok watermarks, CBS/news banners, or overlay handles.
3. **Mandatory Copyright Attribution:** Every generated upload metadata JSON and skill documentation must include:
   > *"All footages used in this video are not mine; full credit goes to the respective owners."*

---

## 6. Git Hygiene & Remote Sync

- **Remote:** `https://github.com/sp25126/compilation-AUTO.git`
- **Strict `.gitignore` Policy:** **NEVER** track or commit video binaries (`*.mp4`, `*.mov`, `temp_harvest/`, `output/`).
- Only commit cue sheets, pipeline scripts, documentation, and skill markdown files.
