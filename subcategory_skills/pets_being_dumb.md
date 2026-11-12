---
sub_category_id: pets_being_dumb
sub_category_name: PETS BEING DUMB
niche: funny_animals
references:
  - "@MrPurifiedWater"
  - "r/AnimalsBeingDerps / r/Catculations / r/OneOrangeBraincell"
audio_track: public/audio/stems/karma_comedy_master.mp3
audio_source: "Monkeys Spinning Monkeys - Kevin MacLeod (pr42azVZi3o, 22.49M views)"
audio_bg_volume: 0.11
compositor: src/remotion/MrPurifiedWaterShort.tsx
prep_script: scripts/prepare_pets_being_dumb.py
metadata_script: scripts/yt_researcher.py
---

# Sub-Category Skill: `pets_being_dumb` ("Pets Being Dumb / 0 Braincells")

> **MANDATORY FOR AI PIPELINE:** Every rule below is verified through multi-platform sourcing and `1fps`/`2fps` visual QA. Follow every step without shortcuts.

---

## 1. Core Narrative & Audio Philosophy
1. **Full Story Preservation (`5.5s – 8.5s` per clip):**
   - Every pet clip MUST show the **setup/miscalculation (CAUSE)**, the **derpy fail/brain-freeze/crash (PAYOFF)**, and the **pet or owner reaction (AFTERMATH)** without cutting early.
2. **Unobstructed Visuals:**
   - Do **NOT** add flashes, zoom-shakes, or text popups over the pet—let the animal's expression and body language carry the comedy.
3. **Very Low-Volume Trending Comedy Bed (`0.11` under `1.0` Natural Audio):**
   - Mix [`karma_comedy_master.mp3`](../public/audio/stems/karma_comedy_master.mp3) (*Monkeys Spinning Monkeys*) at **`volume: 0.11`** underneath **`100%` natural clip audio** (meows, glass shatter, owner laughter) so real audio stays crisp and audible.

---

## 2. Step-by-Step Production Pipeline

### Step 1: Clean Slate
Before starting a new `pets_being_dumb` compilation, clear stale files from:
- `output/*`
- `public/clips/*`
- `temp_harvest/*`

### Step 2: Multi-Platform Sourcing (Reddit, TikTok, Instagram, YouTube)
1. **Reddit (`agent-reach reddit search` + `v.redd.it` HLS bypass):**
   - Query `r/AnimalsBeingDerps`, `r/Catculations`, `r/OneOrangeBraincell`:
     ```powershell
     agent-reach reddit search "cat jump fail miscalculation v.redd.it" --limit 6
     agent-reach reddit search "dog glass door derp v.redd.it" --limit 6
     ```
   - Download `v.redd.it/<id>` directly via its HLS playlist (bypasses Reddit 403):
     ```powershell
     py -3 -m yt_dlp -o "temp_harvest/pet_r.%(ext)s" "https://v.redd.it/<id>/HLSPlaylist.m3u8"
     ```
2. **YouTube / TikTok / Instagram Shorts (`yt-dlp --js-runtimes node`):**
   - Search with `--flat-playlist --dump-json` (`4s <= dur <= 25s`, `views >= 15,000`):
     - `cat jump fail off table #shorts`
     - `dog runs into glass door #shorts`
     - `cat brain freeze ice cream #shorts`
     - `dog fails to catch treat #shorts`
     - `cat slips in bathtub #shorts`
   - Download candidates to `temp_harvest/` with `bv*[height<=1080]+ba/b[height<=1080]/b --merge-output-format mp4`.

### Step 3: Two-Stage Visual Inspection & Rejection Gate
1. **Generate `2fps` (`0.5s` per tile) Contact Sheets:**
   ```powershell
   ffmpeg -y -i temp_harvest/<file>.mp4 -vf "fps=2,scale=260:-1,tile=8x10" -frames:v 1 -q:v 3 temp_harvest/sheet_<id>.jpg
   ```
2. **Strict Rejection Criteria (Learned from Rejected Candidates):**
   - **TikTok / Creator Watermarks:** Reject `m99fqrkpfjf81` and `ba4xgblqce4a1`.
   - **Baked-in Math / Meme Overlays:** Reject `ew6zpphmys131` and `tvl8b0lewzv21` (baked-in geometry/math equations).
   - **Duplicate Concepts:** Avoid two "invisible glass door" clips in the same 5-clip ranking; keep only the cleanest one (`s37dl15ourq71`, zero text overlay).
   - **Too Small / Wide Action:** Reject `0H25ve3qts4` (cat too small in wide bakery shot).
   - **Ensure Variety Across Levels 1–5:** Mix cats and dogs across distinct comedy beats (table roll, invisible door, jump miss, brain freeze, glass table smash).

### Step 4: Clip Trimming & `cue_sheet.json` (`scripts/prepare_pets_being_dumb.py`)
Trim all 5 ranked clips (`rank 5 [Level 1]` up to `rank 1 [Level 5]`) at `30 fps`, `yuv420p`, `aac 192k`, `48000 Hz`:
- Write `cue_sheet.json` with:
  - `titleHeader`: `"Ranking Best Of"`
  - `subjectHeader`: `"Pets Being Dumb Moments"`
  - `versionTag`: `"(0 Braincells Edition)"`
  - `globalAudioPath`: `"public/audio/stems/karma_comedy_master.mp3"`
  - `clips`: `[ { id, videoPath, durationInFrames }, ... ]`

### Step 5: Remotion Compositing (`src/remotion/MrPurifiedWaterShort.tsx`)
- `globalAudioSrc` plays at `volume={0.11}` from `0` to `totalClipsDuration`.
- Each clip's `<OffthreadVideo>` plays at `volume = 1.0` with `width: '100%'`, `maxHeight: '1400px'`, `objectFit: 'contain'` over a blurred ambient background.
- `240px` black 3-line header + bottom-up `5. [Level 1]` ➔ `1. [Level 5]` ladder + `LevelZero0ne` Mew watermark + `75-frame` (`2.5s`) Earshot sonic-branded outro.

### Step 6: Render, Loudness Master & Full-Video Visual QA
1. **Render:**
   ```powershell
   npx remotion render RankingShort output/raw_render.mp4 --props=cue_sheet.json --overwrite
   ```
2. **Loudness Master (`-14.0 ± 1.0 LUFS`, True Peak `<= -1.5 dBTP`):**
   ```powershell
   ffmpeg -i output/raw_render.mp4 -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:v copy -c:a aac -b:a 320k -y output/pets_being_dumb_mastered.mp4
   Copy-Item -Force output\pets_being_dumb_mastered.mp4 output\mastered_final.mp4
   ```
3. **Verify Loudness & `1fps` Full-Video QA Contact Sheet:**
   ```powershell
   ffmpeg -i output/pets_being_dumb_mastered.mp4 -filter_complex "ebur128=peak=true" -f null NUL
   ffmpeg -y -i output/pets_being_dumb_mastered.mp4 -vf "fps=1,scale=240:-1,tile=7x6" -frames:v 1 -q:v 3 output/qa_final_sheet.jpg
   ```
4. Read `output/qa_final_sheet.jpg` and confirm: `0` black frames, full story visible on all 5 ranks, and clean `LevelZero0ne` outro.

### Step 7: YouTube Upload Metadata & Owner Credit (`scripts/yt_researcher.py`)
Run:
```powershell
py -3 scripts/yt_researcher.py --metadata pets_being_dumb
```
Generates `output/upload_metadata.json` with:
- **Title with Hashtags:** `Ranking Funniest Pets Sharing 0 Braincells 😂🐾 #shorts #pets #funnyanimals`
- **Description:** Hook + engagement question + owner-credit disclaimer (`"All footages used in this video are not mine; full credit goes to the respective owners."`) + trending Shorts tags.
- **Category:** `Pets & Animals`
- **Upload Schedule:** `7:30 PM IST` (`9:00 AM EST`) primary; `3:30 AM IST` (`5:00 PM EST`) US evening peak.

---

## 3. Proven 5-Clip Benchmark Mapping
| Rank | Source ID | `trim_start` | Duration (`frames`) | Complete Verified Story Arc |
| :--- | :--- | :--- | :--- | :--- |
| `5 [Level 1]` | `wJMveFiz57A` | `1.50s` | `5.50s` (`165f`) | Cat stretches lazily on table edge ➔ rolls straight off onto floor |
| `4 [Level 2]` | `s37dl15ourq71` (`Reddit`) | `6.00s` | `8.00s` (`240f`) | Golden retriever stuck in open glass door ➔ owner "opens" invisible door ➔ walks in |
| `3 [Level 3]` | `5pmp33azi0da1` (`Reddit`) | `0.00s` | `8.50s` (`255f`) | Orange kitten hops on bed ➔ launches full-send off bed missing mirror |
| `2 [Level 4]` | `QE-T_kikIKI` | `0.00s` | `8.50s` (`255f`) | Cat licks ice cream cone ➔ instant wide-eyed open-mouth brain freeze |
| `1 [Level 5]` | `7AXzLdttiUY` | `6.50s` | `7.00s` (`210f`) | Owner walks in ➔ excited Doberman leaps straight through glass coffee table |
