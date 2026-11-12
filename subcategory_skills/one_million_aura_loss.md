---
sub_category_id: one_million_aura_loss
sub_category_name: -1,000,000 AURA MOMENTS
niche: aura_debt
references:
  - "@MrPurifiedWater"
  - "@cliportey"
audio_track: public/audio/stems/one_million_aura_loss_music_bed.mp3
audio_source: "Ogryzek - AURA (Official Music Anthem, AYeLloU1qjI, 32.89M+ views)"
audio_bg_volume: 0.11
compositor: src/remotion/MrPurifiedWaterShort.tsx
cue_sheet: cue_sheet_one_million_aura_loss.json
---

# Sub-Category Skill: `one_million_aura_loss` ("-1,000,000 AURA MOMENTS")

> **MANDATORY FOR AI PIPELINE:** Every rule in this file was verified through live YouTube trend research, multi-platform sourcing, 2fps visual inspection, story-preserving trimming, Remotion compositing, EBU R128 mastering (`-15.5 LUFS`, True Peak `-1.5 dBFS`), and 1fps final QA.

---

## 1. Core Production Rules
1. **Header & Composition Props (`RankingShort`):**
   - `titleHeader`: `"Ranking The Worst"`
   - `subjectHeader`: `"-1,000,000 AURA MOMENTS"`
   - `versionTag`: `"(Infinite Debt)"`
   - `subCategoryId`: `"one_million_aura_loss"`
   - `subCategoryName`: `"-1,000,000 AURA MOMENTS"`
   - `globalAudioPath`: `"public/audio/stems/one_million_aura_loss_music_bed.mp3"`
2. **Escalating Aura Debt Ladder:**
   - Each clip MUST escalate in social embarrassment ("Aura Debt") from Level 1 (`-10,000 AURA`) up to Level 5 (`-1,000,000 AURA`).
   - Kinetic `punchlineText` triggers at `impactFrameOffset` right as the social humiliation peaks, without obscuring the face or physical comedy.
3. **Never Interrupt the Action:**
   - Zero white impact flashes, zero text banners over the action, and zero premature cuts. Every clip preserves **100% of Cause (Swagger/Attempt) -> Payoff (Fumble/Fail) -> Reaction (Awkward Recovery / Crowd Laughs)**.
4. **Unique Category-Matched Audio Bed & Natural Foley:**
   - Uses **Ogryzek – AURA** (`public/audio/stems/one_million_aura_loss_music_bed.mp3`, 48.0s bed with 1.0s head fade & 2.0s tail fade) mixed at `volume: 0.11` under `1.0` natural clip audio.
   - Where a Reddit clip lacks river-splash audio (Rank 1), mux a synchronized foley splash (`temp_harvest/splash.mp3`) at `6.8s` so the impact hits hard.
   - Mastered via `loudnorm=I=-14.0:TP=-1.5:LRA=11` (verified `-15.5 LUFS`, True Peak `-1.5 dBFS`, LRA `13.6 LU`).

---

## 2. Multi-Platform Sourcing & Rejection Log
- **Reddit (`agent-reach reddit search` + `v.redd.it` HLS):**
  - `"watchpeopledieinside trying to look cool v.redd.it"`
  - `"holdmybeer trying to impress v.redd.it"`
  - `"whatcouldgowrong trying to look cool v.redd.it"`
  - `"cringe handshake left hanging v.redd.it"`
- **YouTube Shorts (`yt-dlp --js-runtimes node --flat-playlist --dump-json`):**
  - `"trying to look cool fail shorts"`
  - `"infinite aura loss moments shorts"`
  - `"Josh Hart high five himself"`
- **Rejected Candidates (2fps Visual QA Gate):**
  - `aura_ultimate_failed_handshake_yg40kfivkzx51`: Baked-in top/bottom meme text banner.
  - `aura_hmb_impress_woman_rgiq4ecrvqu11`: `DU Recorder` watermark overlay.
  - `aura_selfie_scooter_c1sqbefuep091`: Graphic injury/blood (violates clean comedy standard).
  - `sheet_yt_river_stairs`: Baked-in foreign text subtitle over the action.

---

## 3. Verified 5-Clip Benchmark Table (Rank 5 -> Rank 1)

| Rank | Level | Source ID | Story (Cause -> Payoff -> Reaction) | Trim (`ss` / `t`) | Speed | Out Duration / Frames | `impactFrameOffset` | Punchline Text | Output File |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **5** | Level 1 | `yt:BskECLbZaMo` | NBA star Josh Hart raises hand for high-five -> teammate walks past ignoring him -> daps up own hand with deadpan stare | `0.0s` / `3.4s` | `0.85x` | `4.00s` (`120f`) | `45` | `-10,000 AURA` | `public/clips/one_million_aura_loss/rank_5.mp4` |
| **4** | Level 2 | `reddit:kctf7jav87a21` | Swagger walk on highway bridge -> swings jacket over shoulder -> sudden wind gust rips jacket into sky -> scrambles over barrier in horror | `0.0s` / `6.2s` | `1.00x` | `6.23s` (`187f`) | `85` | `-50,000 AURA` | `public/clips/one_million_aura_loss/rank_4.mp4` |
| **3** | Level 3 | `yt:ifptOxN3gdI` | High school boy smiles at camera -> runs to impress girls with flip over bench -> faceplants onto pavement & slides to their feet as they laugh | `0.0s` / `5.9s` | `1.00x` | `5.90s` (`177f`) | `105` | `-100,000 AURA` | `public/clips/one_million_aura_loss/rank_3.mp4` |
| **2** | Level 4 | `reddit:lcdi0r4po98b1` | Man leans over billiard table for flashy trickshot -> loses footing -> belly-flops flat onto green felt, snapping cue stick & scattering balls | `0.0s` / `7.5s` | `1.00x` | `7.50s` (`225f`) | `75` | `-500,000 AURA` | `public/clips/one_million_aura_loss/rank_2.mp4` |
| **1** | Level 5 | `reddit:lmumlsvaooi11` | Two friends swagger down historic stone river stairs -> one slips on stomach -> 20-step slide straight into river with giant splash -> climbs out soaked | `0.0s` / `10.0s` | `1.00x` | `10.00s` (`300f`) | `110` | `-1,000,000 AURA` | `public/clips/one_million_aura_loss/rank_1.mp4` |

---

## 4. Render, Mastering & Final QA Commands
1. **Remotion Render:**
   `npx remotion render RankingShort output/one_million_aura_loss_raw.mp4 --props=cue_sheet_one_million_aura_loss.json --overwrite` (1084 frames / 36.14s @ 30fps).
2. **EBU R128 Audio Master:**
   `ffmpeg -y -i output/one_million_aura_loss_raw.mp4 -af "loudnorm=I=-14.0:TP=-1.5:LRA=11:linear=true" -c:v copy -c:a aac -b:a 320k output/one_million_aura_loss_mastered.mp4`
3. **1fps Final QA Contact Sheet:**
   `ffmpeg -y -i output/one_million_aura_loss_mastered.mp4 -vf "fps=1,scale=260:-1,tile=6x7" -frames:v 1 -q:v 3 output/one_million_aura_loss_qa_sheet.jpg`
4. **Mandatory Owner Disclaimer:**
   `"All footages used in this video are not mine; full credit goes to the respective owners."`
