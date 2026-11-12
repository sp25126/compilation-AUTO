import json
import os
import subprocess
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMP_DIR = os.path.join(BASE_DIR, "temp_harvest", "one_million_aura_loss")
os.makedirs(TEMP_DIR, exist_ok=True)

QUERIES = [
    "trying to look cool fail shorts",
    "infinite aura loss moments shorts",
    "-1000000 aura moments shorts",
    "left hanging handshake cringe shorts",
    "trying to act tough fail shorts",
    "smooth walk slip public fail shorts",
    "trying to impress girl fail shorts",
]

def search_yt():
    seen = set()
    results = []
    for q in QUERIES:
        print(f"Searching: {q}...")
        proc = subprocess.run(
            ["py", "-3", "-m", "yt_dlp", "--js-runtimes", "node", "--flat-playlist", "--dump-json", f"ytsearch8:{q}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            encoding="utf-8",
            errors="ignore",
        )
        for line in proc.stdout.splitlines():
            if not line.strip():
                continue
            try:
                d = json.loads(line)
                vid = d.get("id")
                if not vid or vid in seen:
                    continue
                seen.add(vid)
                dur = d.get("duration") or 0
                views = d.get("view_count") or 0
                title = d.get("title", "")
                if 5 <= dur <= 45 and views >= 10000:
                    results.append({
                        "id": vid,
                        "title": title,
                        "duration": dur,
                        "views": views,
                        "url": f"https://www.youtube.com/watch?v={vid}",
                    })
                    print(f"  FOUND: [{vid}] ({dur}s, {views:,} views) {title[:60]}")
            except Exception:
                pass
    with open(os.path.join(TEMP_DIR, "candidates.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"Total candidates found: {len(results)}")

if __name__ == "__main__":
    search_yt()
