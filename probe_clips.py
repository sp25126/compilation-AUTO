import subprocess
import json

total_frames = 0
clip_infos = []

for rank in range(1, 6):
    path = f"public/clips/love_at_first_sight_caught/rank_{rank}.mp4"
    cmd = [
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=nb_frames,duration,width,height,r_frame_rate",
        "-of", "json", path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    data = json.loads(res.stdout)["streams"][0]
    frames = int(data.get("nb_frames") or round(float(data["duration"]) * 30))
    dur = float(data["duration"])
    total_frames += frames
    print(f"Rank {rank}: {dur:.3f}s | {frames} frames | {data['width']}x{data['height']} | {data['r_frame_rate']}")
    clip_infos.append({"rank": rank, "frames": frames, "duration": dur})

print(f"\nTotal video duration: {total_frames / 30.0:.2f}s ({total_frames} frames)")
