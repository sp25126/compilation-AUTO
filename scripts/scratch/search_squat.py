import json, subprocess

queries = [
    "squat fail safeties shorts",
    "squat bail fail gym shorts",
    "squat fail dumps bar backwards shorts",
    "gym blooper squat rack fail shorts",
    "squat rack funny gym fail reaction shorts"
]

results = []
seen = set()

for q in queries:
    cmd = ["py", "-3", "-m", "yt_dlp", "--flat-playlist", "--dump-json", f"ytsearch10:{q}"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8")
    out, _ = p.communicate()
    for line in out.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            d = json.loads(line)
            vid = d.get("id")
            dur = d.get("duration") or 0
            views = d.get("view_count") or 0
            title = d.get("title") or ""
            if vid and vid not in seen and 5 <= dur <= 55:
                seen.add(vid)
                results.append({"id": vid, "dur": dur, "views": views, "title": title})
        except Exception:
            pass

print(f"Total candidates found: {len(results)}")
for r in results:
    print(f"{r['id']} | {r['dur']}s | {r['views']} views | {r['title']}")

with open("temp_harvest/squat_rack_blunders/search_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
