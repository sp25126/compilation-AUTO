# Pipeline Operational Specification & Forensic QA

## 1. Execution Commands

### Full Headless Run (Targeted Category)
```powershell
python scripts/auto_daemon.py --sub-category road_rage_regret
```

### Full Headless Run (Automated Round-Robin across 50 Subcategories)
```powershell
python scripts/auto_daemon.py
```

### Forensic Review Mode (Render & Master, Skip YouTube Upload)
```powershell
python scripts/auto_daemon.py --sub-category road_rage_regret --skip-upload
```

### Standalone Component Execution & Debugging

#### 1. Agent-Reach Harvester
```powershell
python scripts/harvester.py --query "Road Rage Regret" --definition "Must show aggressive confrontation or intentional retaliation between drivers." --count 5 --min-matches 3 --temp-dir temp_harvest_road_rage_regret
```

#### 2. Level-2 Semantic Fallback Engine
```powershell
python scripts/fallback_analyzer.py "Karen Gets INSTANT KARMA in Road Rage Fight!" "Aggressive driver cut off truck and faced instant justice"
```

#### 3. Multimodal VLM Semantic Verifier
```powershell
python scripts/llm_verifier.py --title "Road rage driver tries to cut off truck and crashes" --description "Instant karma on highway" --thumbnail "https://i.ytimg.com/vi/bDyhzmH8hfw/hqdefault.jpg"
```

#### 4. Next-Level Visual & Audio Impact Evaluator
```powershell
python scripts/visual_evaluator.py --input "public/raw_clips/clip.mp4" --output "public/clips/baked_clip.mp4" --id "road_rage_regret_1"
```

#### 5. Remotion Render
```powershell
npm run render
```

#### 6. EBU R128 Audio Mastering
```powershell
npx ts-node src/services/mastering.ts --input output/raw_render.mp4 --output output/mastered_final.mp4
```

---

## 2. Forensic Quality Assurance (QA) Checklist

Before releasing any video to production:

- [ ] **Upfront Niche Lock**: Does `current_run_context.json` match the target theme before harvesting?
- [ ] **0% Non-Real Content**: Are video games (GTA, BeamNG, Roblox), CGI, anime, and staged PSAs completely rejected?
- [ ] **Contextual Match**: Does every single clip depict the exact action defined in `strictDefinition`?
- [ ] **Impact Cut Timing**: Does the video play the full buildup, capture the collision/impact, and show exactly $1.5\text{ seconds}$ of consequence aftermath?
- [ ] **Micro-Silence**: Does native audio mute completely $1\text{ frame}$ ($33.3\text{ ms}$) before the freeze frame begins?
- [ ] **Clone Freeze Frame**: Is the visual frozen cleanly for exactly $2.2\text{ seconds}$ using `tpad=stop_mode=clone`?
- [ ] **Contextual SFX**: Is the correct sound effect (e.g. `heavy_metal_crunch.mp3` or `tires_screech.mp3` for car crashes) dropped on the freeze frame rather than an unfitting cartoon boing?
- [ ] **Visual Hierarchy**:
  - Center framing with blurred ambient background fill (`blur(24px) brightness(0.4)`).
  - Left-hand ladder HUD (1–5) docked at `left: 45px, top: 230px` scaling dynamically with spring physics.
  - Kinetic meme punchline tilted at `-11°` with word-by-word pop-in animation during the freeze frame.
- [ ] **Audio Loudness**: Does `output/mastered_final.mp4` meet YouTube Shorts standard: $-14.0 \pm 1.0\text{ LUFS}$, True Peak $\le -1.5\text{ dBTP}$?
