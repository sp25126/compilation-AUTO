---
sub_category_id: instant_karma
sub_category_name: INSTANT KARMA
niche: instant_karma
references:
  - "@MrPurifiedWater (ref_videos/ref_karma.webm, ref_videos/ref_karma_audio.mp3, ref_videos/karma_sheet.jpg)"
  - "@cliportey"
audio_track: public/audio/stems/karma_comedy_master.mp3
audio_source: "Monkeys Spinning Monkeys - Kevin MacLeod (pr42azVZi3o, 22.49M views)"
audio_bg_volume: 0.11
compositor: src/remotion/MrPurifiedWaterShort.tsx
prep_script: scripts/prepare_instant_karma.py
sourcing_script: scripts/source_karma_clips.py
metadata_script: scripts/yt_researcher.py
---

# Sub-Category Skill: `instant_karma` ("Instant Karma Moments")

> **MANDATORY FOR AI PIPELINE:** Every rule in this file was learned and verified directly by dissecting `@MrPurifiedWater` (`ref_karma.webm` / `ref_karma_audio.mp3`) and running multi-iteration visual & audio QA. Follow every step below without shortcuts.

---

## 1. Core Lessons & Hard Rules (What NOT to Do vs. What Works)
1. **NEVER cover or interrupt the action:**
   - Do **NOT** add `INSTANT KARMA` text popups, white impact flashes, or snap-zooms over the action—they obscure the cause and ruin comedic timing.
2. **NEVER cut off the setup or the payoff:**
   - If a clip's full story takes `11s–13.5s` (e.g., scare ➔ fall ➔ panic ➔ laugh), **keep the entire story** and apply clean FFmpeg speed-up (`1.25x–1.40x` via `setpts=PTS/<spd>` and `atempo=<spd>`) rather than chopping off the beginning (`T_cause`) or the ending (`T_reaction`).
3. **Music Vibe & Volume (`0.11` Comedy Bed under `1.0` Natural Audio):**
   - `@MrPurifiedWater`'s `ref_karma_audio.mp3` has `mean_rms = 0.2123` (light, playful comedy groove underneath natural clip audio—**NOT** heavy dark phonk).
   - Use [`karma_comedy_master.mp3`](../public/audio/stems/karma_comedy_master.mp3) (*Monkeys Spinning Monkeys*) at **`volume: 0.11`** so the trending background music adds subtle viral energy while **`100%` natural clip audio (`volume: 1.0`)**—horns, slaps, crowd cheers, crashes, and splashes—remains loud and crystal clear.

---

## 2. Step-by-Step Production Pipeline

### Step 1: Clean Slate
Before starting a new `instant_karma` compilation, delete stale files from:
- `output/*`
- `public/clips/*`
- `temp_harvest/*`

### Step 2: Reference & Audio Bed Preparation
1. **Reference Inspection (`ref_videos/ref_karma.webm`):**
   - `1080x1920`, `30 fps`, `38.67s`. Clips run `5s–9s` each so the full provocation/arrogance is clear before payback.
2. **Trending Comedy Background Bed (`karma_comedy_master.mp3`):**
   - Download `pr42azVZi3o` (*Monkeys Spinning Monkeys*, `22.49M` views):
     ```powershell
     py -3 -m yt_dlp --js-runtimes node -x --audio-format mp3 --audio-quality 192K -o "public/audio/stems/karma_comedy_bed.%(ext)s" "https://www.youtube.com/watch?v=pr42azVZi3o"
     ```
   - Cut a `50.0s` bed with smooth fade-in and fade-out:
     ```powershell
     ffmpeg -y -ss 0.0 -t 50.0 -i public/audio/stems/karma_comedy_bed.mp3 -af "afade=t=in:st=0:d=0.2,afade=t=out:st=48.5:d=1.5" -ar 48000 -b:a 192k public/audio/stems/karma_comedy_master.mp3
     ```

### Step 3: Multi-Platform Candidate Sourcing (Reddit, TikTok, Instagram, YouTube)
1. **Reddit (`agent-reach reddit search` + `v.redd.it` HLS bypass):**
   - `reddit.com` post URLs return HTTP 403 in `yt-dlp` without cookies, so search via `agent-reach reddit search "<query> v.redd.it"` (`r/instantkarma`, `r/ConvenientCop`, `r/Instant_Regret`, `r/Whatcouldgowrong`) and download the `v.redd.it/<id>` HLS stream directly:
     ```powershell
     py -3 -m yt_dlp -o "temp_harvest/karma_r.%(ext)s" "https://v.redd.it/<id>/HLSPlaylist.m3u8"
     ```
2. **TikTok, Instagram & YouTube Shorts (`yt-dlp --js-runtimes node`):**
   - Search with `--flat-playlist --dump-json` for real-life camera clips (`5s <= dur <= 35s`, `views >= 10,000`):
     - `celebrating too early fail #shorts`
     - `instant karma kicking fence #shorts`
     - `prank backfire instant karma #shorts`
     - `air horn prank goes wrong`
   - Download candidates to `temp_harvest/` with `bv*[height<=1080]+ba/b[height<=1080]/b --merge-output-format mp4`.

### Step 4: Two-Stage Visual Inspection & Rejection Gate
1. **Generate `2fps` (`0.5s` per tile) & `1fps` Contact Sheets:**
   ```powershell
   ffmpeg -y -i temp_harvest/<file>.mp4 -vf "fps=2,scale=260:-1,tile=8x10" -frames:v 1 -q:v 3 temp_harvest/sheet_<id>.jpg
   ```
2. **Strict Rejection Criteria (Learned from Rejected Candidates):**
   - **Watermarks / Broadcast Banners:** Reject `MMA TV` (`DciQj3EEjo0`), `CBSN` (`seh2ft_n4dQ`), `@THE BUZZER` (`3wd9jA8ovo4`, `38fffcRexi4`), and `Please subscribe!` overlays (`oTQ_PpTnOsA`).
   - **Long Text Intros / Too Dark:** Reject clips with 10s black text intros (`jXTGn-8jjhs`) or dark/unreadable night scenes (`karma_r1`).
   - **Truncated Source Uploads:** Always verify via `ffprobe` and `1fps` sheet that the **full ending is actually in the source file** (e.g., `3PdQpH-dezs` was `12.56s` and cut off *before* the wall slammed down, so we rejected it and sourced `6yCia4DGigs` `14.0s` which contains the complete concrete slab slam onto his leg).

### Step 5: Story-Preserving Trimming & `cue_sheet.json` (`scripts/prepare_instant_karma.py`)
Trim all 5 ranked clips (`rank 5 [Level 1]` up to `rank 1 [Level 5]`) at `30 fps`, `yuv420p`, `aac 192k`, `48000 Hz`:
- Apply `-vf "setpts=PTS/<spd>" -af "atempo=<spd>"` only when a full story exceeds `10.5s` (`1.40x` for `13.5s -> 9.64s`, `1.25x` for `11.0s -> 8.80s`).
- Write `cue_sheet.json`:
  - `titleHeader`: `"Ranking Best Of"`
  - `subjectHeader`: `"Instant Karma Moments"`
  - `versionTag`: `"(Caught On Camera)"`
  - `globalAudioPath`: `"public/audio/stems/karma_comedy_master.mp3"`
  - `clips`: `[ { id, videoPath, durationInFrames }, ... ]` (no `freezeFrameOffset`, no `impactFrameOffset`, no `punchlineText`).

### Step 6: Remotion Compositing (`src/remotion/MrPurifiedWaterShort.tsx`)
- `globalAudioSrc` plays at `volume={0.11}` from `0` to `totalClipsDuration`.
- Each clip's `<OffthreadVideo>` plays at `volume = 1.0` with `width: '100%'`, `maxHeight: '1400px'`, `objectFit: 'contain'` over a blurred ambient background.
- `240px` black 3-line header + bottom-up `5. [Level 1]` ➔ `1. [Level 5]` ladder + `LevelZero0ne` Mew watermark + `75-frame` (`2.5s`) Earshot sonic-branded outro.

### Step 7: Render, Loudness Master & Full-Video Visual QA
1. **Render:**
   ```powershell
   npx remotion render RankingShort output/raw_render.mp4 --props=cue_sheet.json --overwrite
   ```
2. **Loudness Master:**
   ```powershell
   ffmpeg -i output/raw_render.mp4 -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:v copy -c:a aac -b:a 320k -y output/instant_karma_mastered.mp4
   Copy-Item -Force output\instant_karma_mastered.mp4 output\mastered_final.mp4
   ```
3. **Verify Loudness & `1fps` Full-Video QA Contact Sheet:**
   ```powershell
   ffmpeg -i output/instant_karma_mastered.mp4 -filter_complex "ebur128=peak=true" -f null NUL
   ffmpeg -y -i output/instant_karma_mastered.mp4 -vf "fps=1,scale=240:-1,tile=7x7" -frames:v 1 -q:v 3 output/qa_final_sheet.jpg
   ```
4. Read `output/qa_final_sheet.jpg` and confirm: `0` black frames, full cause + payoff + aftermath visible in every level, and clean outro.

### Step 8: YouTube Upload Metadata & Owner Credit (`scripts/yt_researcher.py`)
Run:
```powershell
py -3 scripts/yt_researcher.py --metadata instant_karma
```
Generates `output/upload_metadata.json` with:
- **Title with Hashtags:** `Ranking Best Of Instant Karma Moments 😂💀 #shorts #funny #instantkarma`
- **Description:** Hook + engagement question + owner-credit disclaimer (`"All footages used in this video are not mine; full credit goes to the respective owners."`) + trending Shorts tags (`#shorts #viral #trending #fyp #funny #instantkarma #fails #memes #youtubeshorts #comedy #karma #viralvideo #explore #ytshorts #trendingshorts #laugh #trynottolaugh #ranking`).
- **Upload Schedule:** `7:30 PM IST` (`9:00 AM EST`) primary; `3:30 AM IST` (`5:00 PM EST`) US evening peak.

---

## 3. Proven 5-Clip Benchmark Mapping
| Rank | Source ID | `trim_start` | Source Window | Speed | Out Frames / Dur | Complete Verified Story Arc |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `5 [Level 1]` | `cg20EMKejEE` | `0.00s` | `13.50s` | `1.40x` | `289f` (`9.64s`) | Scare attempt ➔ guy falls & plays dead ➔ costume wearer panics ➔ guy jumps up laughing |
| `4 [Level 2]` | `vWa9iYYPYF4` | `10.50s` | `9.00s` | `1.00x` | `270f` (`9.00s`) | Oregon runner raises arms celebrating early ➔ rival passes at finish line ➔ collapses on track |
| `3 [Level 3]` | `FtdcQt4qCIg` | `0.00s` | `11.00s` | `1.25x` | `264f` (`8.80s`) | Blows red air horn behind man ➔ man confronts him ➔ instant slap |
| `2 [Level 4]` | `6yCia4DGigs` | `3.00s` | `9.50s` | `1.00x` | `285f` (`9.50s`) | Kicks concrete fence ➔ upper concrete slab slams straight down & traps his leg |
| `1 [Level 5]` | `ch6HmvHtV7M` | `1.00s` | `7.50s` | `1.00x` | `225f` (`7.50s`) | Blasts air horn on bridge ➔ picked up ➔ tossed over railing into river + splash |
