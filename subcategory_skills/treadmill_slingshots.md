# Subcategory Skill: `treadmill_slingshots` ("Gym & Treadmill Fails")

- **Niche:** `gym_bloopers`
- **Format:** `1080x1920 @ 30fps`, `39.36s` (`1181` frames including outro)
- **Header Props:**
  - `titleHeader`: `"Ranking Funniest"`
  - `subjectHeader`: `"Gym & Treadmill Fails"`
  - `versionTag`: `"(Max Speed Edition)"`
  - `globalAudioPath`: `"public/audio/stems/treadmill_slingshots_music_bed.mp3"` (DVRST - Close Eyes Instrumental HQ, 48s bed with 1s fade-in and 2s fade-out, mixed at `0.11` volume)

## Production Workflow
1. **Multi-platform Sourcing:**
   - Reddit (`agent-reach reddit search`): `"gym fail treadmill v.redd.it"`, `"whatcouldgowrong treadmill v.redd.it"`, `"gym fail ego lift v.redd.it"` -> downloaded 7 `v.redd.it` candidates via `yt-dlp`.
   - YouTube (`py -3 -m yt_dlp`): `"treadmill fail caught on camera shorts"`, `"gym ego lifting fail shorts"` -> downloaded 2 clean candidates (`9VBjmumIffM`, `SoSULwEZyxA`).
2. **Mandatory 2fps Visual QA:**
   - Generated `2fps` contact sheets for all 9 candidates and inspected every sheet.
   - Rejected `r_169g25yfg49h1` (baked-in emoji overlay) and `r_qk25wikmiipc1` (Facebook/Instagram UI overlay).
3. **Full-Story Trimming (`30fps`, `yuv420p`, `aac 192k`, `48000Hz`):**
   - Preserved full Cause -> Payoff -> Reaction for all 5 clips (`6.2s - 9.3s` per clip).
   - Fixed `rank_2.mp4` color/SAR consistency (`scale=720:1280,setsar=1,format=yuv420p,bt709`) to prevent Remotion `OffthreadVideo` mid-stream `Output changed` errors.
4. **Remotion Render & EBU R128 Mastering:**
   - Rendered `output/treadmill_slingshots_raw.mp4` via `npx remotion render RankingShort --concurrency=2 --offthreadvideo-cache-size-in-bytes=536870912`.
   - Mastered to `output/treadmill_slingshots_mastered.mp4`: **Integrated Loudness `-14.0 LUFS`**, **LRA `6.7 LU`**, **True Peak `-2.2 dBFS`** (`<= -1.5 dBTP`).
   - Verified `1fps` final QA sheet (`output/treadmill_slingshots_qa_sheet.jpg`): 0 black frames, all 5 stories + outro complete.

## 5-Clip Benchmark Table
| Rank | Level | Source ID | Platform | Trim / Speed | Out Duration (Frames) | Story & Punchline |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Rank 5 | Level 1 | `yt_9VBjmumIffM` | YouTube | `0.0s - 7.01s` (1.0x) | `7.01s` (`210f`) | Gym interview photobombed by woman launching off treadmill — `EXITED THE CHAT` |
| Rank 4 | Level 2 | `r_p0yj687dvdc51` | Reddit | `0.0s - 6.22s` (1.0x) | `6.22s` (`186f`) | Falls off treadmill and smoothly transitions into pushups — `10/10 RECOVERY` |
| Rank 3 | Level 3 | `yt_SoSULwEZyxA` | YouTube | `3.5s - 16.0s` (1.35x) | `9.30s` (`279f`) | Ego bench press fail rescued by spotters — `SPOTTER SAVED HIM` |
| Rank 2 | Level 4 | `r_k2q9lom42fwg1` | Reddit | `0.0s - 6.20s` (1.0x) | `6.20s` (`186f`) | Dumbbell press on moving treadmill crashes into table & spills water — `TOTAL WIPEOUT` |
| Rank 1 | Level 5 | `r_v3i48g5ujjoc1` | Reddit | `1.5s - 9.67s` (1.0x) | `8.17s` (`245f`) | Max speed treadmill turns into a human slingshot into the wall — `LAUNCHED TO ORBIT` |
