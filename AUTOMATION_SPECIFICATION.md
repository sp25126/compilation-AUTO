# Viral YouTube Shorts Ranking Engine: Full Automation Architecture & Specification

## 1. Executive Summary & Vision
The goal of this automation is to build a **100% autonomous, zero-touch YouTube Shorts production and publishing pipeline**. The system automatically harvests verified, situational video moments across **10 distinct entertainment niches** (encompassing **50 specialized sub-categories**), visually inspects clip motion and climax moments to eliminate premature cuts, edits them into high-retention Top 5 countdown Shorts using Remotion, masters the audio to YouTube broadcast compliance (-14 LUFS), and publishes or schedules them directly to a linked YouTube channel via the YouTube Data API v3.

---

## 2. System Architecture Diagram

```
┌────────────────────────────────────────────────────────────────────────┐
│               SCHEDULER / CRON TRIGGER (Daily / Hourly)                │
│             Windows Task Scheduler / PM2 / GitHub Actions             │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ triggers
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                    NICHE GRAPH ORCHESTRATOR                            │
│                 (src/pipeline/NicheGraph.ts)                           │
│  - Selects target Niche & Sub-Category Node                            │
│  - Reads situation fingerprint, negative filters, and audio stems       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ invokes
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│            SITUATION HARVESTING & VISUAL EVALUATOR                     │
│               (scripts/visual_evaluator.py)                            │
│  1. Queries YouTube Shorts search with situational keywords            │
│  2. Filters: Duration (3-60s), Views (>=1,000+), Negative filters       │
│  3. Decodes video frames via FFmpeg pipe (180x320 @ 6 fps)             │
│  4. Computes discrete Laplacian variance & motion delta vectors        │
│  5. Locates Climax / Apex moment & ensures full aftermath playout      │
│  6. Bakes trimmed clips with aftermath hold (+0.8s to +1.4s)          │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ passes approved assets
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                  REMOTION VIDEO COMPOSITION ENGINE                     │
│                  (src/remotion/Compilation.tsx)                        │
│  - 9:16 Vertical HD canvas (1080x1920 @ 30 fps)                        │
│  - Dual-layer: Gaussian blurred background + centered crisp video      │
│  - Top header banner with custom neon dual-gradient styling            │
│  - Rank countdown HUD (5 -> 4 -> 3 -> 2 -> 1)                          │
│  - Clean presentation for Ranks 5-2 (zero repetitive clutter)          │
│  - Rank 1 Grand Finale kinetic punchline typography                    │
│  - High-memory Webpack bundle execution (--max-old-space-size=4096)    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ renders raw MP4
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                BROADCAST AUDIO MASTERING ENGINE                        │
│                           (FFmpeg)                                     │
│  - Applies EBU R128 two-pass loudnorm filter                           │
│  - Target: -14.0 ± 1.0 LUFS, True Peak <= -1.5 dBTP, LRA <= 11         │
│  - Re-encodes audio stream to 320 kbps AAC                             │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ mastered MP4 + Manifest
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│               YOUTUBE UPLOADER & SCHEDULING QUEUE                      │
│                  (scripts/youtube_uploader.py)                         │
│  - Generates viral titles, retention tags, description, and comments   │
│  - Calculates scheduled release times (staggered 24-hr windows)        │
│  - Uploads via YouTube Data API v3 (OAuth 2.0 Desktop client)         │
│  - Tracks status in output/upload_schedule_queue.json                  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. The 10 Niches & 50 Sub-Category Pipeline Graph

The system divides short-form viral content into 10 dedicated niches, each containing 5 specialized situational sub-categories:

### 1. Human Physical Fails (`human_fails`)
*Description: The iconic "This Is The End" format—gravity defeats, hammocks, slips, and inevitable falls.*
- **People Accepting Fate** (`people_accepting_fate`): A person sliding, falling, or getting vacuumed where they completely stop struggling and accept doom.
- **Battling Gravity and Losing** (`battling_gravity_losing`): Person desperately trying to stay balanced on ice, rope, or ladder and failing.
- **Clumsy Moments In Public** (`clumsy_moments_public`): Dropping items, tripping over stairs, or walking into poles in public.
- **Overconfident People Humbled** (`overconfident_humbled`): Person boasting or attempting a dangerous stunt they clearly cannot pull off.
- **Moments Before Impact** (`moments_before_impact`): High-speed object or person flying towards camera/ground, freezing inches before impact.

### 2. Instant Regret & Karma (`instant_karma`)
*Description: Instant physical retribution for bad choices, defying warning signs, and taunting.*
- **Defying Warning Signs** (`defying_warning_signs`): Person ignoring warning sign (wet paint, thin ice, wet cement) and facing immediate disaster.
- **Pranks Backfired Instantly** (`pranks_backfired_instantly`): A prankster attempting a scare or trick, immediately getting countered.
- **Taunting Animals Gone Wrong** (`taunting_animals_gone_wrong`): Person teasing a goose, goat, or dog, getting immediately charged.
- **Road Rage Instant Justice** (`road_rage_instant_justice`): Aggressive tailgater or brake checker getting caught by an unmarked police car or ditch.
- **Cocky Challengers Humbled** (`cocky_challengers_humbled`): Person flexing or showboating before an arm wrestle or race and getting embarrassed.

### 3. Funny Animals & Pets (`funny_animals`)
*Description: Slapstick pet physics, unpredictable animal behavior, and slow-motion face reveals.*
- **Pets Being Dumb** (`pets_being_dumb`): Real pet miscalculating a physical jump, sliding into a wall, or getting stuck.
- **Pets Being Smart** (`pets_being_smart`): Pet opening complex locks, using tools, or outsmarting owner/other pet.
- **Animal Funny Moments** (`animal_funny_moments`): Pure unexpected slapstick chaos caused by an animal in a living room.
- **Pets In Slow Motion** (`pets_revealing_true_self`): Pet jumping or catching food in slow motion with unhinged faces.
- **Animals Becoming Scarier** (`animal_becoming_scarier`): Docile pet suddenly locking eyes, standing on hind legs, or moving unnaturally.

### 4. Aura Debt & Loss (`aura_debt`)
*Description: The Gen-Z "-1,000,000 Aura" format—trying to look cool, devastating public embarrassments.*
- **Moments That Cost Infinite Aura** (`moments_cost_infinite_aura`): Person trying to pull off an effortless cool move, completely wiping out.
- **Trying To Look Cool Gone Wrong** (`trying_to_look_cool_gone_wrong`): Stepping out of a sports car, flipping sunglasses, and falling into a puddle.
- **High Stakes Aura Gambles** (`high_stakes_aura_gambles`): Going for an unnecessary flashy skill, immediately getting countered.
- **Devastating Public Stumbles** (`devastating_public_stumbles`): High school or college student taking a dramatic tumble in a crowded hallway.
- **Romantic Aura Debt Fails** (`romantic_aura_debt_fails`): Awkward missed handshakes, rejected hugs, or leaning in for a kiss on live TV.

### 5. Sports & Athletic Bloopers (`sports_bloopers`)
*Description: Premature celebrations, trickshot disasters, and goalkeeper brainfades.*
- **Athletes Celebrating Too Early** (`athletes_celebrating_too_early`): Runner slowing down to taunt, getting passed at the finish line by 1 inch.
- **Trickshot Disasters** (`trickshot_disasters`): Attempting an elaborate basketball or pool trickshot, smashing a ceiling lamp or TV.
- **Goalkeeper Brainfades** (`goalkeeper_brainfades`): Goalie throwing ball directly to opposing striker or watching ball trickle over line.
- **Gymnast Routine Mishaps** (`gymnast_routine_mishaps`): Vault or balance beam landing overshooting into foam pit or sliding off mat.
- **Referee Collision Disasters** (`referee_collision_disasters`): Referee inadvertently tackling a player or blocking a goal-bound shot.

### 6. Real Life NPC Glitches (`npc_glitches`)
*Description: People frozen in place, broken pathfinding, and synchronized stranger actions.*
- **Unrendered Game NPCs** (`unrendered_game_npcs`): Person standing in an unnatural T-pose or staring blankly into space on the subway.
- **Dialogue Loop Real Life** (`dialogue_loop_real_life`): Person repeating the exact same vocal phrase or gesture like an unskippable cutscene.
- **Pathfinding AI Broken** (`pathfinding_ai_broken`): Person walking into a glass door multiple times, or trapped in a revolving door.
- **Object Collision Fails** (`object_collision_fails`): Person attempting to interact with an object as if physical collision mesh failed.
- **NPC Idle Animations** (`npc_idle_animations`): Multiple strangers doing the exact same bizarre synchronized movement.

### 7. Workplace & Job Disasters (`workplace_disasters`)
*Description: High-stakes warehouse dominos, kitchen disasters, and delivery fails.*
- **Worst Shift Of Their Lives** (`worst_shift_of_their_lives`): Worker watching an entire pallet of paint, soda, or flour collapse.
- **Forklift Domino Disasters** (`forklift_domino_disasters`): Warehouse forklift nudging one rack, triggering a warehouse-wide shelf collapse.
- **Commercial Kitchen Nightmares** (`commercial_kitchen_nightmares`): Chef flipping a pancake or dropping a 5-tier wedding cake in slow motion.
- **Retail Display Rampage** (`retail_display_rampage`): Shopper pulling one bottom item from a wine pyramid, sending 500 bottles crashing.
- **Delivery Driver Mishaps** (`delivery_driver_mishaps`): Package slipping on icy porch, throwing delivery box over roof.

### 8. Extreme Luck & Near Misses (`extreme_luck`)
*Description: One-in-a-million saves, runaway tire dodges, and physics-defying recoveries.*
- **Used All Luck For Life** (`used_all_their_luck_for_life`): Pedestrian dodging a falling tree or runaway tire by 2 inches, completely unfazed.
- **Accidental Trickshots Caught** (`accidental_trickshots_caught`): Dropping keys or water bottle, kicking it by accident, landing upright in cup.
- **Physics Defying Saves** (`physics_defying_saves`): Bicycle rider crashing into hood, front flipping, and landing smoothly on their feet.
- **Unintentional Hero Catches** (`unintentional_hero_catches`): Dad or stranger catching falling cup, phone, or child without looking.
- **Crazy Vehicle 360 Recoveries** (`crazy_vehicle_recoveries`): Car spinning 360 degrees on icy highway, exiting cleanly into lane.

### 9. Gym & Fitness Bloopers (`gym_bloopers`)
*Description: Ego lifting gone wrong, treadmill slingshots, and spotters disappearing.*
- **Bench Press Ego Fails** (`bench_press_fails`): Lifter loading 3x their max on bench press, getting pinned or dumping plates off the sides.
- **Treadmill Slingshots** (`treadmill_slingshots`): Person cranking treadmill speed to max, losing footing, and getting launched backwards.
- **Squat Rack Bloopers** (`squat_rack_blunders`): Lifter hitting bottom of squat, unable to stand up, rolling backward onto safeties.
- **Using Equipment Completely Wrong** (`gym_equipment_confusions`): Person hanging upside down from cable crossover or using machines backwards.
- **Spotter Distracted Bloopers** (`gym_spotter_fails`): Spotter looking at phone while lifter struggles and drops the barbell.

### 10. Nature & Weather Surprises (`nature_weather`)
*Description: Rogue winds, surprise waves, icy driveway slides, and sudden natural interruptions.*
- **Sudden Wind Ruining Events** (`sudden_wind_ruining_events`): Microburst gust of wind flipping an entire wedding tent, bounce house, or trampoline.
- **Rogue Waves Catching People** (`rogue_waves_catching_beachgoers`): Calm beach suddenly overtaken by a surprise surge washing towels and chairs away.
- **Ice Driveway Survival Fails** (`slipping_down_ice_driveways`): Person taking trash can out on black ice, sliding uncontrollably down the entire driveway.
- **Wildlife Close Calls** (`wildlife_close_calls`): Tourists approaching a bison or bear, animal making sudden charge, human panicking.
- **Lightning Strike Jump Scares** (`lightning_jump_scares`): Person casually filming rain on porch, lightning striking 15 feet away with explosive boom.

---

## 4. Technical Implementation Details

### A. Situational Visual Evaluator (`scripts/visual_evaluator.py`)
To prevent premature clip cuts and bad context matching:
1. **Zero-Dependency Vectorized Processing:** Uses `ffprobe` for metadata and pure NumPy discrete Laplacian convolution matrix kernels:
   $$\nabla^2 I = I_{x+1, y} + I_{x-1, y} + I_{x, y+1} + I_{x, y-1} - 4 I_{x, y}$$
   Computes texture clarity and frame-to-frame absolute pixel motion deltas without heavy native OpenCV binaries.
2. **Climax & Aftermath Hold:** Locates the peak motion timestamp ($t_{\text{apex}}$). Calculates dynamic buildup:
   $$t_{\text{start}} = \max(0, t_{\text{apex}} - 3.0)$$
   $$t_{\text{live\_duration}} = t_{\text{apex}} - t_{\text{start}} + 0.8\text{s}$$
   Holds the final settling frame for 1.0s (1.4s on Rank 1) so viewers register the physical consequence before transition.

### B. Remotion Composition Engine (`src/remotion/Compilation.tsx`)
1. **Dynamic Roster Sequence:** Iterates through Ranks 5, 4, 3, 2, 1 with precise frame arithmetic:
   ```tsx
   <Sequence from={clip.startFrame} durationInFrames={clip.durationInFrames}>
     <IncidentClip item={clip} isRank1={clip.rank === 1} />
   </Sequence>
   ```
2. **Visual Hierarchy & Clutter Elimination:**
   - Rank numbers (5, 4, 3, 2, 1) displayed on the left HUD with glowing accents.
   - Video area is kept 100% clean and unencumbered during Ranks 5 to 2.
   - Rank 1 features animated kinetic punchline typography popping in word-by-word with color highlights.

### C. Broadcast Audio Compliance
Every rendered Short is mastered through an automated FFmpeg filter:
```bash
ffmpeg -y -i input.mp4 -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:v copy -c:a aac -b:a 320k mastered.mp4
```
This guarantees compliance with YouTube Shorts loudness standards (-14 LUFS ± 1.0, True Peak <= -1.5 dBTP), preventing algorithmic down-ranking caused by audio clipping or volume disparity.

### D. Automated YouTube Channel Uploader (`scripts/youtube_uploader.py`)
- **Direct API Uploads:** Authenticates using Google OAuth 2.0 with the YouTube Data API v3 (`https://www.googleapis.com/auth/youtube.upload`).
- **Viral Metadata Manifest:** Every video generates a corresponding manifest JSON containing:
  - Viral high-CTR title (tested against algorithm patterns)
  - Algorithmic description with chapter timestamps and hashtags
  - Pinned engagement question to maximize viewer comment response rates
  - Relevant category ID (e.g., Comedy `23`, Sports `17`, Entertainment `24`)
- **Automated Scheduling Queue:** Uploads can be queued with a specified `publishAt` ISO-8601 UTC timestamp for automated staggered release.

---

## 5. Daily Autonomous Execution Workflow

To run this pipeline automatically every day on a schedule:

### Step 1: Link YouTube Channel (One-Time Setup)
1. In Google Cloud Console, enable the **YouTube Data API v3**.
2. Create an **OAuth 2.0 Client ID (Desktop Application)**.
3. Download the credentials as `client_secrets.json` into `shorts-ranking-engine/`.
4. Run once to authenticate:
   ```powershell
   npm --prefix shorts-ranking-engine run youtube:publish
   ```

### Step 2: Automated Daily Job (Windows Task Scheduler / Cron)
Create a daily scheduled task executing `scripts/cron_daily_runner.py`:
```python
# Selects next sub-category in circular rotation from NicheGraph
# Runs: npm run graph:run -- --sub=<next_id>
# Runs: npm run youtube:schedule -- --manifest <manifest_path>
# Runs: npm run youtube:publish
```

This ensures a steady, hands-off release schedule of fresh, algorithm-optimized Shorts across all 10 niches.

