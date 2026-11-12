import json
import os
import subprocess
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REGISTRY_PATH = os.path.join(BASE_DIR, "src", "pipeline", "master_category_registry.json")

def run_agent_reach_yt_search(query: str, limit: int = 5) -> list[dict]:
    """
    Executes Agent-Reach YouTube search action to find live viral shorts & compilations.
    """
    cmd = ["agent-reach", "youtube", "search", query, "--limit", str(limit)]
    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=20,
            shell=(sys.platform == "win32")
        )
        if proc.returncode == 0 and proc.stdout:
            data = json.loads(proc.stdout.strip())
            if data.get("ok") and "items" in data:
                return data["items"]
    except Exception as e:
        print(f"[YT Researcher] Agent-Reach search note: {e}", file=sys.stderr)
    return []

def run_agent_reach_yt_read(video_id_or_url: str) -> dict:
    """
    Reads video title, channel, description, and metadata using Agent-Reach.
    """
    cmd = ["agent-reach", "youtube", "read", video_id_or_url]
    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=20,
            shell=(sys.platform == "win32")
        )
        if proc.returncode == 0 and proc.stdout:
            data = json.loads(proc.stdout.strip())
            if data.get("ok") and "items" in data and data["items"]:
                return data["items"][0]
    except Exception as e:
        print(f"[YT Researcher] Agent-Reach read note: {e}", file=sys.stderr)
    return {}

def discover_trending_compilation_topic() -> dict:
    """
    Discovers the highest-velocity trending compilation topic on YouTube Shorts right now.
    """
    print("\n[YT Researcher] Querying YouTube for trending ranking compilations...", file=sys.stderr)
    trending_queries = [
        "ranking instant karma shorts",
        "ranking this is the end shorts",
        "ranking best of moments shorts",
        "ranking funny moments shorts"
    ]
    
    findings = []
    for tq in trending_queries:
        items = run_agent_reach_yt_search(tq, limit=3)
        for it in items:
            raw = it.get("raw") or {}
            findings.append({
                "title": it.get("title", ""),
                "url": it.get("url", ""),
                "views": raw.get("view_count", 0) or 0,
                "duration": raw.get("duration", 0) or 0,
                "query": tq
            })

    # Sort by views / relevance
    findings.sort(key=lambda x: x["views"], reverse=True)
    
    # Determine winning trending category
    top_hit = findings[0] if findings else {
        "title": "Ranking Instant Karma Moments",
        "views": 1920000,
        "query": "instant karma"
    }

    # Match to our 50-subcategory taxonomy
    if "karma" in top_hit["title"].lower() or "justice" in top_hit["title"].lower() or "cop" in top_hit["title"].lower():
        selected_sub = "road_rage_instant_justice"
        niche = "instant_karma"
        header = "Instant Karma Moments"
        version_tag = "(Justice Version)"
        stem = "siren_short.mp3"
        punchline = "INSTANT KARMA"
    elif sub_category_id == "pets_being_dumb":
        metadata = {
            "sub_category_id": sub_category_id,
            "recommended_title": "Ranking Funniest Pets Sharing 0 Braincells 😂🐾 #shorts #pets #funnyanimals",
            "alt_titles": [
                "Ranking Best Of Pets Being Dumb Moments 😭🐶 #shorts #cats #dogs",
                "0 Braincell Pet Moments Ranked 😂🔥 #shorts #viral #animals",
            ],
            "description": (
                "Level 1 rolls off the table, Level 5 forgets glass exists 😭🐾\n\n"
                "Which pet moment made you laugh the hardest — 5, 4, 3, 2, or 1? 👇\n\n"
                "All footages used in this video are not mine; full credit goes to the respective owners.\n\n"
                "#shorts #viral #trending #fyp #funnyanimals #pets #cats #dogs #youtubeshorts "
                "#comedy #catvideos #dogvideos #viralvideo #explore #ytshorts #trendingshorts #trynottolaugh #ranking"
            ),
            "tags": [
                "shorts",
                "viral",
                "trending",
                "fyp",
                "funny animals",
                "pets being dumb",
                "funny cats",
                "funny dogs",
                "ranking best of",
                "try not to laugh",
                "youtubeshorts",
                "trendingshorts",
            ],
            "category": "Pets & Animals",
            "upload_schedule": {
                "primary_ist": "Today, 7:30 PM IST (9:00 AM EST) — India evening + US morning Shorts overlap",
                "secondary_us_peak_ist": "Tomorrow, 3:30 AM IST (5:00 PM EST) — Peak US after-school/evening scroll",
            },
        }
    else:
        selected_sub = "people_accepting_fate"
        niche = "human_fails"
        header = "This Is The End Moments"
        version_tag = "(Surrender Version)"
        stem = "skyfall_this_is_the_end.mp3"
        punchline = "THIS IS THE END"

    result = {
        "trending_topic": top_hit["title"],
        "view_count": top_hit["views"],
        "niche_id": niche,
        "sub_category_id": selected_sub,
        "title_header": "Ranking Best Of",
        "subject_header": header,
        "version_tag": version_tag,
        "audio_stem": stem,
        "punchline_text": punchline,
        "research_hits": findings[:5]
    }
    
    print(f"[YT Researcher] Selected Trending Niche: '{niche}' -> Subcategory: '{selected_sub}' ({punchline})", file=sys.stderr)
    return result

def generate_upload_metadata(sub_category_id: str = "people_accepting_fate") -> dict:
    """
    Uses Agent-Reach YouTube research to benchmark viral titles, descriptions, hashtags,
    and optimal upload windows for the given sub-category, and writes output/upload_metadata.json.
    """
    ref_data = run_agent_reach_yt_read("https://www.youtube.com/shorts/JMtRMZavYY0")
    search_hits = run_agent_reach_yt_search("Ranking The Funniest This Is The End Moments", limit=5)

    if sub_category_id == "people_accepting_fate":
        metadata = {
            "sub_category_id": sub_category_id,
            "recommended_title": "Ranking Best Of \"This Is The End\" Moments 💀😂",
            "alt_titles": [
                "Ranking The Funniest This Is The End Moments 😂💀",
                "Ranking 5 People Who Accepted Their Fate 💀😭",
            ],
            "description": (
                "Level 1 starts with a slip, Level 5 is pure surrender 😭💀\n\n"
                "Which moment had you laughing the hardest — 5, 4, 3, 2, or 1? 👇\n\n"
                "#shorts #ranking #thisistheend #fails #funny #memes #instantregret #viral"
            ),
            "tags": [
                "this is the end",
                "this is the end moments",
                "ranking best of",
                "people accepting their fate",
                "funny fails",
                "ranking shorts",
                "viral fails",
                "memes",
                "shorts",
            ],
            "category": "Entertainment",
            "upload_schedule": {
                "primary_ist": "Today, 7:30 PM IST (9:00 AM EST) — Best overlap for India evening + US morning Shorts feed",
                "secondary_us_peak_ist": "Tomorrow, 3:30 AM IST (5:00 PM EST) — Peak US after-school/evening scroll",
                "why": "Thursday evening / Friday morning windows capture high weekend-warmup Shorts retention; publishing 30–60 min before peak lets initial 30-min seed velocity build.",
            },
            "benchmark_reference": {
                "title": ref_data.get("title"),
                "author": ref_data.get("author"),
                "views": (ref_data.get("raw") or {}).get("view_count"),
                "published_at": ref_data.get("published_at"),
                "search_sample_count": len(search_hits),
            },
        }
    elif sub_category_id == "pets_being_dumb":
        metadata = {
            "sub_category_id": sub_category_id,
            "recommended_title": "Ranking Funniest Pets Sharing 0 Braincells 😂🐾 #shorts #pets #funnyanimals",
            "alt_titles": [
                "Ranking Best Of Pets Being Dumb Moments 😭🐶 #shorts #cats #dogs",
                "0 Braincell Pet Moments Ranked 😂🔥 #shorts #viral #animals",
            ],
            "description": (
                "Level 1 rolls off the table, Level 5 forgets glass exists 😭🐾\n\n"
                "Which pet moment made you laugh the hardest — 5, 4, 3, 2, or 1? 👇\n\n"
                "All footages used in this video are not mine; full credit goes to the respective owners.\n\n"
                "#shorts #viral #trending #fyp #funnyanimals #pets #cats #dogs #youtubeshorts "
                "#comedy #catvideos #dogvideos #viralvideo #explore #ytshorts #trendingshorts #trynottolaugh #ranking"
            ),
            "tags": [
                "shorts",
                "viral",
                "trending",
                "fyp",
                "funny animals",
                "pets being dumb",
                "funny cats",
                "funny dogs",
                "ranking best of",
                "try not to laugh",
                "youtubeshorts",
                "trendingshorts",
            ],
            "category": "Pets & Animals",
            "upload_schedule": {
                "primary_ist": "Today, 7:30 PM IST (9:00 AM EST) — India evening + US morning Shorts overlap",
                "secondary_us_peak_ist": "Tomorrow, 3:30 AM IST (5:00 PM EST) — Peak US after-school/evening scroll",
            },
        }
    else:
        metadata = {
            "sub_category_id": sub_category_id,
            "recommended_title": "Ranking Best Of Instant Karma Moments 😂💀 #shorts #funny #instantkarma",
            "alt_titles": [
                "Ranking 5 Craziest Instant Karma Moments 💀😂 #shorts #viral #karma",
                "Don't Get Cocky: Instant Karma Ranked 😂🔥 #shorts #fails #trending",
            ],
            "description": (
                "Level 1 starts with a prank, Level 5 goes straight into the river 😭💀\n\n"
                "Which Instant Karma moment was your favorite — 5, 4, 3, 2, or 1? 👇\n\n"
                "All footages used in this video are not mine; full credit goes to the respective owners.\n\n"
                "#shorts #viral #trending #fyp #funny #instantkarma #fails #memes #youtubeshorts "
                "#comedy #karma #viralvideo #explore #ytshorts #trendingshorts #laugh #trynottolaugh #ranking"
            ),
            "tags": [
                "shorts",
                "viral",
                "trending",
                "fyp",
                "instant karma",
                "instant karma moments",
                "ranking best of",
                "funny",
                "fails",
                "memes",
                "try not to laugh",
                "comedy",
                "youtubeshorts",
                "trendingshorts",
                "karma",
            ],
            "category": "Entertainment",
            "upload_schedule": {
                "primary_ist": "Today, 7:30 PM IST (9:00 AM EST) — India evening + US morning Shorts overlap",
                "secondary_us_peak_ist": "Tomorrow, 3:30 AM IST (5:00 PM EST) — Peak US after-school/evening scroll",
            },
        }

    out_path = os.path.join(BASE_DIR, "output", "upload_metadata.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    return metadata


CANDIDATE_SUBCATEGORIES = [
    {
        "sub_id": "athletes_celebrating_too_early",
        "niche": "sports_bloopers",
        "subject_header": "Premature Celebrations",
        "version_tag": "(Too Early Edition)",
        "query": "celebrating too early fail shorts",
        "reddit_query": "premature celebration v.redd.it",
    },
    {
        "sub_id": "moments_cost_infinite_aura",
        "niche": "aura_debt",
        "subject_header": "Infinite Aura Loss Moments",
        "version_tag": "(-1000000 Aura)",
        "query": "infinite aura loss fail shorts",
        "reddit_query": "watchpeopledieinside aura fail v.redd.it",
    },
    {
        "sub_id": "defying_warning_signs",
        "niche": "instant_karma",
        "subject_header": "Ignoring Warning Signs",
        "version_tag": "(What Could Go Wrong)",
        "query": "ignoring warning signs fail shorts",
        "reddit_query": "whatcouldgowrong warning sign v.redd.it",
    },
    {
        "sub_id": "overconfident_humbled",
        "niche": "human_fails",
        "subject_header": "Overconfident People Humbled",
        "version_tag": "(Ego Checked Edition)",
        "query": "overconfident fail humbled shorts",
        "reddit_query": "instant_regret overconfident v.redd.it",
    },
    {
        "sub_id": "pets_being_smart",
        "niche": "funny_animals",
        "subject_header": "200 IQ Smart Pet Moments",
        "version_tag": "(Genius Edition)",
        "query": "smart pets 200 iq moments shorts",
        "reddit_query": "smart dog cat opens door v.redd.it",
    },
    {
        "sub_id": "taunting_animals_gone_wrong",
        "niche": "instant_karma",
        "subject_header": "Taunting Animals Gone Wrong",
        "version_tag": "(Wrong Target Edition)",
        "query": "taunting animals gone wrong shorts",
        "reddit_query": "animalsbeingjerks goose attack v.redd.it",
    },
]


def rank_trending_subcategories(limit: int = 4) -> list[dict]:
    """
    Step 0 / Step A Pipeline Integration:
    Queries live YouTube view counts via Agent-Reach for candidate sub-categories
    and returns the top `limit` highest-velocity trending sub-categories.
    """
    ranked = []
    for cand in CANDIDATE_SUBCATEGORIES:
        items = run_agent_reach_yt_search(cand["query"], limit=4)
        top_views = 0
        top_title = ""
        for it in items:
            raw = it.get("raw") or {}
            v = raw.get("view_count") or 0
            if v > top_views:
                top_views = v
                top_title = it.get("title", "")
        ranked.append({
            **cand,
            "top_views": top_views,
            "top_trending_title": top_title,
        })
    ranked.sort(key=lambda x: x["top_views"], reverse=True)
    return ranked[:limit]


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--rank-trending":
        lim = int(sys.argv[2]) if len(sys.argv) > 2 else 4
        top_cats = rank_trending_subcategories(lim)
        print(json.dumps(top_cats, indent=2, ensure_ascii=False))
    elif len(sys.argv) > 1 and sys.argv[1] == "--metadata":
        sub_id = sys.argv[2] if len(sys.argv) > 2 else "people_accepting_fate"
        meta = generate_upload_metadata(sub_id)
        print(json.dumps(meta, indent=2, ensure_ascii=False))
    else:
        trend = discover_trending_compilation_topic()
        print(json.dumps(trend, indent=2))
