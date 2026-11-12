---
sub_category_id: pets_being_smart
sub_category_name: 200 IQ SMART PETS
niche: funny_animals
references:
  - "@MrPurifiedWater"
  - "@cliportey"
  - "r/AnimalsBeingGeniuses / r/Catculations / r/Catswithjobs"
audio_track: public/audio/stems/karma_comedy_master.mp3
audio_source: "Monkeys Spinning Monkeys - Kevin MacLeod (pr42azVZi3o, 22.49M views)"
audio_bg_volume: 0.11
compositor: src/remotion/MrPurifiedWaterShort.tsx
cue_sheet: cue_sheet_pets_being_smart.json
---

# Sub-Category Skill: `pets_being_smart` ("200 IQ Smart Pet Moments / Genius Edition")

> **MANDATORY FOR AI PIPELINE:** Every rule below is verified through multi-platform sourcing and `1fps`/`2fps` visual QA. Follow every step without shortcuts.

---

## 1. Core Narrative & Audio Philosophy
1. **Full Story Preservation (`7.2s – 8.6s` per clip):**
   - Every smart pet clip MUST show the **obstacle/problem (CAUSE)**, the **clever unlock/solution (PAYOFF)**, and the **aftermath/exit/closing behind itself (REACTION)** without cutting early.
2. **Unobstructed Visuals:**
   - Do **NOT** add white flashes, zoom-shakes, or text popups over the pet—let the animal's problem-solving and body language carry the video.
3. **Very Low-Volume Trending Comedy Bed (`0.11` under `1.0` Natural Audio):**
   - Mix `public/audio/stems/karma_comedy_master.mp3` at **`volume: 0.11`** underneath **`100%` natural clip audio** (door clicks, paws, owner reactions) so real audio stays crisp and audible. For silent source clips (e.g., `r_1wgm133ae5f41`), inject silent `48000 Hz` stereo audio via `anullsrc` during trimming.

---

## 2. Step-by-Step Production Pipeline

### Step 1: Isolated Directories (`pets_being_smart`)
- `temp_harvest/pets_being_smart/`
- `public/clips/pets_being_smart/`
- `cue_sheet_pets_being_smart.json`
- `output/pets_being_smart_raw.mp4`
- `output/pets_being_smart_mastered.mp4`
- `output/pets_being_smart_qa_sheet.jpg`
- `output/pets_being_smart_upload_metadata.json`

### Step 2: Multi-Platform Sourcing
1. **Reddit (`agent-reach reddit search` + `v.redd.it` HLS bypass):**
   - Queries: `"smart dog opens door v.redd.it"`, `"cat opens door handle v.redd.it"`, `"smart dog saves v.redd.it"`, `"cat solves puzzle v.redd.it"`, `"dog opens fridge v.redd.it"`, `"smart cat steals v.redd.it"`.
   - Download `v.redd.it/<id>` via `py -3 -m yt_dlp -o "temp_harvest/pets_being_smart/r_<id>.%(ext)s" "https://v.redd.it/<id>/HLSPlaylist.m3u8"`.
2. **YouTube Shorts (`yt-dlp --js-runtimes node`):**
   - Queries (`5s <= dur <= 30s`, `views >= 15,000`): `"smart cat opens door handle #shorts"`, `"200 iq dog moments #shorts"`, `"smart dog tricks owner #shorts"`, `"genius cat caught on camera #shorts"`, `"smart dog opens door"`, `"cat opens door handle"`.

### Step 3: Mandatory `2fps` Visual Inspection & Rejection Gate
Generate `2fps` contact sheets (`fps=2,scale=260:-1,tile=8x10`) for every candidate and inspect visually:
- **Rejected Candidates:**
  - `yt_IGldIqSpel0`: Rejected due to `"Tommy the Cat"` watermark and `"chicken would be nice"` bottom text overlay.
  - `r_o53nenfnvqp81`: Rejected due to large yellow/white baked-in narration caption bars.
  - `r_e4ns67v0ur8b1`: Rejected due to Chinese Weibo watermark in top-right corner.
  - `r_cnn0n49ecwp71`: Rejected due to bottom-right creator watermark.
  - `yt_tUm41XsYKm4`: Rejected because cat fails to open the door (missing payoff).
  - `r_93urx3ael0k31`: Rejected as too dark and slow (`63.26s`).

### Step 4: Clip Trimming & `cue_sheet_pets_being_smart.json`
Trim all 5 ranked clips (`Rank 5 [Level 1]` up to `Rank 1 [Level 5]`) at `30 fps`, `yuv420p`, `aac 192k`, `48000 Hz`. For `10–12s` stories, apply `setpts=PTS/<spd>` and `atempo=<spd>` (`1.25–1.35`) so the full story fits cleanly in `7–8.6s`.

### Step 5: Remotion Render, Loudness Master & `1fps` Final QA
1. Render: `npx remotion render RankingShort output/pets_being_smart_raw.mp4 --props=cue_sheet_pets_being_smart.json --overwrite`
2. Master: `ffmpeg -i output/pets_being_smart_raw.mp4 -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:v copy -c:a aac -b:a 320k -y output/pets_being_smart_mastered.mp4`
3. Verify `ebur128=peak=true` loudness (`-14.0 ± 1.0 LUFS`, True Peak `<= -1.5 dBTP`).
4. Generate `1fps` `output/pets_being_smart_qa_sheet.jpg` (`fps=1,scale=240:-1,tile=7x7`) and inspect visually for 0 black frames and 100% complete stories.

---

## 3. Proven 5-Clip Benchmark Mapping
| Rank | Source ID | Trim Start | Speed | Out Duration (`frames`) | Complete Verified Story Arc |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `5 [Level 1]` | `yt_oKNc948aC_M` (`YouTube`) | `12.50s` (`9.0s` src) | `1.25x` | `7.21s` (`216f`) | Boxer outside French door jumps up, pulls lever handle down, swings door open, walks inside |
| `4 [Level 2]` | `yt_LRyJ6tn3RwY` (`YouTube`) | `3.50s` (`11.5s` src) | `1.35x` | `8.53s` (`255f`) | Dog enters through front door, turns around, and nudges the door shut behind himself |
| `3 [Level 3]` | `r_1wgm133ae5f41` (`Reddit`) | `1.50s` (`10.5s` src) | `1.30x` | `8.07s` (`242f`) | Cat in sweater outsmarts green slow-feeder puzzle bowl by flipping it upside down to eat |
| `2 [Level 4]` | `yt_u_T29QcphRg` (`YouTube`) | `6.50s` (`8.5s` src) | `1.00x` | `8.53s` (`255f`) | Black cat on cabinet eyes door handle, leaps mid-air onto lever, opens door, walks out |
| `1 [Level 5]` | `r_jexr4vpdcak71` (`Reddit`) | `0.00s` (`8.3s` src) | `1.00x` | `8.30s` (`249f`) | White cat opens kitchen drawer, snatches dried fish, pulls back in, and closes drawer |
