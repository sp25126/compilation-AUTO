---
sub_category_id: overconfident_humbled
sub_category_name: OVERCONFIDENT HUMBLED
niche: overconfident_humbled
references:
  - "@MrPurifiedWater"
  - "@cliportey"
audio_track: public/audio/stems/karma_comedy_master.mp3
audio_source: "Monkeys Spinning Monkeys - Kevin MacLeod (pr42azVZi3o, 22.49M views)"
audio_bg_volume: 0.11
compositor: src/remotion/MrPurifiedWaterShort.tsx
cue_sheet: cue_sheet_overconfident_humbled.json
---

# Sub-Category Skill: `overconfident_humbled` ("Overconfident People Humbled")

> **MANDATORY FOR AI PIPELINE:** Every rule in this file was verified through multi-platform sourcing, 2fps visual inspection, story-preserving trimming, Remotion compositing, EBU R128 mastering, and 1fps final QA.

---

## 1. Core Production Rules
1. **Header Props:**
   - `titleHeader`: `"Ranking Best Of"`
   - `subjectHeader`: `"Overconfident People Humbled"`
   - `versionTag`: `"(Ego Checked Edition)"`
   - `subCategoryId`: `"overconfident_humbled"`
   - `subCategoryName`: `"OVERCONFIDENT HUMBLED"`
2. **Never Interrupt the Action:**
   - Zero white impact flashes, zero text popups over the action, and zero premature cuts. Every clip preserves **100% of Cause -> Payoff -> Reaction** (`5.5s - 9.5s` per clip).
3. **Audio Bed & Natural Audio:**
   - `public/audio/stems/karma_comedy_master.mp3` mixed at `volume: 0.11` under `1.0` natural clip audio, mastered to `-14.0 LUFS` (`TP <= -1.5 dBTP`).

---

## 2. Multi-Platform Sourcing & Rejection Log
- **Reddit (`agent-reach reddit search` + `v.redd.it` HLS):**
  - `"instant_regret overconfident v.redd.it"`
  - `"whatcouldgowrong showoff fail v.redd.it"`
  - `"prematurecelebration v.redd.it"`
- **YouTube (`yt-dlp --js-runtimes node --flat-playlist --dump-json`):**
  - `"showing off fail instant regret #shorts"`
  - `"backflip fail showing off #shorts"`
  - `"arm wrestling cocky humbled #shorts"`
  - `"parkour fail showing off #shorts"`
- **Rejected Candidates (2fps Visual QA Gate):**
  - `r_m051y0x4k3201`: 180x320 resolution too low.
  - `r_suyr3qhku6621`: Streamer webcam + chat overlay, unclear action.
  - `yt_RDl1yp-UN04`: First-person GoPro roof jump, payoff unclear.
  - `r_f57ywjbt04cd1`: `PAC-12 NETWORK` broadcast ticker banner at bottom.
  - `r_6n6g7w9rl6d21`: `Videoholic` watermark in top-right corner.
  - `r_bed4278rtdq11` / `r_50f2m7f92cd91`: Low resolution / distant framing.

---

## 3. Verified 5-Clip Benchmark Table (Rank 5 -> Rank 1)

| Rank | Clip ID | Source | Story (Cause -> Payoff -> Reaction) | Trim (`ss` / `t`) | Speed | Out Duration / Frames | Output File |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Rank 5 (Level 1)** | `overconfident_humbled_5` | YouTube `dbstNMD24w4` | Parkour showoff sprints across bleachers -> misses trash can and faceplants into grass -> rolls in pain | `1.0s` / `8.5s` | `1.25x` | `6.83s` (`205f`) | `public/clips/overconfident_humbled/rank5_trimmed.mp4` |
| **Rank 4 (Level 2)** | `overconfident_humbled_4` | Reddit `v.redd.it/fh91gbkxq04b1` | Guy tries a showoff backflip/kick in front of girls -> slips on wet pavement, slams flat on back | `0.0s` / `5.53s` | `1.00x` | `5.53s` (`166f`) | `public/clips/overconfident_humbled/rank4_trimmed.mp4` |
| **Rank 3 (Level 3)** | `overconfident_humbled_3` | Reddit `v.redd.it/4og6cf5cl0c21` | Guy struts one-handed with a full tray of pints -> drops entire tray on table/floor -> bolts out door | `0.5s` / `10.8s` | `1.35x` | `8.03s` (`241f`) | `public/clips/overconfident_humbled/rank3_trimmed.mp4` |
| **Rank 2 (Level 4)** | `overconfident_humbled_2` | YouTube `9dLQI6nKhWI` | Graduate attempts showoff backflip off graduation stage -> under-rotates, faceplants into turf -> walks off humbled | `19.0s` / `7.8s` | `1.00x` | `7.80s` (`234f`) | `public/clips/overconfident_humbled/rank2_trimmed.mp4` |
| **Rank 1 (Level 5)** | `overconfident_humbled_1` | Reddit `v.redd.it/7a23ned9a4ge1` | Cocky runner turns around taunting rival before finish line -> trips and faceplants in dirt while rivals sprint past | `2.5s` / `8.4s` | `1.15x` | `7.31s` (`219f`) | `public/clips/overconfident_humbled/rank1_trimmed.mp4` |
