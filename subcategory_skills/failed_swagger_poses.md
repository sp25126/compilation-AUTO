# Sub-Category Skill: `failed_swagger_poses` ("Ranking Funniest Failed Swagger Moments")

> **MANDATORY FOR AI PIPELINE:** Every rule in this file was verified through multi-platform sourcing, 2fps visual inspection, full story-preserving CFR trimming, custom Brazilian Phonk music mastering, Remotion compositing, EBU R128 loudness mastering (`-14.9 LUFS`, True Peak `< -1.5 dBTP`), and 1fps final QA verification.

---

## 1. Subcategory Overview & Niche Positioning
- **Subcategory ID:** `failed_swagger_poses`
- **Subcategory Name:** `Failed Swagger Moments`
- **Display Title:** `Ranking Funniest Failed Swagger Moments (Swagger Fails)`
- **Niche:** `aura_debt`
- **Style Archetype:** LevelZero0ne (@MrPurifiedWater + @cliportey hybrid)
- **Key Psychology:** The psychological delight of watching someone attempt maximum arrogance, confidence, or coolness, only for reality and physics to humiliate them in an instant.

---

## 2. Core Remotion Props & Audio Architecture
1. **Remotion Composition Props (`RankingShort`):**
   - `titleHeader`: `"Ranking Funniest"`
   - `subjectHeader`: `"Failed Swagger Moments"`
   - `versionTag`: `"(Swagger Fails)"`
   - `musicBedPath`: `"public/audio/stems/failed_swagger_poses_music_bed.mp3"`
   - `musicVolume`: `0.11`
   - `showSubtitles`: `false`
   - `enableLogoPopupDemo`: `false`
2. **Category-Specific Distinct Audio Bed:**
   - **Track:** Baila Lento (Slowed + Reverb Brazilian Phonk Bass Drift)
   - **Location:** `public/audio/stems/failed_swagger_poses_music_bed.mp3`
   - **Specs:** 50.0s looped stem, 1.0s head fade-in, 2.5s tail fade-out, 192k MP3.
   - **Volume Balance:** Mixed at 11% volume under 100% natural clip foley and voices.

---

## 3. Verified 5-Clip Benchmark Table (Rank 5 -> Rank 1)

| Rank | Level | Source ID | Story Arc (Cause -> Payoff -> Reaction) | Trim Window | Speed | Out Duration / Frames | Output File |
| :---: | :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| **5** | Level 1 | `reddit:pqhozwmg723a1` | Group martial arts swagger pose attempt -> guy drops into horse stance for girls to climb -> entire human pyramid collapses in heap | `ss 01.0s, t 8.0s` | `1.00x` | `8.00s` (`240f`) | `public/clips/failed_swagger_poses/rank_5.mp4` |
| **4** | Level 2 | `reddit:6ym9uhg8qimh1` | Convertible passenger flexes and tries to flip sunglasses over nose -> wind instantly blows sunglasses into his eyeball and backseat | `ss 04.2s, t 7.5s` | `1.00x` | `7.50s` (`225f`) | `public/clips/failed_swagger_poses/rank_4.mp4` |
| **3** | Level 3 | `reddit:kctf7jav87a21` | High-altitude highway swagger walk -> swings red jacket over shoulder -> crosswind rips jacket away into abyss -> desperate barrier scramble | `ss 00.0s, t 6.2s` | `1.00x` | `6.23s` (`187f`) | `public/clips/failed_swagger_poses/rank_3.mp4` |
| **2** | Level 4 | `reddit:lcdi0r4po98b1` | Snooker table flashy trickshot pose -> leans across table -> slips and belly-flops flat onto green felt, snapping cue stick | `ss 00.0s, t 7.5s` | `1.00x` | `7.50s` (`225f`) | `public/clips/failed_swagger_poses/rank_2.mp4` |
| **1** | Level 5 | `reddit:lmumlsvaooi11` | Strutting down historic river stairs with utmost swagger -> loses footing -> 20-step stomach slide straight into water with massive splash | `ss 00.0s, t 8.0s` | `1.00x` | `8.03s` (`241f`) | `public/clips/failed_swagger_poses/rank_1.mp4` |

---

## 4. Multi-Platform Candidate Sourcing & Rejection Log
- **Candidates Harvested:** Reddit (`v.redd.it` HLS) & YouTube Shorts.
- **Rejections via 2fps Visual QA Gate:**
  - `78icpazrm3xd1`: Staged police breathalyzer skit with heavy baked-in text captions across every beat.
  - `213pdwgwk7m71`: Staged supercar Reno 911 skit with baked-in subtitles and unnatural comedic acting.
  - `rhsyn8at3we51`: Dashcam 320x320 crop with vehicle 50 meters away; action too small to discern on mobile.
  - `dChsc1LUaZ8`: Baseball fan opening bottle, broadcast stadium screen overlays and news score bugs.
  - `TNfDA1kp-1I`: Kitchen vlogger flex with twitch stream overlay and discord notification sound.

---

## 5. Technical Encoding & Mastering Commands
1. **Anti-Stutter CFR Encoding:**
   `ffmpeg -y -ss <ss> -t <dur> -i <source> -r 30 -g 15 -keyint_min 15 -sc_threshold 0 -pix_fmt yuv420p -c:v libx264 -preset fast -crf 18 -c:a aac -b:a 192k -ar 48000 public/clips/failed_swagger_poses/rank_<N>.mp4`
2. **Remotion Composition Render:**
   `npx remotion render RankingShort output/failed_swagger_poses_raw.mp4 --props=cue_sheet_failed_swagger_poses.json --overwrite` (1193 frames @ 30fps = 39.77s)
3. **EBU R128 Audio Mastering:**
   `ffmpeg -y -i output/failed_swagger_poses_raw.mp4 -af "loudnorm=I=-14:TP=-1.5:LRA=11:linear=true" -c:v copy -c:a aac -b:a 320k output/failed_swagger_poses_mastered.mp4`
4. **Loudness Verification Result:**
   - **Integrated Loudness:** `-14.9 LUFS` (Target `-14.0 ± 1.0 LUFS` -> PASS)
   - **True Peak:** `Peak < -1.5 dBTP` (Target `<= -1.5 dBTP` -> PASS)
   - **Loudness Range (LRA):** `8.1 LU`
5. **1fps Final QA Sheet:**
   `ffmpeg -y -i output/failed_swagger_poses_mastered.mp4 -vf "fps=1,scale=260:-1,tile=8x6" -frames:v 1 -update 1 -q:v 3 output/failed_swagger_poses_qa_sheet.jpg`
   - Verified 0 black frames, zero watermark defects, complete story arcs preserved from flex attempt to aftermath.
