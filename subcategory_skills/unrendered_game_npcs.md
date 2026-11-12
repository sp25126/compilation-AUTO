# Subcategory Skill: `unrendered_game_npcs` — Real-Life NPC Glitches

## Overview
- **Niche:** `npc_glitches`
- **Title Header:** `Ranking Funniest`
- **Subject Header:** `Real-Life NPC Glitches`
- **Version Tag:** `(Matrix Broken)`
- **Resolution / FPS:** `1080x1920 @ 30fps`
- **Music Bed:** `public/audio/stems/unrendered_game_npcs_music_bed.mp3` — *The Elder Scrolls IV: Oblivion - Harvest Dawn* (48s trim, 1s fade-in, 2s fade-out, mixed at low background volume ~0.11 so 100% natural clip audio remains clear).

## Sourcing & Visual QA Rules
- **Reddit (`agent-reach reddit search`):** `"glitchinthematrix npc behavior v.redd.it"`, `"tooktoomuch npc moment v.redd.it"`, `"funny npc caught on camera v.redd.it"`, `"npc in real life v.redd.it"`, `"real life npc glitch v.redd.it"`, `"oblivion npc irl v.redd.it"`.
- **YouTube (`yt-dlp`):** `"real life npc moments caught on camera shorts"`, `"people acting like npcs in real life shorts"`, `"matrix glitch funny moments shorts"`, `"Glitched NPC in real life"`.
- **2fps QA Rejections:** Rejected TikTok watermarked clips (`r_ncifyihhdaaa1`, `r_315ep2gxaz781`, `r_qfdz2ctmr6db1`, `r_vd9nyay5lm581`), The Sun watermarked clip (`r_2n9opzdgw5te1`), baked-in game UI/text overlays (`r_5gxinbifpwga1`, `r_xyopuusclt991`), actual GTA V gameplay (`yt_BdBKPFCBKXk`), and dark/unreadable or too-short clips (`r_lqvhkh7ev2ha1`, `r_rmn1wyx0hbz31`, `r_2l93xnvfcjvb1`).

## 5-Clip Benchmark Table (Rank 5 [Level 1] -> Rank 1 [Level 5])

| Rank | Level | Source ID | Trim / Speed | Out Duration (Frames) | Story (Cause -> Payoff -> Reaction) |
|---|---|---|---|---|---|
| 5 | Level 1 | `yt_jNERSokQAbE` | `0.0s–5.9s` (1.0x) | `5.93s` (178f) | Vlogger talking on sidewalk -> yellow-shirt NPC freezes, stares deadpan, and glitches sideways out of frame |
| 4 | Level 2 | `r_o4lnmhjovz5d1` | `23.0s–31.5s` (1.0x) | `8.50s` (255f) | Crowd clapping/cheering -> politician stands frozen like an AFK NPC, then does a delayed robotic fist pump |
| 3 | Level 3 | `r_9ozb1vt4q8341` | `5.5s–16.5s` (1.3x) | `8.47s` (254f) | Commuters walk up subway stairs around a corner -> immediately turn and walk back down in a pathfinding loop |
| 2 | Level 4 | `r_vbgeqzsf4fk81` | `0.0s–8.0s` (1.0x) | `7.97s` (239f) | Live street interview -> cyclist NPC with zero collision detection rides straight into pedestrian, knocking him down |
| 1 | Level 5 | `r_n9cxcl8okmu71` | `1.5s–13.0s` (1.35x) | `8.53s` (256f) | Man outside store walks straight into a brick wall, stays stuck leaning against it, backs up and resets |

## Pipeline Commands
1. **Trim & Normalize:** `1080x1920`, `30fps`, `yuv420p`, `libx264 -crf 18`, `aac 192k 48000Hz` stereo (with blurred-background framing for non-9:16 sources).
2. **Remotion Render:** `npx remotion render RankingShort output/unrendered_game_npcs_raw.mp4 --props=cue_sheet_unrendered_game_npcs.json --overwrite`
3. **EBU R128 Mastering:** `ffmpeg -i output/unrendered_game_npcs_raw.mp4 -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:v copy -c:a aac -b:a 320k -y output/unrendered_game_npcs_mastered.mp4`
4. **Final 1fps QA:** `ffmpeg -y -i output/unrendered_game_npcs_mastered.mp4 -vf "fps=1,scale=260:-1,tile=8x6" -frames:v 1 -q:v 3 output/unrendered_game_npcs_qa_sheet.jpg`
