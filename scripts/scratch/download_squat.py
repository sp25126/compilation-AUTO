import subprocess, os

# Target candidate IDs to download
candidates = [
    "sBq5rpF3wrc", # How to safely fail a squat (1.1M views, 13s)
    "cam4HcVlFu8", # Epic squat re-rack fail (68k views, 10s)
    "LpSFwM1m4h4", # Epic Squat Fail at IPF Worlds (30k views, 14s)
    "jv5QJ56NxEs", # Gym fail ?! Squat fail ?! 230 (51k views, 41s)
    "Dtpu8aIaePo", # Coach almost loses life showing off (18k views, 31s)
    "TqJu8rY4eps", # 260 kg 573 lb squat fail fall (14k views, 51s)
    "GS8EtKn6ZJw", # Guy Fails to Balance Weights (6.8k views, 20s)
    "HqnyraDVmBM", # FRONT SQUAT DANGEROUS FAIL (2.4k views, 24s)
    "yR7jqQeZqwE", # Using safety bars for a failed squat (31s)
    "LzCq7YCkuOw", # EPIC FRONT SQUAT FAIL (28s)
    "NSXMHAc5i-A", # why I don't squat with safeties (17s)
]

for vid in candidates:
    out_tmpl = f"temp_harvest/squat_rack_blunders/{vid}.%(ext)s"
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "--merge-output-format", "mp4",
        "-o", out_tmpl,
        f"https://www.youtube.com/watch?v={vid}"
    ]
    print(f"Downloading {vid}...")
    try:
        subprocess.run(cmd, check=True)
    except Exception as e:
        print(f"Error downloading {vid}: {e}")

print("Downloads finished.")
