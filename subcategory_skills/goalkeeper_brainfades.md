# Sub-Category Skill: Goalkeeper Brainfades (`goalkeeper_brainfades`)

- **Niche:** `sports_bloopers`
- **Title Header:** `Ranking Funniest`
- **Subject Header:** `Goalkeeper Brainfades`
- **Version Tag:** `(Zero IQ Edition)`
- **Music Bed:** `public/audio/stems/goalkeeper_brainfades_music_bed.mp3` (Portugal Phonk, 48s, 1s fade-in, 2s fade-out, mixed at `0.11` volume under `1.0` natural clip audio)
- **Format:** `1080x1920` @ `30fps` (`yuv420p`, `aac 320k`, `48000Hz`, EBU R128 `-14.0 ± 1.0 LUFS`, `TP <= -1.5 dBTP`)

## Production Process
1. **Multi-Platform Sourcing:**
   - Reddit (`agent-reach reddit search`): `"soccer goalkeeper fail v.redd.it"`, `"ekstraklasaboners goalkeeper fail v.redd.it"`, `"prematurecelebration goalkeeper v.redd.it"`. Downloaded via `yt_dlp` `HLSPlaylist.m3u8`.
   - YouTube (`yt-dlp`): `"goalkeeper fail funny moments shorts"`, `"worst goalkeeper blunders shorts"`, `"goalkeeper brainfade moments shorts"`.
2. **Mandatory 2fps Visual QA:**
   - Generated `2fps` contact sheets (`tile=8x10`) for all candidates and inspected every sheet with `read_file`.
   - Rejected `r_gomphtxdgtgf1` (baked-in Chinese text & watermark) and `yt_lMQ-lwTi7WU` (The Guardian news overlay).
3. **Full-Story Trimming (Cause -> Payoff -> Reaction):**
   - Trimmed 5 distinct clips at 30fps, `yuv420p`, `aac 192k`, `48000Hz` with `1.25x–1.35x` speed adjustment on 10–12s sources so every clip lands in `8.0s–9.0s` without cutting off cause or reaction.
4. **Remotion Render & Mastering:**
   - Rendered via `RankingShort` composition with `cue_sheet_goalkeeper_brainfades.json` (`1299` clip frames + `75` outro frames = `1374` frames / `45.80s`).
   - Mastered with `loudnorm=I=-14:TP=-1.5:LRA=11` and verified with `ebur128=peak=true` + 1fps QA sheet inspection.

## 5-Clip Benchmark Table

| Rank | Level | Source ID | Platform | Trim Window | Speed | Out Duration (Frames) | Story (Cause → Payoff → Reaction) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **5** | Level 1 | `r_fdj44sy8getg1` | Reddit (`v.redd.it`) | `17.5s–29.5s` | `1.35x` | `8.90s` (`267f`) | Polish 2 Liga keeper Murawski #12 whiffs routine backpass into own net + devastated close-up |
| **4** | Level 2 | `r_ysgfubrds4ca1` | Reddit (`v.redd.it`) | `0.5s–10.5s` | `1.25x` | `8.00s` (`240f`) | Besiktas keeper Mert Gunok concedes in under 60s off a backpass whiff & collapses inside the net |
| **3** | Level 3 | `r_f06d7w5zflzb1` | Reddit (`v.redd.it`) | `20.5s–31.0s` | `1.25x` | `8.40s` (`252f`) | Keeper saves penalty, fist-pumps to celebrate, and concedes the rebound while celebrating |
| **2** | Level 4 | `r_qgztgebdsrdg1` | Reddit (`v.redd.it`) | `2.0s–11.0s` | `1.00x` | `9.00s` (`270f`) | AFC U23 Asian Cup keeper #22 saves penalty and walks off celebrating while ball spins back into goal |
| **1** | Level 5 | `yt_3GMig6o3bMs` | YouTube | `0.0s–9.0s` | `1.00x` | `9.00s` (`270f`) | Bundesliga 2 keeper Mark Flekken drinks from water bottle inside goal while opponent scores |
