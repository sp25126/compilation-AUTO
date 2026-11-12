# Subcategory Skill: Friendzone Escapes (`friendzone_escapes`)

- **Niche:** `wholesome_romance`
- **Format:** 1080x1920 @ 30fps Vertical Ranking Short (`RankingShort`)
- **Headers:** `Ranking Greatest` / `Friendzone Escapes` / `(W Moment)`
- **Music Bed:** `public/audio/stems/friendzone_escapes_music_bed.mp3` — *"Until I Found You - Stephen Sanchez (AI Filtered Instrumental)"* (`l6RBDcfxJac`), 48s cut (`12s–60s`) with 1s fade-in and 2s fade-out, mixed at `0.11` volume under `1.0` natural clip audio.

## Production Process
1. **Multi-platform Sourcing:**
   - Searched Reddit (`agent-reach reddit search`) across `r/MadeMeSmile`, `r/Happyfreakout`, `r/Friendzone`, `r/Advice` for `v.redd.it` confession/kiss clips.
   - Searched YouTube via `yt-dlp` for clean, watermark-free confession & friendzone escape reactions (`yt__BnU5a5z1J8`, `yt_G1mz0Qv6Itg`, `yt_KgvEhso82f4`, `yt_aVvGVJMZw9s`, `yt_I6zMJC0etzE`, `yt_JYvdV_7Ub-c`).
2. **2fps Visual QA Gate:**
   - Generated `fps=2,scale=260:-1,tile=8x10` contact sheets for every candidate and inspected via `read_file`.
   - Rejected all clips with TikTok watermarks (`@butterscotch1124`, `@tylerdownss`), kiss-cam overlays, split-screens, or off-topic content.
3. **Full-Story Trimming (Cause → Payoff → Reaction):**
   - Encoded 5 distinct creator clips at `30fps`, `yuv420p`, `aac 192k`, `48000Hz`.
   - Applied `1.25x–1.38x` speed-up (`setpts=PTS/<spd>`, `atempo=<spd>`) to preserve full 11.5s–13.0s Cause → Payoff → Reaction arcs within `9.2s–9.5s` each.
   - Cropped 4:3 pillarboxed source (`yt_I6zMJC0etzE`) to `1440:1080` to eliminate black sidebars.
   - Omitted `impactFrameOffset` and `punchlineText` to keep action clean (no white flashes or popups).
4. **Remotion Render & EBU R128 Mastering:**
   - Rendered `output/friendzone_escapes_raw.mp4` via `RankingShort`.
   - Mastered to `output/friendzone_escapes_mastered.mp4` (`loudnorm=I=-14:TP=-1.5:LRA=11`, `320k` AAC) and verified via `ebur128=peak=true` + 1fps `output/friendzone_escapes_qa_sheet.jpg`.

## 5-Clip Benchmark Table

| Rank | Level | Source Video | Trim Window | Speed | Out Duration | Frames | Story Arc (Cause → Payoff → Reaction) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Rank 5 | Level 1 | `yt_G1mz0Qv6Itg` (NYC Roommate Dinner) | `608.0s–619.5s` (11.5s) | 1.25x | 9.21s | 274 | Candlelit dinner confession card → warm snowy NYC street hug |
| Rank 4 | Level 2 | `yt_KgvEhso82f4` (Night Beach Confession) | `446.5s–458.0s` (11.5s) | 1.25x | 9.23s | 274 | Asks crush on beach at night → "Yes, I have been and I will be" + shoulder lean |
| Rank 3 | Level 3 | `yt_aVvGVJMZw9s` (Rose-Petal Room) | `200.0s–211.5s` (11.5s) | 1.25x | 9.22s | 274 | Red roses + "May I be your boyfriend?" lightbox → "Yeah" + beaming hug |
| Rank 2 | Level 4 | `yt_I6zMJC0etzE` (Picnic Under Tree) | `572.0s–585.0s` (13.0s) | 1.38x | 9.47s | 281 | "Rosy, can I please be your boyfriend?" → "You already know, it's a yes" |
| Rank 1 | Level 5 | `yt_JYvdV_7Ub-c` (Bed Confession) | `669.0s–682.0s` (13.0s) | 1.38x | 9.43s | 280 | "Was it weird that I said I love you?" → "No" → pulls him in by hoodie for first kiss |
