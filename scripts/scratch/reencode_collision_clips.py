import subprocess
import os

clips = [
    {
        "rank": 5,
        "src": "temp_harvest/object_collision_fails/clip_glass_walk.mp4",
        "ss": "0.5",
        "t": "7.0",
        "frames": 210,
        "impact_offset": 93
    },
    {
        "rank": 4,
        "src": "temp_harvest/object_collision_fails/clip_phone_glass.mp4",
        "ss": "0.0",
        "t": "5.5",
        "frames": 165,
        "impact_offset": 33
    },
    {
        "rank": 3,
        "src": "temp_harvest/object_collision_fails/clip_guy_glass_window.mp4",
        "ss": "3.0",
        "t": "7.5",
        "frames": 225,
        "impact_offset": 78
    },
    {
        "rank": 2,
        "src": "temp_harvest/object_collision_fails/clip_glass_3times.mp4",
        "ss": "0.5",
        "t": "8.0",
        "frames": 240,
        "impact_offset": 55
    },
    {
        "rank": 1,
        "src": "temp_harvest/object_collision_fails/clip_ronaldo_glass.mp4",
        "ss": "5.0",
        "t": "7.5",
        "frames": 225,
        "impact_offset": 130
    }
]

out_dir = "public/clips/object_collision_fails"
os.makedirs(out_dir, exist_ok=True)

for c in clips:
    out_file = os.path.join(out_dir, f"rank_{c['rank']}.mp4")
    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-nostats", "-y",
        "-ss", c["ss"],
        "-t", c["t"],
        "-i", c["src"],
        "-r", "30",
        "-g", "15",
        "-keyint_min", "15",
        "-sc_threshold", "0",
        "-pix_fmt", "yuv420p",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        "-ar", "48000",
        out_file
    ]
    print(f"Re-encoding rank_{c['rank']}...")
    subprocess.run(cmd, check=True)

print("Re-encoding complete.")
