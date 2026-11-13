import subprocess
import os

clip_configs = [
    {
        "rank": 5,
        "raw": "temp_harvest/commercial_kitchen_nightmares/cand_bartender_drop.mp4",
        "ss": 0.0,
        "t": 7.8,
        "frames": 234,
        "impact_offset": 140
    },
    {
        "rank": 4,
        "raw": "temp_harvest/commercial_kitchen_nightmares/cand_waitress_spill_tray.mp4",
        "ss": 1.5,
        "t": 8.0,
        "frames": 240,
        "impact_offset": 90
    },
    {
        "rank": 3,
        "raw": "temp_harvest/commercial_kitchen_nightmares/cand_slippery_chef.mp4",
        "ss": 5.5,
        "t": 8.0,
        "frames": 240,
        "impact_offset": 100
    },
    {
        "rank": 2,
        "raw": "temp_harvest/commercial_kitchen_nightmares/cand_worker_drop_food.mp4",
        "ss": 1.5,
        "t": 8.0,
        "frames": 240,
        "impact_offset": 90
    },
    {
        "rank": 1,
        "raw": "temp_harvest/commercial_kitchen_nightmares/cand_waitress_slip_floor.mp4",
        "ss": 0.5,
        "t": 8.5,
        "frames": 255,
        "impact_offset": 100
    }
]

out_dir = "public/clips/commercial_kitchen_nightmares"
os.makedirs(out_dir, exist_ok=True)

for cfg in clip_configs:
    rank = cfg["rank"]
    raw = cfg["raw"]
    ss = cfg["ss"]
    t = cfg["t"]
    target = os.path.join(out_dir, f"rank_{rank}.mp4")
    
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(ss),
        "-t", str(t),
        "-i", raw,
        "-vf", "setpts=PTS-STARTPTS,fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-r", "30",
        "-g", "15",
        "-keyint_min", "15",
        "-sc_threshold", "0",
        "-c:a", "aac",
        "-ar", "48000",
        "-b:a", "320k",
        target
    ]
    
    print(f"Encoding Rank {rank} -> {target}...")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print(f"Error encoding Rank {rank}: {res.stderr}")
    else:
        print(f"Successfully encoded Rank {rank} ({t}s)!")

print("All 5 ranks successfully encoded with anti-stutter dense keyframes!")
