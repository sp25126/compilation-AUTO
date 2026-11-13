import urllib.request
import json
import os

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
url = "https://www.reddit.com/r/nevertellmetheodds/search.json?q=trickshot+OR+accidental+OR+bounce&restrict_sr=on&sort=top&t=all&limit=25"

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        posts = data["data"]["children"]
        print(f"Got {len(posts)} posts from r/nevertellmetheodds:")
        for p in posts:
            post = p["data"]
            title = post.get("title")
            ups = post.get("ups")
            is_video = post.get("is_video")
            post_url = post.get("url")
            print(f"[{ups} ups] {title} -> {post_url} (is_video={is_video})")
except Exception as e:
    print(f"Reddit fetch error: {e}")
