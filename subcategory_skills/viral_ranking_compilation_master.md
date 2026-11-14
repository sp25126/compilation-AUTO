---
name: viral-ranking-compilation-master
description: Master production blueprint and execution standard for LevelZero0ne (@MrPurifiedWater + @cliportey) viral ranking compilation Shorts. Use whenever authoring, sourcing, editing, compositing, or mastering 5-tier escalating ranking compilation videos.
---

# Master Viral Ranking Compilation Skill

This skill enforces the exact production, visual staging, anti-stutter encoding, audio mastering, and QA protocols for the 50-to-60-day viral Shorts series.

## 1. Core Production Protocol

### 1.1 Escalating 5-Level Ladder
Every compilation must feature 5 distinct real-life clips escalating in comedy, shock value, or difficulty:
- **Rank 5 (Level 1):** The initial hook / relatable misstep.
- **Rank 4 (Level 2):** Clear momentum escalation.
- **Rank 3 (Level 3):** High stakes / rising tension.
- **Rank 2 (Level 4):** Catastrophic blunder or extreme reaction.
- **Rank 1 (Level 5):** The ultimate viral climax / boss level.

### 1.2 Single-Shot Narrative Arc
Each clip must be a **single continuous shot** (~6.0s - 9.0s) adhering to the 3-beat causal structure:
$$\text{Buildup } (T_0) \longrightarrow \text{Trigger / Cause } (T_{\text{cause}}) \longrightarrow \text{Climax / Payoff } (T_{\text{payoff}})$$
*Never accept multi-cut edits, TikTok compilations, or choppy montages within a single rank.*

---

## 2. Media Pre-Processing (The Anti-Stutter Mandate)

All raw candidate clips must be pre-encoded to Constant Frame Rate 30.0 fps before Remotion compositing:

```bash
ffmpeg -y -ss <start> -t <duration> -i <raw_file> \
  -r 30 -g 15 -keyint_min 15 -sc_threshold 0 \
  -pix_fmt yuv420p -c:v libx264 -preset fast -crf 18 \
  -c:a aac -b:a 192k -ar 48000 \
  public/clips/<sub_id>/rank_<N>.mp4
```

- **Strict CFR 30fps (`-r 30`):** Aligns perfectly with Remotion timeline frames.
- **Dense Keyframe Spacing (`-g 15`):** Injects an I-frame every 0.5s, eliminating seeking hitches.
- **Color & Sample Rate:** Universal `yuv420p` and studio `48000 Hz` stereo AAC.

---

## 3. Remotion Compositing (`MrPurifiedWaterShort.tsx`)

- **Composition Resolution:** $1080 \times 1920$ vertical canvas.
- **Video Element:** Rendered with `<OffthreadVideo>` for hardware off-thread decoding.
- **Subtitles:** Strictly disabled (`showSubtitles: false`) across all cue sheets.
- **Top Badge:** 3-line centered text (Ranking The Best / Subject / Version Tag). No opaque rectangular pill overlays.
- **Branding:** Clip 1 features subtle LevelZero0ne / Mew coin pop without black screen pauses. Outro features the 75-frame Earshot sonic brand loop.

---

## 4. Broadcast Audio Mastering (EBU R128)

Apply two-pass linear `loudnorm` normalization to the raw render:
```bash
ffmpeg -y -i output/<sub_id>_raw.mp4 \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11:linear=true" \
  -c:v copy -c:a aac -b:a 320k \
  output/<sub_id>_mastered.mp4
```
- **Integrated Loudness ($I$):** Target $-14.0 \pm 1.0\text{ LUFS}$.
- **True Peak ($TP$):** Clamped to $\le -1.5\text{ dBTP}$.
- **Music Bed Volume:** Category-matched stem mixed at `volume: 0.11` beneath 100% natural clip audio.

---

## 5. Automated Quality Assurance

1. **Visual Contact Sheet:** Verify a 1fps contact sheet (`output/<sub_id>_qa_sheet.jpg`) or run `blackdetect`:
   - 0 black frames.
   - 0 dropped frames.
   - 0 watermarks (TikTok, CBS, channel logos).
2. **Mandatory Disclaimer:** Embed in all metadata JSON and skill documents:
   > *"All footages used in this video are not mine; full credit goes to the respective owners."*
