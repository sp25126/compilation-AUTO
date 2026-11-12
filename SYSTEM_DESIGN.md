# System Design: Autonomous Viral Shorts Engine

## 1. System Goals & Operational Principles

1. **Autonomous Operation (Zero-Touch)**: Headless pipeline running without human supervision.
2. **Contextual Fidelity Over Volume**: Strict semantic gates prevent generic or miscategorized clips from entering the edit.
3. **Multi-Tier Fault Tolerance**: External API downtimes (e.g. OpenRouter rate limits or network issues) must trigger the local NLP & community consensus engine rather than halting.
4. **Broadcast Standard Audio & Video**: Strict YouTube Shorts compliance (1080x1920, 30 FPS, -14.0 LUFS, no black/white frames).
5. **Deterministic Lifecycle Isolation**: Every sub-category operates within its own isolated staging directory.

---

## 2. Data Models & Interface Contracts

### 2.1 SubCategory & Niche Interface
```typescript
export interface SubCategory {
  id: string;               // Unique slug (e.g., 'road_rage_regret')
  name: string;             // Human-readable title ('Road Rage Regret')
  strictDefinition: string; // Negative and positive semantic criteria
  negativeFilters: string[];// Banned keyword list
  audioStem: string;        // Stored in public/ audio asset
  punchlineText: string;    // Fallback meme punchline
}

export interface Niche {
  id: string;
  name: string;
  subCategories: SubCategory[];
}
```

### 2.2 Run Context Manifest (`current_run_context.json`)
```json
{
  "run_id": "run_20261109_215500",
  "locked_at": "2026-11-09T21:55:00.000Z",
  "sub_category_id": "road_rage_regret",
  "sub_category_name": "Road Rage Regret",
  "strict_definition": "Must show aggressive confrontation or intentional retaliation between drivers...",
  "negative_filters": ["fatal crash", "gore", "news report"],
  "audio_stem": "siren_short.mp3",
  "punchline_text": "INSTANT JUSTICE"
}
```

### 2.3 Arena Selection Manifest (`arena_selected.json`)
```json
[
  {
    "clip_id": "Nh41RLIpAEg",
    "file_path": "C:\\Users\\...\\public\\raw_clips\\Nh41RLIpAEg.mp4",
    "score": 9.2,
    "incident_type": "car_crash",
    "punchlineText": "BRO THOUGHT HE HAD BRAKES",
    "reason": "Clear dashcam angle of an aggressive pickup truck cutting off and crashing."
  }
]
```

### 2.4 Remotion Composition Manifest (`cue_sheet.json`)
```json
{
  "subCategoryId": "road_rage_regret",
  "subCategoryName": "ROAD RAGE REGRET",
  "audioStem": "siren_short.mp3",
  "clips": [
    {
      "videoPath": "C:\\Users\\...\\public\\clips\\road_rage_regret_1_baked.mp4",
      "durationInFrames": 135,
      "punchlineText": "BRO THOUGHT HE HAD BRAKES",
      "incidentType": "car_crash",
      "impactSfx": "heavy_metal_crunch.mp3"
    }
  ]
}
```

---

## 3. Mathematical Signal Processing Models

### 3.1 Visual Motion Delta & Jerk Analysis
Frames are downsampled to $180 \times 320$ grayscale at 6 FPS. For each frame pair $(F_{t-1}, F_t)$, the difference matrix is:
$$D(x, y) = F_t(x, y) - F_{t-1}(x, y)$$

The discrete Laplacian kernel operator is applied:
$$\nabla^2 D(x, y) = D(x+1, y) + D(x-1, y) + D(x, y+1) + D(x, y-1) - 4 D(x, y)$$

The motion variance $\sigma^2_L(t)$ is computed across all spatial pixels:
$$\sigma^2_L(t) = \text{Var}\left(\nabla^2 D\right)$$

To identify the **impact impulse** and reject continuous smooth panning, the motion acceleration (jerk) is evaluated:
$$J(t) = \max\left(0, \sigma^2_L(t) - \sigma^2_L(t-1)\right)$$

The visual score combines variance and jerk:
$$S_{visual}(t) = 0.70 \cdot \sigma^2_L(t) + 0.30 \cdot J(t)$$

### 3.2 Acoustic Transient Peak Detection
Audio is analyzed across the frequency spectrum using FFmpeg's `lavfi.astats`:
$$\text{RMS}_{dB}(t) = 20 \log_{10}\left(\sqrt{\frac{1}{N} \sum_{i=1}^N x[i]^2}\right)$$
The acoustic apex is the timestamp $t_{audio}$ maximizing $\text{RMS}_{dB}(t)$.

### 3.3 Tri-Modal Apex Fusion
The system combines acoustic transients, optical motion jerk, and physical frame VLM estimates:
- **Case 1 (Acoustic + Visual Coincidence)**: When $t_{audio} > 0$ and $|t_{audio} - t_{visual}| \le 0.5\text{ s}$ outside scene cuts:
  $$t_{apex} = 0.50 \cdot t_{audio} + 0.35 \cdot t_{visual} + 0.15 \cdot t_{vlm}$$
- **Case 2 (Acoustic + VLM Coincidence)**: When $t_{audio} > 0$ and $|t_{audio} - t_{vlm}| \le 0.8\text{ s}$:
  $$t_{apex} = 0.55 \cdot t_{audio} + 0.45 \cdot t_{vlm}$$
- **Case 3 (Visual + VLM Fusion)**: When acoustic data has no sharp spike:
  $$t_{apex} = \begin{cases}
  0.60 \cdot t_{visual} + 0.40 \cdot t_{vlm} & \text{if } |t_{visual} - t_{vlm}| \le 1.5\text{ s} \\
  t_{vlm} & \text{if } t_{vlm} > 0 \text{ and } t_{visual} \text{ triggered by scene cut} \\
  t_{visual} & \text{otherwise}
  \end{cases}$$

### 3.4 Rank-Aware Action Boundaries & Aftermath Playout
Action boundary extraction dynamically adapts consequence playout based on compilation ladder ranking:
- **Buildup Window**:
  $$t_{start} = \max(0, t_{apex} - 3.0)$$
  *Guarded by previous scene cut*: If $t_{prev\_cut}$ exists and $t_{start} < t_{prev\_cut} + 0.15$, set $t_{start} = t_{prev\_cut} + 0.15$.
- **Aftermath Playout Buffer**:
  $$\Delta t_{aftermath} = \begin{cases}
  1.5\text{ s} & \text{if Rank } 1 \text{ (Grand Finale Climax)} \\
  1.2\text{ s} & \text{if Rank } 2, 3, 4, 5 \text{ (Paced Viral Beats)}
  \end{cases}$$
- **Freeze Cut Timestamp**:
  $$t_{freeze} = \min(D_{total}, t_{apex} + \Delta t_{aftermath})$$
  *Guarded by next scene cut*: If $t_{next\_cut}$ exists and $t_{freeze} > t_{next\_cut} - 0.10$, set $t_{freeze} = t_{next\_cut} - 0.10$.
- **Freeze Hold & Acoustic Micro-Silence**:
  - Live video action plays from $t_{start}$ to $t_{freeze}$.
  - Clone freeze frame duration: $2.2\text{ s}$ via `tpad=stop_mode=clone:stop_duration=2.2,setpts=PTS-STARTPTS`.
  - Audio muted exactly 1 frame ($33.3\text{ ms}$) prior to $t_{freeze}$, padded with silence via `apad=whole_dur=target_dur`.

---

## 4. Multi-Tier Fault Tolerance & Recovery

| Failure Mode | Trigger Condition | Automated Mitigation Protocol |
|---|---|---|
| **VLM API Rate Limit (429)** | OpenRouter pool exhausted | Rotates to backup key in `OPENROUTER_API_KEYS`. If all exhausted, falls back to Level-2 NLP & Community Consensus Engine. |
| **API Timeout / JSON Error** | External service offline | Fallback Engine inspects comments, title, description, and tags with 0 downtime. |
| **Insufficient Strict Matches** | Harvester finds $< 5$ clips | Exits with status code `2`. Daemon logs fallback, advances to next sub-category, and restarts harvesting without burning API quotas. |
| **Hard Camera Scene Cut** | Edit cut spikes motion delta | Level-2 scene detector (`gt(scene,0.40)`) flags edit timestamp and selects true physical impact. |
| **Missing Google OAuth Key** | `client_secrets.json` not present | Daemon generates `output/mastered_final.mp4` for local forensic review and gracefully bypasses YouTube upload. |

---

## 5. File System & Staging Hierarchy

```
automation/
├── .env                              # Rotated API keys & provider endpoints
├── ARCHITECTURE.md                   # System Architecture & Flowcharts
├── SYSTEM_DESIGN.md                  # System Design & Mathematical Models
├── current_run_context.json          # Locked subcategory context for active run
├── candidates_meta.json              # Harvested candidate metadata
├── arena_selected.json               # Top-5 VLM ranked selections
├── cue_sheet.json                    # Remotion composition manifest
├── pipeline_history.json             # Round-robin state tracking
├── used_clips_registry.json          # Deduplication registry
├── public/
│   ├── clips/                        # Baked apex freeze MP4s (e.g. road_rage_regret_1_baked.mp4)
│   ├── raw_clips/                    # Top-5 raw clips selected by Arena
│   └── *.mp3                         # Audio stems and contextual impact SFX
├── temp_harvest_road_rage_regret/    # Isolated subcategory staging directory
├── output/
│   ├── raw_render.mp4                # Raw Remotion render output
│   └── mastered_final.mp4            # Final EBU R128 mastered deliverable
├── src/
│   ├── pipeline/NicheGraph.ts        # 10 Niches & 50 Subcategories with strict definitions
│   ├── remotion/
│   │   ├── Compilation.tsx           # Dual-layer, dynamic ladder HUD, -11° kinetic punchlines
│   │   ├── Root.tsx                  # Remotion root registration
│   │   └── index.ts                  # Remotion entry point
│   └── services/
│       ├── mastering.ts              # EBU R128 two-pass loudnorm service
│       ├── sound_designer.ts         # Incident-type SFX mapper & ducking rules
│       └── supabase.ts               # Cloud telemetry & analytics persistence
└── scripts/
    ├── auto_daemon.py                # Autonomous master daemon orchestrator
    ├── harvester.py                  # Agent-Reach Exa crawler & downloader
    ├── fallback_analyzer.py          # Level-2 NLP & community consensus analyzer
    ├── llm_verifier.py               # Multimodal VLM semantic filter
    ├── arena_scorer.py               # VLM Arena ranker & punchline synthesizer
    ├── visual_evaluator.py           # Level-2 frame-perfect apex & freeze baker
    └── youtube_uploader.py           # YouTube Data API release scheduler
```
