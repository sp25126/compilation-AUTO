# Sub-Category Skill: `adults_humbled_by_kids`

## Header & Composition Config
- **Composition:** `RankingShort` (`src/remotion/MrPurifiedWaterShort.tsx`)
- **Cue Sheet:** `cue_sheet_adults_humbled_by_kids.json`
- **titleHeader:** `Ranking Best Of`
- **subjectHeader:** `Adults Humbled By Kids`
- **versionTag:** `(Schooled Edition)`
- **subCategoryId:** `adults_humbled_by_kids`
- **niche:** `aura_debt`
- **globalAudioPath:** `public/audio/stems/adults_humbled_by_kids_music_bed.mp3`

## Audio Design
- **Unique Background Stem:** `public/audio/stems/adults_humbled_by_kids_music_bed.mp3`
- **Source Track:** `g3ox_em - GigaChad Theme (Instrumental)` (YouTube ID: `TFdv3neI_zM`)
- **Audio Specs:** 48.00s duration, 48,000 Hz sample rate, 192 kbps AAC stereo, 1.0s fade-in, 2.0s fade-out.
- **Mix Level:** Volume set to `0.11` in Remotion props so 100% natural clip audio (voices, crowd cheers, court squeaks, mat taps) punches through with broadcast clarity.

## Multi-Platform Sourcing & 2fps Visual QA Process
1. **Reddit Sourcing (`agent-reach reddit search`):**
   - Queries: `"childrenfallingover humbled adult v.redd.it"`, `"sports kid humiliates adult v.redd.it"`, `"basketball kid ankle breaker adult v.redd.it"`.
   - Extracted and downloaded candidates: `v.redd.it/4xdtc1p1sv5h1`, `v.redd.it/rgbl51j9p2131`, `v.redd.it/tipzttma3y331`, `v.redd.it/tba5h17xibjd1`.
2. **YouTube Shorts Sourcing (`yt-dlp`):**
   - Queries: `"kids humbling adults in sports shorts"`, `"kid destroys adult 1v1 shorts"`, `"adults humbled by kids funny shorts"`.
   - Downloaded and analyzed candidates including `cNx2_r3eE8U` (BJJ match).
3. **2fps Contact Sheet QA (`fps=2,scale=260:-1,tile=8x10`):**
   - Generated contact sheets for all candidates and visually reviewed using `read_file`.
   - Filtered out clips with news/TV watermarks, baked-in meme captions, or missing payoffs.
4. **Full-Story Trimming (Cause -> Payoff -> Reaction):**
   - All 5 clips trimmed strictly to 30fps, yuv420p, aac 192k 48000Hz stereo.
   - Zero white flashes or action-obscuring popups.
   - Clean dark radial ambient backdrop (`radial-gradient(circle at center, #1c1d24 0%, #08080a 100%)`).

## 5-Clip Benchmark Table

| Rank | Level | Clip Path | Source | Duration | Frames | Aura Debt | Story Beat (Cause -> Payoff -> Reaction) |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| **5** | Level 1 | `public/clips/adults_humbled_by_kids/rank_5.mp4` | Reddit `v.redd.it/4xdtc1p1sv5h1` | 7.50s | 225 | -10,000 AURA | Dad flexes backwards halfcourt shot -> kid steps up and swishes it on first try effortlessly |
| **4** | Level 2 | `public/clips/adults_humbled_by_kids/rank_4.mp4` | Reddit `v.redd.it/rgbl51j9p2131` | 7.50s | 225 | -50,000 AURA | Dad challenges son in driveway defense -> kid drives and posterizes dad straight to the ground |
| **3** | Level 3 | `public/clips/adults_humbled_by_kids/rank_3.mp4` | YouTube `cNx2_r3eE8U` | 8.07s | 242 | -100,000 AURA | Adult competitor tries to bully young yellow belt -> kid pulls guard, locks armbar, adult taps out |
| **2** | Level 4 | `public/clips/adults_humbled_by_kids/rank_2.mp4` | Reddit `v.redd.it/tipzttma3y331` | 8.50s | 255 | -500,000 AURA | Adult challenges young boxing prodigy -> kid slips every single punch and outboxes him cleanly |
| **1** | Level 5 | `public/clips/adults_humbled_by_kids/rank_1.mp4` | Reddit `v.redd.it/tba5h17xibjd1` | 8.80s | 264 | -1,000,000 AURA | Little girl completely dismantles adult street soccer player with nutmeg & turn in front of his crew |

## Rendering & Audio Mastering Standards
- **Render Engine:** Remotion 4 (`RankingShort`) pre-bundled to avoid public folder file contention.
- **Audio Mastering:** FFmpeg `loudnorm=I=-14:TP=-1.5:LRA=11` (AAC 320k, 48kHz).
- **Loudness Verification:** EBU R128 `ebur128=peak=true` targeting Integrated Loudness `-14.0 ± 1.0 LUFS` and True Peak `<= -1.5 dBTP`.
- **Final QA Sheet:** 1fps visual sheet (`output/adults_humbled_by_kids_qa_sheet.jpg`) verified for 0 black frames and clean story payoff arcs.
- **Upload Metadata:** `output/adults_humbled_by_kids_upload_metadata.json` with mandatory owner credit disclaimer.
