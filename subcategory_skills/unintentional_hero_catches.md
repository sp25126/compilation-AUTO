# Sub-Category Skill: `unintentional_hero_catches`

## Header & Composition Config
- **Composition:** `RankingShort` (`src/remotion/MrPurifiedWaterShort.tsx`)
- **Cue Sheet:** `cue_sheet_unintentional_hero_catches.json`
- **titleHeader:** `Ranking Insane`
- **subjectHeader:** `Dad Reflex Catches`
- **versionTag:** `(Superhero Reflexes)`
- **subCategoryId:** `unintentional_hero_catches`
- **subCategoryName:** `DAD REFLEX CATCHES`
- **niche:** `extreme_luck`
- **globalAudioPath:** `public/audio/stems/unintentional_hero_catches_music_bed.mp3`
- **showSubtitles:** `false` (Subtitles disabled per user instructions)
- **enableLogoPopupDemo:** `false`

## Audio Design
- **Unique Background Stem:** `public/audio/stems/unintentional_hero_catches_music_bed.mp3`
- **Source Track:** Alexander Lewis & Brasstracks - All Of The Lights Brass Remix (YouTube ID: `a35lFoN0NHg`, 1.4M views)
- **Audio Specs:** 48.02s duration, 48,000 Hz sample rate, 192 kbps AAC stereo, 1.0s fade-in, 2.0s fade-out.
- **Mix Level:** Volume ducked to `0.11` in Remotion props so 100% natural clip audio (cheers, laughs, gasps, stadium roar, physical slides) punches through with crystal clear broadcast balance.

## Multi-Platform Sourcing & 2fps Visual QA Process
1. **Multi-Platform Sourcing:**
   - **Reddit Sourcing (`agent-reach reddit search`):**
     - Queries: `"DadReflexes insane save v.redd.it"`, `"stepdadreflexes save v.redd.it"`, `"fastreflexes hero catch v.redd.it"`.
     - Analyzed submissions from `r/DadReflexes`, `r/StepDadReflexes`, and `r/holdmyfeedingtube`.
   - **YouTube Shorts Sourcing (`yt-dlp`):**
     - Queries: `"dad reflexes insane catches shorts"`, `"superhero dad saves baby caught on camera shorts"`, `"insane reflex catches caught on camera shorts"`.
     - Harvested high-definition viral candidates with full context and reactions.
2. **2fps Contact Sheet QA (`fps=2,scale=260:-1,tile=8x10`):**
   - Generated 2fps contact sheets for all downloaded harvest candidates.
   - Visually inspected each candidate sheet with `read_file`.
   - **Strict Rejections:**
     - `yt_Ktwgm1U2ero`: Rejected (Good Morning America broadcast lower thirds and banner).
     - `yt_qtwK7SEOpKM`: Rejected (Fox 5 News logo and ticker watermark).
     - `yt_rB-MGqrW8is`: Rejected (Inside Edition TV graphics overlay).
     - `yt_5Gu7Snp3yzs`: Rejected (GoViral subscribe watermark, distant crop).
     - `r_jl8uetnzsfz21`: Rejected (164x320 low resolution, heavy compression artifacts).
     - `cake_save.mp4`: Rejected (silent 3.8s 90s camcorder clip lacking reaction).
3. **Full-Story Trimming (Cause -> Payoff -> Reaction):**
   - Trimmed 5 verified clean clips strictly to 30fps, yuv420p, aac 192k 48000Hz stereo.
   - Paced each story beat at 5.97s - 8.50s maintaining complete buildup, reflex catch payoff, and celebratory reaction.
   - Zero white flashes or action-obscuring popups.
   - Styled with clean dark radial ambient backdrop (`radial-gradient(circle at center, #1c1d24 0%, #08080a 100%)`).

## 5-Clip Benchmark Table

| Rank | Level | Clip Path | Source | Duration | Frames | Story Beat (Cause -> Payoff -> Reaction) |
| :--- | :---: | :--- | :--- | :---: | :---: | :--- |
| **5** | Level 1 | `public/clips/unintentional_hero_catches/clip_5.mp4` | YouTube `yt_9gdMuSt2SUg` | 6.00s | 180 | **Living Room Cushion Toss:** Toddler slips off foam steps backwards -> Dad launches throw pillow sniper-style directly under the infant's falling head -> Dad throws hands up in touchdown celebration, Mom claps. |
| **4** | Level 2 | `public/clips/unintentional_hero_catches/clip_4.mp4` | YouTube `yt_7bVTmaGo8kA` | 5.97s | 179 | **Park Walkway Dive:** Toddler trips headfirst on pavement -> Dad executes horizontal baseball slide on asphalt, catching child inches from impact -> Scoops kid up safely. |
| **3** | Level 3 | `public/clips/unintentional_hero_catches/clip_3.mp4` | YouTube `yt_fEPHbTFv1Cs` | 6.00s | 180 | **Crib Somersault Save:** Toddler flips upside down over top rail of high crib -> Dad power-slides on knees across carpet catching child mid-air before hitting floor -> Hugs toddler safely. |
| **2** | Level 4 | `public/clips/unintentional_hero_catches/clip_2.mp4` | YouTube `yt_tCxPx0URUI` | 7.50s | 225 | **Blind No-Look Snatch:** Gamer dad sits wearing headset facing PC monitor -> Toddler rolls off high bed directly behind him -> Dad reaches blind left arm backwards mid-fall and snatches child by shirt inches from hardwood floor without even looking. |
| **1** | Level 5 | `public/clips/unintentional_hero_catches/clip_1.mp4` | YouTube `yt_YWbBR8dFlUg` | 8.50s | 255 | **MLB 90mph Barehand Line-Drive Catch:** Screaming 90mph foul ball rockets toward lower deck stands -> Dad cradling baby with left arm reaches bare right hand high into the air, snatching the line-drive clean -> Entire stadium erupts in standing ovation, mom and fans celebrate in disbelief. |

## Rendering & Mastering Pipeline
- **Render Engine:** Remotion 4 (`RankingShort` composition, 1080x1920 @ 30fps).
- **Audio Mastering:** FFmpeg Two-Pass/Single-Pass EBU R128 `loudnorm=I=-14:TP=-1.5:LRA=11` (AAC 320k, 48kHz).
- **Loudness Verification:** EBU R128 `ebur128=peak=true` targeting Integrated Loudness `-14.0 ± 1.0 LUFS` and True Peak `<= -1.5 dBTP`.
- **Final QA Sheet:** 1fps visual sheet (`output/unintentional_hero_catches_qa_sheet.jpg`) inspected with `read_file` to confirm 0 black frames and clean story payoff arcs.
- **Upload Metadata:** `output/unintentional_hero_catches_upload_metadata.json` with mandatory owner credit disclaimer, SEO tags, and optimal IST/EST scheduling.
