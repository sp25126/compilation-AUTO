# System Architecture: Autonomous Viral Shorts Engine

## 1. Executive Overview

The **Autonomous Viral Shorts Engine** is an end-to-end, headless production system that transforms multi-platform internet footage into viral compilation shorts (1080x1920 @ 30 FPS). The pipeline operates autonomously 24/7 without human intervention, incorporating:
- **Upfront Niche Decision & Locking**: Immutably binds each production cycle to a designated niche before ingestion begins.
- **Agent-Reach Sourcing**: Multi-query crawler across 3 specific search queries per subcategory using Exa semantic search and Reddit community boards (`/r/IdiotsInCars`, `/r/PublicFreakout`, `/r/AnimalsBeingDerps`).
- **Dual-Gate Verification**: Multimodal 3-frame VLM physical action validation (15% Setup, 60% Apex, 90% Settling) backed by an offline 50-subcategory NLP Community Consensus Fallback Engine.
- **Tri-Modal Apex Calibration**: Scene-cut guarded motion jerk ($d^3x/dt^3$) detection, acoustic RMS spike synchronization, and VLM apex estimation with rank-aware aftermath buffers (+1.5s for Rank 1, +1.2s for Ranks 2–5).
- **Remotion Composition**: Dual-layer ambient blurred background, dynamic left-docked rank ladder HUD (1–5), and staggered word-by-word kinetic punchline typography tilted at `-11°`.
- **Broadcast Audio Mastering**: Two-pass EBU R128 loudness normalization (`-14.0 LUFS ± 1.0`, True Peak `≤ -1.5 dBTP`).

---

## 2. High-Level Architecture Diagram

```mermaid
flowchart TD
    subgraph Step0["Step 0: Niche Determination & Lock-in"]
        NG[NicheGraph: 10 Niches / 50 Subcategories] --> Lock[Lock Run Context: current_run_context.json]
        Lock --> Iso[Create Isolated Staging Directory]
    end

    subgraph Step1["Step 1: Multi-Platform Ingestion"]
        Iso --> AR[Agent-Reach CLI / Exa Semantic Engine]
        AR -->|Crawl Links| Targets[Reddit, TikTok, YouTube Shorts URLs]
        Targets --> Meta[yt-dlp Metadata Extraction]
    end

    subgraph Step2["Step 2: Dual-Gate Semantic Validation"]
        Meta --> GatePrimary{OpenRouter VLM API Online?}
        GatePrimary -->|Yes| VLM[VLM Semantic & Reality Filter]
        GatePrimary -->|Timeout / Failure / 429| Fallback[Level-2 Heuristic Community Consensus Engine]
        Fallback --> Comments[Inspect Top Comments, Title, Description, Tags]
        Comments --> Lexicon[Lexical Niche Scoring & Disqualification]
        VLM --> Decision{Passes Rule 1 & Rule 2?}
        Lexicon --> Decision
        Decision -->|Pass| DL[Download & Stage Raw MP4]
        Decision -->|Reject / Exit 2| FallbackNiche[Advance Niche without burning API key]
    end

    subgraph Step3["Step 3: Arena Scoring & Incident Tagging"]
        DL --> Arena[Arena Scorer: 3 Keyframes + Metadata]
        Arena --> Rank[Top-5 Selection, Incident Type, & Punchline]
        Rank --> SelectedManifest[arena_selected.json]
    end

    subgraph Step4["Step 4: Next-Level Frame-Perfect Evaluator"]
        SelectedManifest --> SceneCut[FFmpeg Scene Cut Detector: gt(scene, 0.40)]
        SceneCut --> MotionJerk[Laplacian Variance & Motion Acceleration: d(Var)/dt]
        MotionJerk --> AudioSpike[lavfi.astats RMS Spike Detection]
        AudioSpike --> ApexFusion[Tri-Modal Fusion: Audio + Visual Jerk + VLM Apex]
        ApexFusion --> RankBuffer{Rank 1 Finale?}
        RankBuffer -->|Rank 1| Buff15[Aftermath Buffer: +1.5s]
        RankBuffer -->|Rank 2-5| Buff12[Aftermath Buffer: +1.2s]
        Buff15 --> Bake[Bake Clone Freeze Frame: tpad 2.2s + PTS Recalculation]
        Buff12 --> Bake
        Bake --> MicroSilence[Cut Native Audio 1 Frame Early + apad Silence Padding]
    end

    subgraph Step5["Step 5: Composition, Mastering & Scheduling"]
        MicroSilence --> Remotion[Remotion Headless Composition: cue_sheet.json]
        Remotion --> DynamicHUD[Dynamic Ranking Ladder 1-5 + SFX]
        DynamicHUD --> Render[output/raw_render.mp4]
        Render --> Loudnorm[EBU R128 2-Pass Audio Mastering: -14 LUFS]
        Loudnorm --> Final[output/mastered_final.mp4]
        Final --> YouTube[YouTube Data API: Schedule UTC +6h]
    end
```

---

## 3. Subsystem Breakdown

### 3.1 Upfront Niche Decision & Locking
- Before querying or downloading any media, the pipeline executes `step_a_select_sub_category()`.
- Generates an immutable `current_run_context.json`:
  ```json
  {
    "run_id": "run_20261109_215500",
    "locked_at": "2026-11-09T21:55:00Z",
    "sub_category_id": "road_rage_regret",
    "sub_category_name": "Road Rage Regret",
    "strict_definition": "Must show aggressive confrontation or intentional retaliation between drivers. Reject generic bad driving, traffic violations, or riding on the wrong side of the road.",
    "negative_filters": ["fatal crash", "gore", "news report"],
    "audio_stem": "siren_short.mp3",
    "punchline_text": "INSTANT JUSTICE"
  }
  ```
- All worker scripts isolate staging in `temp_harvest_<sub_category_id>/` and `public/clips/<sub_category_id>/`.

### 3.2 Agent-Reach Ingestion Layer
- Bridges AI agents directly to the web using the official `agent-reach` CLI tool (`v1.6.1`).
- Utilizes Exa semantic web queries targeting high-signal Reddit dashcam boards (`/r/IdiotsInCars`, `/r/PublicFreakout`), TikTok viral links, and YouTube Shorts.
- Resolves candidate URLs and extracts high-resolution streams via `yt-dlp`.

### 3.3 Dual-Gate Semantic Verification
1. **Primary Gate (OpenRouter VLM API):**
   - Routes to `openrouter/auto` using rotated `OPENROUTER_API_KEYS`.
   - Checks Rule 1 (100% real-life footage) and Rule 2 (Exact niche definition match).
2. **Secondary Gate (Heuristic Community Consensus Engine):**
   - Triggers automatically if the external AI API times out, returns HTTP 429, or fails.
   - Inspects the top 20 comments, video title, description, and tags.
   - Disqualifies CGI, video games (GTA, BeamNG, Roblox), animations, and scripted comedy.
   - Confirms true road-rage incidents via community consensus markers (*"he got what he deserved"*, *"instant karma"*, *"dashcam never lies"*, *"satisfying"*).

### 3.4 Level-2 Frame-Perfect Visual Evaluator
- **Hard Scene-Cut Detection**: Filters out camera transitions via `select='gt(scene,0.40)'` to prevent false motion triggers. Guards boundaries: $t_{\text{start}} \ge t_{\text{prev\_cut}} + 0.15\text{s}$, $t_{\text{freeze}} \le t_{\text{next\_cut}} - 0.10\text{s}$.
- **Laplacian Variance & Jerk ($d^2\Delta / dt^2$)**: Analyzes 6 FPS grayscale frames and calculates acceleration of variance to identify physical impact.
- **Audio RMS Spike Alignment**: Computes peak decibels using `lavfi.astats.Overall.RMS_level`.
- **Tri-Modal Apex Fusion**: Fuses acoustic transient peak ($t_{\text{audio}}$), optical motion jerk ($t_{\text{visual}}$), and VLM physical verification apex estimate ($t_{\text{vlm}}$).
- **Rank-Aware Aftermath Playout**:
  - Starts $3.0\text{ s}$ before apex: $t_{start} = \max(0, t_{apex} - 3.0)$.
  - Plays $+1.5\text{ s}$ consequence aftermath for Rank 1 (grand finale climax).
  - Plays $+1.2\text{ s}$ consequence aftermath for regular ranks (Ranks 2–5).
- **Impact Cut & Clone Freeze**:
  - Mutes native audio exactly 1 frame ($33.3\text{ ms}$) before freeze.
  - Clones the apex frame for $2.2\text{ s}$ via `-vf "tpad=stop_mode=clone:stop_duration=2.2,setpts=PTS-STARTPTS"`.
  - Pads audio with silence across the full freeze hold via `-af "apad=whole_dur=target_dur"`, preventing container truncation.

### 3.5 Remotion Staging & Composition
- **Video Dimensions**: 1080x1920 (9:16 vertical ratio).
- **Background Layer**: Ambient fill with `blur(24px) brightness(0.4)`.
- **Foreground Layer**: Centered video with `objectFit: contain` and `drop-shadow(0 16px 40px rgba(0,0,0,0.8))`.
- **Left-Hand Ranking Ladder**: Ranks 1 to 5 docked at `left: 45px, top: 230px`, animating on active clip with spring scale ($1.0 \to 1.15$).
- **Kinetic Punchline**: Staggered word-by-word typography tilted at `-11°`, bouncing onto the screen during the freeze frame.

### 3.6 Mastering & Distribution
- **Loudness Compliance**: EBU R128 two-pass normalization target `-14.0 LUFS ± 1.0`, True Peak $\le -1.5\text{ dBTP}$, LRA 11.
- **Encoding**: 320 kbps AAC, H.264 High Profile (`crf 18`).
- **Scheduling**: YouTube Data API v3 release schedule set to $\text{UTC} + 6\text{ hours}$.
