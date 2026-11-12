# Subcategory Skill: `road_rage_justice` ("Road Rage Justice")

## Overview
- **Niche:** `instant_karma`
- **Format:** 1080x1920 @ 30fps YouTube Short (`RankingShort` Remotion composition)
- **Title Header:** `Ranking Best Of`
- **Subject Header:** `Road Rage Instant Karma`
- **Version Tag:** `(Dashcam Justice)`
- **Music Bed:** `public/audio/stems/road_rage_justice_music_bed.mp3` (Teriyaki Boyz - Tokyo Drift Instrumental `SHmzj5H7KiE`, 48s bed with 1s fade-in and 2s fade-out, mixed at `volume: 0.11` under `1.0` natural dashcam audio)

## Production Pipeline
1. **Multi-Platform Sourcing:**
   - Reddit (`agent-reach reddit search`): `"ConvenientCop road rage v.redd.it"`, `"IdiotsInCars instant karma v.redd.it"`, `"instantkarma road rage v.redd.it"`, `"brake check instant karma v.redd.it"`, `"ConvenientCop brake check v.redd.it"`.
   - YouTube (`yt-dlp`): `"road rage instant karma dashcam shorts"`, `"convenient cop road rage shorts"`, `"road ragers getting instant karma shorts"`.
2. **Mandatory 2fps Visual QA:**
   - Generated `fps=2,scale=260:-1,tile=8x10` contact sheets for all candidates and inspected every sheet visually.
   - Rejected: `r_k4fwzx7kyng41` (TikTok watermark), `r_p0zsktnhibee1` (heavy letterboxing + slow highway), `yt_iQ_OZP9psek` (Newsner watermark + baked-in captions), `yt_CF6HsP3Y7lA` (center logo + baked-in captions).
3. **Full-Story Trimming (30fps, yuv420p, aac 192k, 48000Hz):**
   - Preserved complete Cause -> Payoff -> Reaction arcs with `1.25x–1.38x` speed-up where needed so every clip lands in `8.8s–9.5s`.
4. **Remotion Render & EBU R128 Mastering:**
   - Rendered via `npx remotion render RankingShort output/road_rage_justice_raw.mp4 --props=cue_sheet_road_rage_justice.json --concurrency=2 --overwrite`.
   - Mastered with `loudnorm=I=-14:TP=-1.5:LRA=11` to `output/road_rage_justice_mastered.mp4`.

## 5-Clip Benchmark Table (Rank 5 -> Rank 1)

| Rank | Level | Source ID | Clip File | Source Window & Speed | Output Duration | Frames | Story Arc (Cause -> Payoff -> Reaction) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **5** | Level 1 | `v.redd.it/9ck84dsdea5e1` (r/ConvenientCop) | `public/clips/road_rage_justice/rank5_unmarked_cop.mp4` | `5.5s–18.0s` @ `1.32x` | `9.47s` | `284` | Sedan cuts off semi & driver gets out to rage -> unmarked cop behind flashes lights -> rager immediately gets back in |
| **4** | Level 2 | `v.redd.it/iurql50nav0e1` (r/ConvenientCop) | `public/clips/road_rage_justice/rank4_moto_cops.mp4` | `8.0s–20.0s` @ `1.30x` | `9.23s` | `276` | Dark sedan cuts off & brake-checks truck -> 2 police motorcycle officers pull right alongside -> truckers cheer as he gets pulled over |
| **3** | Level 3 | `v.redd.it/kim8ymadu4091` (r/IdiotsInCars) | `public/clips/road_rage_justice/rank3_spinout_barrier.mp4` | `18.0s–30.5s` @ `1.35x` | `9.27s` | `278` | Aggressive silver sedan speeds past on highway -> loses control, spins 180° across lanes -> slams into barrier in dust cloud |
| **2** | Level 4 | `v.redd.it/5ihff1snog891` (r/WinStupidPrizes) | `public/clips/road_rage_justice/rank2_brake_check_crash.mp4` | `2.5s–13.5s` @ `1.25x` | `8.81s` | `264` | Blue hatchback brake-checks to a full stop on highway -> truck behind rear-ends cam car into the brake-checker |
| **1** | Level 5 | `v.redd.it/p43qtq2v3wae1` (r/instantkarma) | `public/clips/road_rage_justice/rank1_suv_flips_ditch.mp4` | `5.5s–9.5s` + `17.5s–26.5s` @ `1.38x` | `9.43s` | `282` | White SUV swerves & clips motorcyclist, speeds off -> loses control & flips onto its side in ditch -> biker pulls up to confront |
