import subprocess
import json
import os

queries = [
    "people repeating same phrase npc glitch funny shorts",
    "real life npc dialogue loop funny shorts",
    "strangers saying same thing at same time funny",
    "npc dialogue loop in public funny cctv shorts",
    "real life glitch npc repeating sentence shorts",
    "real life npc dialogue loop",
    "talking at the same time npc glitch funny shorts",
    "repeating the same words npc glitch shorts"
]

downloaded = set()
for f in os.listdir("temp_harvest/dialogue_loop_real_life"):
    if f.endswith(".mp4"):
        downloaded.add(f.split(".")[0])

for q in queries:
    print(f"--- Query: {q} ---")
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        "--js-runtimes", "node",
        "--flat-playlist",
        "--dump-json",
        f"ytsearch10:{q}"
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        for line in res.stdout.strip().split("\n"):
            if not line:
                continue
            data = json.loads(line)
            vid_id = data.get("id")
            dur = data.get("duration") or 0
            views = data.get("view_count") or 0
            title = data.get("title", "")
            
            # criteria: 5s to 35s, views >= 15000
            # ignore obvious gaming titles
            lower_title = title.lower()
            if any(w in lower_title for w in ["gta", "fortnite", "roblox", "minecraft", "gameplay", "animation", "tadc"]):
                continue
                
            if 5 <= dur <= 35 and views >= 15000:
                print(f"Candidate: [{vid_id}] {dur}s, {views} views: {title}")
                target = f"temp_harvest/dialogue_loop_real_life/{vid_id}.mp4"
                if not os.path.exists(target) and vid_id not in downloaded:
                    dl_cmd = [
                        "py", "-3", "-m", "yt_dlp",
                        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                        "-o", target,
                        f"https://www.youtube.com/watch?v={vid_id}"
                    ]
                    subprocess.run(dl_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    downloaded.add(vid_id)
    except Exception as e:
        print(f"Error: {e}")

print("Search & download complete.")
