# Viral Compilation Pipeline — Complete Architecture & SOP

This document is the master engineering write-up for the 10-niche / 50-subcategory viral ranking compilation pipeline (`@MrPurifiedWater` + `@cliportey` hybrid architecture).

---

## 1. Directory & File Map
- **`subcategory_skills/`** — Execution-ready production skill files, one per `subCategoryId`:
  - [`README.md`](./README.md) — Index of all sub-category skill files.
  - [`PIPELINE_ARCHITECTURE.md`](./PIPELINE_ARCHITECTURE.md) — This master SOP & architecture guide.
  - [`people_accepting_fate.md`](./people_accepting_fate.md) — Verified skill for **"THIS IS THE END"** (`people_accepting_fate`).
- **`src/pipeline/master_category_registry.json`** — Master taxonomy of all 10 niches and 50 sub-categories.
- **`src/remotion/MrPurifiedWaterShort.tsx`** — Main `1080x1920 @ 30fps` Remotion compositor (`RankingShort`).
- **`scripts/prepare_this_is_the_end.py`** — Frame-verified trimmer, freeze-frame extractor, and `cue_sheet.json` builder.
- **`scripts/auto_daemon.py`** — Automated pipeline orchestrator (reads `subcategory_skills/<sub_id>.md` when available).
- **`scripts/yt_researcher.py`** — YouTube research integration via `agent-reach youtube search/read`.
- **`public/audio/stems/`** — Pre-cut, silence-trimmed signature audio hooks (e.g., `skyfall_this_is_the_end.mp3` @ `2.976s` / `90 frames`).
- **`public/clips/`** — Trimmed `30fps` clips (`*_trimmed.mp4`) and extracted freeze frames (`*_freeze.jpg`).
- **`output/`** — Raw render (`raw_render.mp4`), mastered deliverables (`this_is_the_end_mastered.mp4`, `mastered_final.mp4`), and QA contact sheets (`qa_final_sheet.jpg`).

---

## 2. End-to-End 7-Stage Production Workflow

### Stage 1: Reference Dissection & Stem Engineering
1. Download viral reference Shorts via `py -3 -m yt_dlp --js-runtimes node`.
2. **Unique Category-Matched Music Rule:** NEVER reuse the same background track across different categories. Source a fresh, category-matched trending track for each new sub-category (e.g., *Wii Shop* / *Coconut Mall* / *Fluffing a Duck* / *Sneaky Snitch* / upbeat sports/comedy groove) and mix at **`volume: 0.11`** underneath `100%` natural clip audio (unless the category uses a freeze-frame vocal hook like `people_accepting_fate`).
3. Generate a `2fps` contact sheet (`fps=2,scale=270:-1,tile=10x7`) to dissect:
   - Buildup vs. cause vs. freeze/punchline timing.
   - Audio behavior (natural audio during buildup, instant cut on freeze, full signature hook playback).
   - Typography placement & styling (no giant opaque boxes covering the subject).
3. Inspect the signature audio stem with `silencedetect` and `volumedetect` per `0.25s` window:
   - Trim leading silence (`-ss 0.13`) and add a smooth tail fade (`afade=t=out`).
   - Compute `stem_frames = ceil(stem_duration_sec * 30)`.
   - **Rule:** `freezeDurationFrames` **MUST BE `>= stem_frames`** (e.g., `90 frames` / `3.00s` for `2.976s` Skyfall) so the final word (`"END"`) is never clipped.

### Stage 2: Candidate Sourcing
- Query YouTube via `py -3 -m yt_dlp --js-runtimes node --flat-playlist --dump-json` for **real-life camera footage** (`4s <= duration <= 35s`, `views >= 50,000`).
- Reject gaming, Roblox, anime, ads, news broadcasts, and compilation re-uploads at metadata stage.

### Stage 3: Strict Visual Rejection Gate (`2fps` Contact Sheet)
- Generate `temp_harvest/sheet_<id>.jpg` (`fps=2,scale=260:-1,tile=8x10`) for every downloaded clip.
- Reject immediately if any clip has:
  - TikTok, FailBlog, news, or creator watermarks/logos.
  - Pre-edited meme/math/caption overlays.
  - Blurry letterboxed sidebars (clean 9:16-in-16:9 black pillarbox is cropped with `-vf "crop=ih*9/16:ih"`).
  - Unreadable dark footage or severe/fatal injury.
  - Missing **Buildup ➔ Cause (`T_cause`) ➔ Climax/Surrender (`T_freeze`)** arc.

### Stage 4: Precision Timing (`5fps` Fine Strip)
- Extract `temp_harvest/fine_<id>.jpg` (`fps=5`, `0.2s` per tile) around `[T_cause - 0.5s, T_cause + 1.0s]`.
- Pinpoint:
  - `T_freeze_abs`: `0.30s – 0.80s` **after** `T_cause` (never before `T_cause`).
  - `trim_start`: `2.60s – 3.60s` before `T_freeze_abs`.
  - `freeze_offset = round((T_freeze_abs - trim_start) * 30)`.
  - `freeze_duration = max(90, stem_frames)`.
  - `duration_frames = freeze_offset + freeze_duration`.

### Stage 5: Clip Trimming, Freeze Extraction & Cue Sheet
- Trim each clip to `30fps`, `yuv420p`, `aac 192k`, `48000 Hz`.
- Extract `public/clips/<id>_freeze.jpg` at `freeze_offset / 30.0` seconds and visually verify all 5 freeze images before rendering.
- Write `cue_sheet.json` with `videoPath`, `freezeImagePath`, `durationInFrames`, `freezeFrameOffset`, `freezeDurationFrames`, `punchlineText`, and `audioHookPath`.

### Stage 6: Remotion Compositing (`MrPurifiedWaterShort.tsx`)
- Render `RankingShort` with `--props=cue_sheet.json`:
  - `240px` black 3-line header (`Ranking Best Of` / `<Subject>` / `<Version Tag>`).
  - Bottom-up ladder (`5. [Level 1]` ➔ `1. [Level 5]`).
  - Foreground card uses `width: '100%'`, `maxWidth: '1040px'`, `maxHeight: '1400px'`, `objectFit: 'contain'`.
  - **True Freeze Swap:** `<OffthreadVideo>` plays during `0 .. freezeOffset - 1`; `<Img src={freezeImgSrc} />` renders solid during `freezeOffset .. durationInFrames - 1` with `1.03 -> 1.09` zoom and `grayscale(35%) contrast(1.12) brightness(0.92)`, cutting clip audio to `0.0`.
  - `LevelZero0ne` circular Mew watermark + `75-frame` (`2.5s`) Earshot sonic-branded outro.

### Stage 7: Loudness Mastering & Final QA
1. Master audio via FFmpeg:
   ```powershell
   ffmpeg -i output/raw_render.mp4 -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:v copy -c:a aac -b:a 320k -y output/this_is_the_end_mastered.mp4
   ```
2. Verify integrated loudness via `ebur128=peak=true` (target `-14.0 ± 1.0 LUFS`, True Peak `<= -1.5 dBTP`).
3. Extract `output/qa_final_sheet.jpg` (`fps=1`, full video) and verify:
   - `0` black frames or unplanned white frames.
   - Full card width, zero watermarks, zero pillarbox bars.
   - Every freeze occurs **after** `T_cause` and holds long enough for the full audio hook.

---

## 3. Template for New Sub-Category Skill Files
Every new sub-category added to `subcategory_skills/<sub_category_id>.md` must include:
1. **YAML Frontmatter:** `sub_category_id`, `sub_category_name`, `niche`, `references`, `audio_stem`, `audio_stem_frames_30fps`, `compositor`.
2. **Core Narrative & 3-Beat Causal Arc:** Exact `T_cause` -> `T_trigger` rule.
3. **Audio Stem Profile:** Leading silence trim, fade-out, and minimum `freeze_duration` / `climax_duration`.
4. **Visual Rejection Criteria:** Specific watermarks, overlays, and framing disqualifiers.
5. **Typography & Visual Effect Sync:** Exact frame offsets for kinetic text and camera/filter effects.
6. **Proven Benchmark Table:** At least 1 verified 5-clip run with exact `trim_start`, `duration_frames`, and `freeze_offset` values.
