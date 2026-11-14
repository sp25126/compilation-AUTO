# Subcategory Production Skill: Real-Life Dialogue Loops (`dialogue_loop_real_life`)

## Overview & Niche Identity
- **Niche**: `npc_glitches`
- **Subcategory ID**: `dialogue_loop_real_life`
- **Concept**: Ranking real-life NPC dialogue loops where real humans glitch, repeat the same phrase, or deliver uncanny conversational loops with zero awareness or deadpan conviction.
- **Style**: Hybrid `@MrPurifiedWater` + `@cliportey` ranking format (Rank 5 -> Rank 1 / Level 1 -> Level 5), high-contrast kinetic visual hierarchy, custom quirk synth-glitch audio bed, clean zero-watermark footage.

---

## 5-Clip Benchmark Table

| Rank | Level | Clip Title / Subject | Source File / ID | Duration | Cause -> Payoff -> Reaction Story | Audio Foley & Dialogue Loop |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Rank 5** | **Level 1** | The Proximity Greeting Loop | `gfGt3F7nj6Q` | 7.03s | Rowan steps out of his cottage; Baelin the fisherman turns and triggers the proximity greeting line 3 times consecutively as Rowan stares in bewilderment. | Repeated crisp voice line: *"Morning!... Morning!... Morning!"* with nature ambiance. |
| **Rank 4** | **Level 2** | The Boundary Dialogue Glitch | `XatCv5jfcYU` | 7.00s | Pedestrian stands rigidly on the rainbow crosswalk boundary and stiffly repeats territorial script lines to camera operator. | Robotic cadence: *"This is the gayborhood and you are not welcome!"* -> *"That's why I need to be here."* |
| **Rank 3** | **Level 3** | Combat Voiceover Loop | `688z-4SWxOQ` | 8.03s | ProZD attacks multiple enemies with sword strikes; character model repeatedly fires the exact same single voiceover bark without variation. | Fast-paced combat loop: *"I think that enemy got the point!"* repeated identically on every strike. |
| **Rank 2** | **Level 4** | The Escalation Loop | `nx9xE5-5BGA` | 7.00s | Man confrontational in retail store gets stuck in an uncanny cognitive loop, repeating the identical phrase while squaring up. | Iconic deadpan delivery: *"You're not that guy pal, trust me you're not that guy. Okay? You're not that guy."* |
| **Rank 1** | **Level 5** | The Infinite Brainfreeze Loop | `6yPgDBvMLtA` | 8.44s | Studio documentary interview where a kid attempts to formulate a profound thought, entering an infinite loop of linguistic recursion. | The legendary internet speech loop: *"Have you ever had a dream that you... you could do anything?"* |

---

## Production Pipeline & Engineering Rules

### 1. File Isolation
All intermediate and final outputs are strictly isolated:
- Harvest: `temp_harvest/dialogue_loop_real_life/`
- Rendered Clips: `public/clips/dialogue_loop_real_life/`
- Cue Sheet: `cue_sheet_dialogue_loop_real_life.json`
- Raw Render: `output/dialogue_loop_real_life_raw.mp4`
- Mastered Export: `output/dialogue_loop_real_life_mastered.mp4`
- QA Contact Sheet: `output/dialogue_loop_real_life_qa_sheet.jpg`
- Upload Metadata: `output/dialogue_loop_real_life_upload_metadata.json`

### 2. Video Processing & Aspect Ratio Harmonization
- Format: Full-bleed 1080x1920 (9:16 vertical shorts).
- CFR 30fps keyframed every 15 frames (`-r 30 -g 15 -keyint_min 15 -sc_threshold 0 -pix_fmt yuv420p -c:v libx264 -preset fast -crf 18`).
- 16:9 / 4:3 widescreen inputs utilize a stylized dual-layer stack: blurred canvas background (`boxblur=20:5`) with centered full-detail foreground scaling.
- Native vertical inputs (Rank 2) cropped precisely (`crop=405:720`) to eliminate black letterbox bars.

### 3. Audio & Music Design
- **Music Bed**: `public/audio/stems/dialogue_loop_real_life_music_bed.mp3` (Quirky 8-bit / synth game loop) mixed at `volume: 0.11`.
- **Dialogue Primacy**: Natural clip audio remains 100% intelligible with crisp voice frequencies pocketed above the subtle background bed.
- **EBU R128 Broadcast Loudness**: Mastered using two-pass `loudnorm=I=-14:TP=-1.5:LRA=11:linear=true` with 320kbps AAC audio.

### 4. QA Gates
- Pre-render 2fps contact sheet verification (rejection of watermarks, hardcoded news tickers, TikTok badges).
- Post-render 1fps contact sheet verification (0 black frames, complete narrative payoffs, clean brand outro).
