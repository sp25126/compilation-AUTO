import subprocess
import json
import sys

queries = [
    "he accepted his fate fail shorts",
    "accepted his fate fail funny shorts",
    "person accepts fate fail shorts",
    "this is the end fail funny shorts",
    "moments before disaster accepting fate shorts"
]

results = []
seen_ids = set()

for q in queries:
    print(f"[Search] Query: {q}")
    cmd = [
        "py", "-3", "-m", "yt_dlp",
        f"ytsearch10:{q}",
        "--dump-json",
        "--skip-download",
        "--no-playlist"
    ]
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="ignore")
        stdout, _ = proc.communicate(timeout=45)
        for line in stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
                vid_id = d.get("id")
                dur = d.get("duration", 0)
                title = d.get("title", "")
                if vid_id and vid_id not in seen_ids and dur and dur <= 60:
                    seen_ids.add(vid_id)
                    results.append({
                        "id": vid_id,
                        "title": title,
                        "duration": dur,
                        "url": f"https://www.youtube.com/watch?v={vid_id}"
                    })
                    print(f"  -> Found: {vid_id} ({dur}s): {title}")
            except Exception:
                pass
    except Exception as e:
        print(f"Error for query {q}: {e}")

print(f"\n[Total Unique Candidates Found]: {len(results)}")
with open("candidates_fate.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
