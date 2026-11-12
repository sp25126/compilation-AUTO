# Subcategory Skill: Defying Warning Signs (`defying_warning_signs`)

## Category Metadata
- **Subcategory ID:** `defying_warning_signs`
- **Subcategory Name:** `IGNORING WARNING SIGNS`
- **Title Header:** `Ranking Best Of`
- **Subject Header:** `Ignoring Warning Signs`
- **Version Tag:** `(What Could Go Wrong)`
- **Audio Bed:** `public/audio/stems/karma_comedy_master.mp3` (mixed at `0.11` under `1.0` natural clip audio)
- **Target Loudness:** `-14.0 LUFS` / `-1.5 dBTP`

## Sourcing Queries
- **Reddit (`agent-reach reddit search`):**
  - `whatcouldgowrong thin ice v.redd.it`
  - `whatcouldgowrong wet paint sign v.redd.it`
  - `idiotsincars road closed flood v.redd.it`
  - `whatcouldgowrong electric fence v.redd.it`
- **YouTube (`yt-dlp ytsearch10`):**
  - `walking on thin ice fail #shorts`
  - `driving through flood fail #shorts`
  - `wet cement fail caught on camera #shorts`
  - `do not touch electric fence fail #shorts`
  - `wet floor sign slip fail #shorts`

## QA & Rejection Criteria (2fps Contact Sheet Gate)
- **Rejected:**
  - `r_38nqjt7da5451` (news station watermark top-right)
  - `r_f4pqeqx54yu61` (`newsflare` watermark bottom-left)
  - `r_lfdvcnammsr41` (truncated before ice plunge)
  - `r_s6w9f5ry7ov81` (nighttime dark/unreadable)
  - `yt_CjVYJwOswrQ` (192x144 low resolution)

## Final 5-Clip Benchmark Table (Rank 5 -> Rank 1)

| Rank | Clip ID | Source | Story (Cause -> Payoff -> Reaction) | Speed | Out Duration | Frames (30fps) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **5 (Level 1)** | `rank5_wet_floor.mp4` | YouTube (`uZQoZMGwuCw`) | Walks right past bright yellow "WET FLOOR" sign in restaurant -> wipes out flat on back -> gets up embarrassed | 1.25x | 7.27s | 218 |
| **4 (Level 2)** | `rank4_electric_fence.mp4` | Reddit (`v.redd.it/0pfstggo33b51`) | Touches electric fence despite warning -> gets zapped & screams -> bolts up deck stairs & trips flat | 1.00x | 5.87s | 176 |
| **3 (Level 3)** | `rank3_wet_concrete.mp4` | YouTube (`T9ZX0ED4a8U`) | Dog ignores cones/barriers -> sprints straight across freshly poured wet concrete driveway -> full trail of paw prints | 1.25x | 6.83s | 205 |
| **2 (Level 4)** | `rank2_electric_mat_bear.mp4` | YouTube (`84woEFap1G8`) | Bear walks past orange warning sign onto electric welcome mat -> gets zapped -> bolts backwards off porch | 1.40x | 9.44s | 283 |
| **1 (Level 5)** | `rank1_thin_ice.mp4` | Reddit (`v.redd.it/yc36s68gmlq61`) | Runs out onto thin ice bridge -> ice cracks under feet -> plunges into freezing lake | 1.25x | 8.87s | 266 |

**Total Compiled Duration:** `38.27s` (`1148` frames @ 30fps)
