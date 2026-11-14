import subprocess
import json

files = [
    "XatCv5jfcYU.mp4",
    "6yPgDBvMLtA.mp4",
    "r_wwc67ducopq71.mp4",
    "7W5iM-7ueKs.mp4",
    "-wOo7mAyirk.mp4"
]

for f in files:
    path = f"temp_harvest/dialogue_loop_real_life/{f}"
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "stream=codec_type,codec_name,duration,channels,sample_rate",
        "-of", "json",
        path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(f"=== {f} ===")
    try:
        data = json.loads(res.stdout)
        for s in data.get("streams", []):
            print(f"  {s.get('codec_type')}: {s.get('codec_name')}, {s.get('duration')}s")
    except Exception as e:
        print(e)
