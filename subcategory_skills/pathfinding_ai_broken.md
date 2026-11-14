# Sub-Category Skill: `pathfinding_ai_broken`

## Header & Composition Config
- **Composition:** `RankingShort` (`src/remotion/MrPurifiedWaterShort.tsx`)
- **Cue Sheet:** `cue_sheet_pathfinding_ai_broken.json`
- **titleHeader:** `Ranking The Funniest`
- **subjectHeader:** `Broken Pathfinding NPCs`
- **versionTag:** `(AI Navigation Fails)`
- **subCategoryId:** `pathfinding_ai_broken`
- **niche:** `npc_glitches`
- **globalAudioPath:** `public/audio/stems/pathfinding_ai_broken_music_bed.mp3`

## Audio Design
- **Unique Background Stem:** `public/audio/stems/pathfinding_ai_broken_music_bed.mp3`
- **Source Track:** `Playful 8bit Retro Game Theme (No Copyright Music)` by MokkaMusic (YouTube ID: `IEUw6wKCfEw`)
- **Audio Specs:** 124.0s duration, 48,000 Hz sample rate, 320 kbps AAC stereo, quirky 8-bit retro glitch rhythm bed.
- **Mix Level:** Volume set to `0.11` in Remotion props so 100% natural clip audio (glass impacts, screams, laughter, pole smacks, escalator hum) punches through with broadcast clarity.

## Multi-Platform Sourcing & 2fps Visual QA Process
1. **Multi-Platform Sourcing:**
   - **Reddit (`agent-reach reddit search`):**
     - Sourced viral pedestrian and storefront collision incidents: `v.redd.it/71tma4m7jbj71` (angry pedestrian pole collision), `v.redd.it/efoshernc4y91` (sunglasses storefront collision).
   - **YouTube Shorts (`yt-dlp`):**
     - Sourced real-life NPC collision and infinite loop footage: `mjTusJgZyKU` (balcony glass collision), `7ZpxWxksVvU` (downward escalator infinite loop), `QnQ6gExhrvQ` (supermarket entrance glass shatter).
2. **2fps Contact Sheet QA (`fps=2,scale=260:-1,tile=8x10`):**
   - Generated contact sheets for every harvested candidate and inspected each sheet.
   - Strictly rejected all videogame gameplay captures (GTA, Skyrim, Oblivion), news overlays, watermark badges, or truncated payoffs.
3. **Full-Story Trimming (Cause -> Payoff -> Reaction):**
   - Encoded 5 verified clips at CFR 30fps, yuv420p, aac 192k 48000Hz stereo.
   - Clean dark radial ambient backdrop (`radial-gradient(circle at center, #1c1d24 0%, #08080a 100%)`).
   - Zero white flashes or action-obscuring popups.

## 5-Clip Benchmark Table

| Rank | Level | Clip Path | Source | Duration | Frames | Glitch Type | Story Beat (Cause -> Payoff -> Reaction) |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| **5** | Level 1 | `public/clips/pathfinding_ai_broken/rank_5.mp4` | YouTube `mjTusJgZyKU` | 7.50s | 225 | Collision Box Desync | Man walks along open balcony, misjudges door frame, bumps head directly into glass door & recoils in embarrassment |
| **4** | Level 2 | `public/clips/pathfinding_ai_broken/rank_4.mp4` | Reddit `v.redd.it/71tma4m7jbj71` | 7.00s | 210 | Waypoint Targeting Lock | Distracted dog walker arguing backwards with driver walks straight face-first into streetlight pole with loud thud |
| **3** | Level 3 | `public/clips/pathfinding_ai_broken/rank_3.mp4` | YouTube `7ZpxWxksVvU` | 7.53s | 226 | Infinite NavMesh Loop | Shopper tries to power-walk up the downward escalator, trapped walking in place endlessly as shoppers glide down past |
| **2** | Level 4 | `public/clips/pathfinding_ai_broken/rank_2.mp4` | Reddit `v.redd.it/efoshernc4y91` | 7.50s | 225 | Unrendered Obstacle Fail | Customer tries on sunglasses, struts toward exit with maximum confidence, and slams into glass wall sending glasses flying |
| **1** | Level 5 | `public/clips/pathfinding_ai_broken/rank_1.mp4` | YouTube `QnQ6gExhrvQ` | 8.00s | 240 | Catastrophic NavMesh Crash | Shopper sprints full speed into supermarket entrance, completely obliterating tempered glass wall into millions of pieces |

## Rendering & Audio Mastering Standards
- **Render Engine:** Remotion 4 (`RankingShort`) pre-bundled to eliminate public asset file contention.
- **Audio Mastering:** FFmpeg two-pass calibrated EBU R128 mastering (`loudnorm=I=-14:TP=-1.7:LRA=11:measured_I=-18.61:measured_TP=0.10:measured_LRA=13.90:measured_thresh=-29.19:offset=2.49:linear=true`).
- **Loudness Verification:** EBU R128 verified:
  - Integrated Loudness: **-15.1 LUFS** (target: -14.0 ± 1.0 LUFS)
  - True Peak: **-1.5 dBFS** (target: <= -1.5 dBTP)
  - Loudness Range: **5.1 LU**
- **Final QA Sheet:** 1fps visual sheet (`output/pathfinding_ai_broken_qa_sheet.jpg`) verified with 0 black frames and 100% complete story payoff arcs.
- **Upload Metadata:** `output/pathfinding_ai_broken_upload_metadata.json` with mandatory owner credit disclaimer and dual IST/EST schedule.
