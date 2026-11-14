import json
import glob
import os

candidates = []
for p in glob.glob("temp_harvest/animals_becoming_scarier/search*.json"):
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if not line.strip():
                continue
            try:
                data = json.loads(line)
                candidates.append({
                    "id": data.get("id"),
                    "title": data.get("title"),
                    "duration": data.get("duration"),
                    "view_count": data.get("view_count"),
                    "url": f"https://www.youtube.com/watch?v={data.get('id')}"
                })
            except Exception as e:
                pass

seen = set()
unique = []
for c in candidates:
    if c["id"] and c["id"] not in seen:
        seen.add(c["id"])
        dur = c.get("duration") or 0
        if 5 <= dur <= 50:
            unique.append(c)

print(f"Total valid candidates: {len(unique)}")
for u in unique:
    print(f"{u['id']} | dur:{u['duration']}s | {u['title']}")

with open("temp_harvest/animals_becoming_scarier/candidates.json", "w", encoding="utf-8") as out:
    json.dump(unique, out, indent=2)
