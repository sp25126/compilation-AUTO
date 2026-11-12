import json
import os
import re
import subprocess
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMP_DIR = os.path.join(BASE_DIR, "temp_harvest")
os.makedirs(TEMP_DIR, exist_ok=True)


def run_agent_reach_reddit(query: str, limit: int = 8) -> list[str]:
    cmd = ["agent-reach", "reddit", "search", query, "--limit", str(limit)]
    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=25,
            shell=(sys.platform == "win32"),
        )
        if proc.returncode == 0 and proc.stdout:
            data = json.loads(proc.stdout.strip())
            urls = []
            for item in data.get("items", []):
                u = item.get("url", "")
                text = item.get("text", "")
                if "v.redd.it" in text and "/comments/" in u:
                    urls.append(u)
            return urls
    except Exception as e:
        print(f"[Reddit search note] {e}")
    return []


def search_yt_social(query: str, min_views: int = 5000) -> list[dict]:
    proc = subprocess.run(
        ["py", "-3", "-m", "yt_dlp", "--js-runtimes", "node", "--flat-playlist", "--dump-json", query],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        encoding="utf-8",
        errors="ignore",
    )
    hits = []
    for line in proc.stdout.splitlines():
        if not line.strip():
            continue
        try:
            d = json.loads(line)
            vid = d.get("id")
            dur = d.get("duration") or 0
            views = d.get("view_count") or 0
            if vid and 4 <= dur <= 35 and views >= min_views:
                hits.append({
                    "id": vid,
                    "dur": dur,
                    "views": views,
                    "title": d.get("title", "")[:80],
                    "url": f"https://www.youtube.com/watch?v={vid}",
                })
        except Exception:
            pass
    return hits


def download_clip(url: str, out_prefix: str) -> str | None:
    out_tpl = os.path.join(TEMP_DIR, f"{out_prefix}.%(ext)s")
    proc = subprocess.run(
        [
            "py", "-3", "-m", "yt_dlp", "--js-runtimes", "node",
            "-f", "bv*[height<=1080]+ba/b[height<=1080]/b",
            "--merge-output-format", "mp4",
            "-o", out_tpl,
            url,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=45,
    )
    target = os.path.join(TEMP_DIR, f"{out_prefix}.mp4")
    if os.path.exists(target):
        return target
    return None


def main():
    reddit_urls = []
    for q in ["instant karma v.redd.it", "instant regret karma v.redd.it", "convenient cop v.redd.it"]:
        for u in run_agent_reach_reddit(q, limit=6):
            if u not in reddit_urls:
                reddit_urls.append(u)

    print(f"Found {len(reddit_urls)} Reddit v.redd.it candidates")
    downloaded = []
    for idx, u in enumerate(reddit_urls[:6]):
        p = download_clip(u, f"karma_reddit_{idx+1}")
        if p:
            print(f"  [Reddit] Downloaded {os.path.basename(p)} <- {u}")
            downloaded.append(p)

    # Also search TikTok & Instagram Reels mirrors
    yt_hits = []
    for q in [
        "ytsearch10:instant karma tiktok fail",
        "ytsearch10:instant karma reels caught on camera",
        "ytsearch10:road rage instant karma caught on camera",
    ]:
        yt_hits.extend(search_yt_social(q, min_views=5000))

    seen = set()
    unique_hits = []
    for h in sorted(yt_hits, key=lambda x: x["views"], reverse=True):
        if h["id"] not in seen:
            seen.add(h["id"])
            unique_hits.append(h)

    print(f"Found {len(unique_hits)} TikTok/Instagram/YouTube candidates")
    for idx, h in enumerate(unique_hits[:6]):
        p = download_clip(h["url"], f"karma_social_{h['id']}")
        if p:
            print(f"  [Social] Downloaded {os.path.basename(p)} ({h['views']:,} views): {h['title']}")
            downloaded.append(p)

    # Generate 2fps contact sheets for all downloaded files
    for p in downloaded:
        base = os.path.basename(p).replace(".mp4", "")
        sheet = os.path.join(TEMP_DIR, f"sheet_{base}.jpg")
        subprocess.run(
            ["ffmpeg", "-y", "-i", p, "-vf", "fps=2,scale=260:-1,tile=8x10", "-frames:v", "1", "-q:v", "3", sheet],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print(f"  [Sheet] {sheet}")


if __name__ == "__main__":
    main()
