# Sub-Category Skill: `ice_driveway_slides` — Ice Driveway Slipping Moments

## 1. Concept & Niche Profile
- **Sub-Category ID:** `ice_driveway_slides`
- **Niche:** `nature_weather`
- **Title Header:** `Ranking Funniest`
- **Subject Header:** `Ice Slipping Moments`
- **Version Tag:** `(Zero Friction Edition)`
- **Target Format:** 1080x1920 @ 30fps YouTube Shorts / Reels / TikTok
- **Music Bed:** `public/audio/stems/ice_driveway_slides_music_bed.mp3` — *Fluffing a Duck* (Kevin MacLeod, 48s trim, 1s fade-in, 2s fade-out), mixed at `volume: 0.11` so natural clip audio (thuds, laughter, reactions, car/porch ambience) stays crystal clear.

## 2. Multi-Platform Sourcing & Visual QA
- **Reddit (`agent-reach reddit search`):**
  - Queries: `"slipping on ice ring camera v.redd.it"`, `"funny ice driveway slide v.redd.it"`, `"wellthatsucks ice slip v.redd.it"`
  - Candidates inspected: `r_17igkb44vvd61` (PASS), `r_jlllxzqb1xt91` (PASS), `r_p8o7wsh4rwqc1` (PASS), `r_e4mz9vth1pj61` (PASS), `r_r9eg9msg4if81` (PASS).
- **YouTube (`yt-dlp`):**
  - Queries: `"people slipping on ice ring camera shorts"`, `"ice driveway slide fail shorts"`, `"funny winter ice fails caught on camera shorts"`, `"slipping on ice driveway"`, `"slipping on ice ring camera"`
  - Candidates inspected: `yt_-OFJsQvR25U` (PASS), `yt_Q_WrhIgNHS8` (PASS), `yt_u7H05RzfzUE` (PASS), `yt_glRlDUUG_-c` (PASS), `yt_Yu3kzI3eeKA` (PASS), `yt_sUj81JgJeBs` (REJECT — CBS2 news banner & anchors).
- **2fps Visual QA:** Every candidate was inspected via `fps=2` contact sheets before selection; clips with news lower-thirds, baked-in text, or truncated payoffs were rejected.

## 3. 5-Clip Benchmark Table (Rank 5 -> Rank 1)

| Rank | Level | Source ID | Platform | Raw Trim & Speed | Final Duration | Frames | Story Arc (Cause -> Payoff -> Reaction) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **5** | Level 1 | `yt_-OFJsQvR25U` | YouTube | `5.5s–15.5s` @ `1.25x` | `8.00s` | `240` | Two guys step onto icy porch at night -> one slips and faceplants into the Ring camera -> laughs it off with friend. |
| **4** | Level 2 | `r_jlllxzqb1xt91` | Reddit | `0.0s–8.17s` @ `1.00x` | `8.17s` | `245` | Man in dress shirt & briefcase hits black ice -> 7-second cartoon flail-skate all the way down the driveway -> recovers at street. |
| **3** | Level 3 | `yt_Q_WrhIgNHS8` | YouTube | `15.5s–26.0s` @ `1.25x` | `8.47s` | `253` | UPS driver carries package across icy driveway -> loses footing and goes completely horizontal -> slides across pavement & gets up. |
| **2** | Level 4 | `r_17igkb44vvd61` | Reddit | `0.0s–11.5s` @ `1.35x` | `8.53s` | `255` | Woman holding coffee steps onto golden icy driveway -> slides all the way down on her butt -> crashes into parked car & stands up. |
| **1** | Level 5 | `yt_u7H05RzfzUE` | YouTube | `6.5s–17.5s` @ `1.30x` | `8.50s` | `254` | Man walks onto long icy driveway with salt bucket -> slips immediately -> slides 100ft all the way down to the street & gets up. |

## 4. Mastering & QA
- **Render:** `npx remotion render RankingShort output/ice_driveway_slides_raw.mp4 --props=cue_sheet_ice_driveway_slides.json --concurrency=2 --timeout=120000 --overwrite`
- **Mastering:** EBU R128 `loudnorm=I=-14:TP=-1.5:LRA=11` at `320k` AAC (`output/ice_driveway_slides_mastered.mp4`).
- **Final QA:** `1fps` contact sheet (`output/ice_driveway_slides_qa_sheet.jpg`) verified for 0 black frames and 100% complete stories.
