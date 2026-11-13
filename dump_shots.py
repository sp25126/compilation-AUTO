import json
import subprocess
import os

with open("temp_harvest/love_at_first_sight_caught/shot_cuts.json") as f:
    shots = json.load(f)

os.makedirs("temp_harvest/love_at_first_sight_caught/all_shots", exist_ok=True)
src = "temp_harvest/love_at_first_sight_caught/cand_stare4min.mp4"

long_shots = [s for s in shots if (s["end"] - s["start"]) >= 2.5]
print(f"Total long shots: {len(long_shots)}")

for s in long_shots:
    idx = s["index"]
    mid = (s["start"] + s["end"]) / 2.0
    dur = s["end"] - s["start"]
    out_img = f"temp_harvest/love_at_first_sight_caught/all_shots/shot_{idx}_{s['start']:.1f}_{dur:.1f}s.jpg"
    subprocess.run([
        "ffmpeg", "-y", "-ss", f"{mid:.2f}", "-i", src,
        "-vframes", "1", "-q:v", "3", out_img
    ], capture_output=True)
    print(f"Shot {idx}: {s['start']:.2f}s to {s['end']:.2f}s ({dur:.2f}s) -> {out_img}")
