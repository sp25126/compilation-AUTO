# Sub-Category Skill: `delivery_driver_mishaps` ("Delivery Driver Slips")

- **Niche:** `workplace_disasters`
- **Format:** 1080x1920 @ 30fps, @MrPurifiedWater + @cliportey hybrid ranking Short
- **Header Props:**
  - `titleHeader`: `"Ranking Funniest"`
  - `subjectHeader`: `"Delivery Driver Fails"`
  - `versionTag`: `"(Ring Camera Edition)"`
- **Music Bed:** `public/audio/stems/delivery_driver_mishaps_music_bed.mp3` — *Sneaky Snitch* (Kevin MacLeod, YouTube `Cm0qaXi9THA`), 48s bed with 1s fade-in and 2s fade-out, mixed at `0.11` volume under `1.0` natural clip audio.

## Production Process
1. **Multi-Platform Sourcing:**
   - Reddit (`agent-reach reddit search`): `"delivery driver fail ring camera v.redd.it"`, `"amazon driver funny fail v.redd.it"`, `"doordash fail ring camera v.redd.it"`, `"delivery driver fell ring camera v.redd.it"`, `"ups fedex driver slip fall v.redd.it"`.
   - YouTube (`yt-dlp`): `"funny delivery driver ring camera shorts"`, `"amazon delivery driver fail caught on camera shorts"`, `"best doorbell delivery fails shorts"`, `"delivery driver slip fall ring camera shorts"`, `"ups fedex delivery driver slips falls ring camera shorts"`.
2. **2fps Visual QA:**
   - Generated `2fps` contact sheets (`tile=8x10`) for all harvested candidates and inspected via `read_file`.
   - Rejected candidates with TikTok watermarks (`r_ar78k6lceir71`, `r_ucnwsal1kjba1`), baked-in meme/news overlays (`r_ao697hjkrkxg1`, `r_jx74xsvx02if1`, `yt_vY50qU8C4Zo`, `r_5rsgbu1nz2uf1`), dark/unreadable footage (`r_57ckeuxv8ez91`), or static monitor recordings (`r_7jrgtzrznt6g1`).
3. **Full-Story Trimming:**
   - Trimmed 5 distinct, clean Ring/Nest/Wyze security camera clips preserving full Cause -> Payoff -> Reaction (`8.0s - 9.43s` out, 30fps `yuv420p`, `aac 192k`, `48000Hz`).
4. **Remotion Render & Mastering:**
   - Rendered `RankingShort` to `output/delivery_driver_mishaps_raw.mp4` using `cue_sheet_delivery_driver_mishaps.json`.
   - Mastered to YouTube Shorts EBU R128 loudness (`-14.0 ± 1.0 LUFS`, `TP <= -1.5 dBTP`) into `output/delivery_driver_mishaps_mastered.mp4`.
   - Verified final `1fps` contact sheet (`output/delivery_driver_mishaps_qa_sheet.jpg`).

## 5-Clip Benchmark Table

| Rank | Level | Source ID | Platform | Trim Window | Speed | Out Duration (Frames) | Story Summary |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Rank 5 | Level 1 | `wCe2UPweuIo` | YouTube (Wyze Cam) | `3.5s - 12.0s` | `1.0x` | `8.50s` (`255f`) | Amazon driver walks up, casually yeets package onto porch, and jogs away. |
| Rank 4 | Level 2 | `ja2ki1prmlie1` | Reddit (Nest Cam) | `10.0s - 19.0s` | `1.0x` | `9.00s` (`270f`) | Driver drops package, sprints back to car, and wipes out flat on the driveway. |
| Rank 3 | Level 3 | `VbXRKrEFUTE` | YouTube (Ring Cam) | `2.5s - 13.5s` | `1.25x` | `8.83s` (`264f`) | Amazon driver trips on porch steps at night, faceplants, and crawls back up. |
| Rank 2 | Level 4 | `PPHgXEdKvko` | YouTube (Ring Cam) | `5.5s - 13.5s` | `1.0x` | `8.00s` (`240f`) | Visitor/delivery slips on top porch step and tumbles backwards down the stairs. |
| Rank 1 | Level 5 | `alzksetli5v51` | Reddit (Ring Cam) | `4.5s - 17.5s` | `1.38x` | `9.43s` (`282f`) | Amazon driver slips on wet porch, tries to recover packages, and gets body-slammed a second time. |
