# Sub-Category Skill: `athletes_celebrating_too_early`

## Header & Composition Config
- **Composition:** `RankingShort` (`src/remotion/MrPurifiedWaterShort.tsx`)
- **Cue Sheet:** `cue_sheet_athletes_celebrating_too_early.json`
- **titleHeader:** `Ranking Best Of`
- **subjectHeader:** `Premature Celebrations`
- **versionTag:** `(Too Early Edition)`
- **subCategoryId:** `athletes_celebrating_too_early`
- **subCategoryName:** `CELEBRATING TOO EARLY`
- **globalAudioPath:** `public/audio/stems/karma_comedy_master.mp3`

## Sourcing & Visual QA Process
1. **Reddit (`agent-reach reddit search`):** Searched `"premature celebration v.redd.it"` and `"Prematurecelebration v.redd.it"`. Downloaded 7 `v.redd.it` candidates via `yt-dlp` HLSPlaylist.
2. **YouTube Shorts (`yt-dlp --flat-playlist`):** Searched `"runner celebrates too early loses #shorts"`, `"cyclist celebrates too early #shorts"`, `"soccer goalie celebrates too early #shorts"`, `"mma fighter celebrates too early #shorts"`, and additional sports queries. Downloaded 8 candidates.
3. **2fps Visual QA:** Generated `8x10` contact sheets (`fps=2,scale=260:-1`) for all 15 candidates and inspected every sheet with `read_file`.
   - Rejected `r_6n6g7w9rl6d21` (`Videoholic` watermark), `yt_38fffcRexi4` (baked-in news banner), `yt_3wd9jA8ovo4` (baked-in text + `@THE BUZZER`), `yt_lMQ-lwTi7WU` & `yt_oFYRyDW2oj0` (`The Guardian` watermark), `yt_yGcTCJxnQuI` (`COMPFUSED.COM` watermark), and `r_nsmedznmodbh1` (TikTok text overlays & red circles).
4. **Full-Story Trimming (30fps, yuv420p, AAC 192k 48000Hz):**
   - Preserved full **Cause (early celebration) -> Payoff (overtaken/scored on) -> Reaction** for all 5 clips.
   - Added silent `anullsrc` stereo 48kHz audio track to `clip_5.mp4` (source had no audio stream).
   - Sped up `clip_1.mp4` (`1.25x` via `setpts=PTS/1.25`, `atempo=1.25`) from `10.5s` source (`8.0s–18.5s`, cleanly before `@THE BUZZER` outro) to `8.43s` (`252` frames).
   - Scaled `clip_3.mp4` from 1080p to `1280x720` and rendered with `--concurrency=2` to prevent Remotion OffthreadVideo compositor OOM.
5. **Mastering & 1fps Final QA:**
   - Mastered with `loudnorm=I=-14:TP=-1.5:LRA=11` (`aac -b:a 320k`).
   - Measured EBU R128 loudness: **Integrated `-13.4 LUFS`**, **LRA `8.6 LU`**, **True Peak `-1.3 dBFS`**.
   - Verified `output/athletes_celebrating_too_early_qa_sheet.jpg` (1fps): 0 black frames, 0 watermarks, 100% complete stories.

## 5-Clip Benchmark Table

| Rank | Level | Clip File | Source | Trim Window | Speed | Duration | Frames | Story Beat (Cause -> Payoff -> Reaction) |
| :--- | :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **5** | 1 | `public/clips/athletes_celebrating_too_early/clip_5.mp4` | `v.redd.it/4l1lqlyiets81` | `0.0s – 7.0s` | `1.0x` | `7.00s` | `210` | Volleyball team celebrates in group hug -> opponent kicks ball back over net -> point lost |
| **4** | 2 | `public/clips/athletes_celebrating_too_early/clip_4.mp4` | `v.redd.it/7a23ned9a4ge1` | `2.5s – 10.9s` | `1.0x` | `8.40s` | `252` | Dirt track runner raises arms to celebrate -> trips & faceplants -> rivals sprint past |
| **3** | 3 | `public/clips/athletes_celebrating_too_early/clip_3.mp4` | `youtube.com/watch?v=aFyk_aReMLs` | `4.5s – 13.5s` | `1.0x` | `9.00s` | `270` | Pro road cyclist raises both arms before pink finish line -> two sprinters pass him |
| **2** | 4 | `public/clips/athletes_celebrating_too_early/clip_2.mp4` | `youtube.com/watch?v=W32EJrhIffg` | `0.0s – 9.5s` | `1.0x` | `9.50s` | `285` | Soccer goalie saves penalty and runs away celebrating -> ball spins back into open net |
| **1** | 5 | `public/clips/athletes_celebrating_too_early/clip_1.mp4` | `youtube.com/watch?v=vWa9iYYPYF4` | `8.0s – 18.5s` | `1.25x` | `8.43s` | `252` | Oregon runner waves to crowd -> Washington rival passes at the tape -> lies on track in disbelief |
