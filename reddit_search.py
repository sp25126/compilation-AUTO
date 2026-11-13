import urllib.request
import json

subreddits = ["MadeMeSmile", "wholesomepranks", "wholesomegifs", "ContagiousLaughter", "aww"]
results = []

for sub in subreddits:
    url = f"https://www.reddit.com/r/{sub}/search.json?q=prank+husband+OR+boyfriend+OR+wife+OR+couple&restrict_sr=1&limit=25"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        res = urllib.request.urlopen(req, timeout=10)
        data = json.loads(res.read().decode())
        posts = data.get("data", {}).get("children", [])
        for p in posts:
            d = p.get("data", {})
            p_url = d.get("url", "")
            title = d.get("title", "")
            score = d.get("score", 0)
            if "v.redd.it" in p_url:
                results.append({"sub": sub, "title": title, "url": p_url, "score": score})
    except Exception as e:
        print(f"Error on {sub}: {e}")

print(f"Found {len(results)} reddit video posts:")
for r in sorted(results, key=lambda x: x["score"], reverse=True):
    print(f"[{r['score']} pts, r/{r['sub']}] {r['title']} -> {r['url']}")

with open("temp_harvest/couple_pranks_gone_wholesome/reddit_candidates.json", "w") as f:
    json.dump(results, f, indent=2)
