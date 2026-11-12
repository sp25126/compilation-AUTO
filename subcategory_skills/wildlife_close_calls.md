# Subcategory Skill: Wildlife Close Calls (`wildlife_close_calls`)

**Niche:** `nature_weather`  
**Format:** 1080x1920 @ 30fps, 5-clip countdown ranking (`Level 1` -> `Level 5`)  
**Title Header:** `Ranking Scariest`  
**Subject Header:** `Wildlife Close Calls`  
**Version Tag:** `(Inches Away)`  

## 1. Sourcing & Selection Criteria
- **Reddit (`agent-reach reddit search`):**
  - `"watchpeoplesurvive bear close call v.redd.it"`
  - `"sweatypalms shark close call v.redd.it"`
  - `"nonononoyes wildlife close call v.redd.it"`
- **YouTube (`yt-dlp`):**
  - `"wildlife close call caught on camera shorts"`
  - `"scary animal encounter close call shorts"`
  - `"bear chase close call shorts"`
  - `"shark close call shorts"`
- **2fps Visual QA Gate:** Rejected clips with watermarks (`kaotic.com`, `LatestSightings.com`), baked-in foreign subtitles (`yt_24IV6hAf9Lk`), or missing natural audio (`r_beejssjh6ya31`).

## 2. Audio & Music Bed
- **Unique Stem:** `public/audio/stems/wildlife_close_calls_music_bed.mp3`
- **Source:** YouTube `i4vz2v20G2M` ("Heartbeat Trailer NoCopyright Background Music for Video Editors"), trimmed to 48s with 1s fade-in and 2s fade-out.
- **Mix:** `0.11` volume under `1.0` natural clip audio (shouts, splashes, bear/shark impacts).
- **Master Target:** EBU R128 `-14.0 ± 1.0 LUFS`, `TP <= -1.5 dBTP`.

## 3. 5-Clip Benchmark Table

| Rank | Level | Source ID | Subject / Story | Source Window & Speed | Output Duration | Frames | Impact Frame |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 5 | Level 1 | `r_lq2u8jdu29n91` | Black bear charges onto screened porch; man fends it off with bench | `0.5s–9.5s` @ `1.15x` | `7.85s` | 235 | 85 |
| 4 | Level 2 | `r_lp08qx4hvpuc1` | Great white shark sneaks up behind diver and grazes his head | `0.0s–7.6s` @ `1.00x` | `7.60s` | 228 | 120 |
| 3 | Level 3 | `r_qx2hrkpst5z91` | Grizzly climbs up tree stand inches from hunter's boots | `2.0s–15.0s` @ `1.40x` | `9.30s` | 279 | 145 |
| 2 | Level 4 | `yt_0UhVwaPfhHM` | Polar bear shoves snout and paws through metal grate stairs | `6.0s–17.0s` @ `1.30x` | `8.47s` | 254 | 110 |
| 1 | Level 5 | `yt_oGtQKF62ZYg` | Great white shark smashes inside diving cage with diver trapped | `0.5s–13.0s` @ `1.35x` | `9.28s` | 278 | 70 |
