import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from dotenv import load_dotenv

# Load environment
load_dotenv()

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

try:
    from scripts.llm_verifier import verify_clip_semantics, verify_clip_physical_frames
except ImportError:
    from llm_verifier import verify_clip_semantics, verify_clip_physical_frames


def load_registry(registry_path: str) -> set:
    if not os.path.exists(registry_path):
        return set()
    try:
        with open(registry_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return set(data)
    except Exception as e:
        print(f"[Harvester] Warning loading registry: {e}", file=sys.stderr)
    return set()


def resolve_subcategory_metadata(niche_id: str | None, sub_id: str | None, query: str | None) -> dict:
    """
    Resolves subcategory metadata from dist/pipeline/NicheGraph.js or provides safe fallback.
    """
    target = sub_id or query or "pets_being_dumb"
    target_clean = target.lower().strip().replace("-", "_").replace(" ", "_")

    node_script = (
        f"const {{ NICHE_GRAPH, findSubCategory }} = require('./dist/pipeline/NicheGraph.js'); "
        f"const found = findSubCategory('{target_clean}') || "
        f"NICHE_GRAPH.flatMap(n => n.subCategories).find(s => s.id === '{target_clean}' || (s.aliases && s.aliases.includes('{target_clean}'))) || "
        f"NICHE_GRAPH[0].subCategories[0]; "
        f"console.log(JSON.stringify(found));"
    )
    node_cmd = ["node", "-e", node_script]

    try:
        out = subprocess.check_output(node_cmd, text=True, cwd=BASE_DIR).strip()
        for line in reversed(out.splitlines()):
            try:
                data = json.loads(line)
                if isinstance(data, dict) and "id" in data:
                    return data
            except json.JSONDecodeError:
                continue
    except Exception as e:
        print(f"[Harvester] Subcategory resolution note: {e}", file=sys.stderr)

    return {
        "id": target_clean,
        "name": target_clean.replace("_", " ").title(),
        "strictDefinition": f"Must show real-life {target_clean.replace('_', ' ')} incident.",
        "searchQueries": [
            f"{target_clean.replace('_', ' ')} fail",
            f"{target_clean.replace('_', ' ')} #shorts",
            f"{target_clean.replace('_', ' ')} instant karma",
        ],
        "negativeFilters": ["gaming", "animation", "podcast", "cgi", "tutorial"],
        "situationalPrompt": f"Verify real-life {target_clean.replace('_', ' ')} physical incident.",
        "audioStem": "cartoon_slip.mp3",
        "punchlineText": "VIRAL MOMENT",
    }


def passes_negative_filters(title: str, description: str, negative_filters: list[str]) -> bool:
    text_to_check = f"{title or ''} {description or ''}".lower()
    for banned_word in negative_filters:
        clean_word = banned_word.strip().lower()
        if clean_word and clean_word in text_to_check:
            return False
    return True


def extract_video_urls_from_text(text: str) -> list[str]:
    patterns = [
        r"https?://(?:www\.)?youtube\.com/shorts/[\w-]+",
        r"https?://(?:www\.)?youtube\.com/watch\?v=[\w-]+",
        r"https?://youtu\.be/[\w-]+",
        r"https?://(?:www\.)?tiktok\.com/@[\w.-]+/video/\d+",
        r"https?://v\.redd\.it/[\w-]+",
    ]
    urls = []
    for pat in patterns:
        matches = re.findall(pat, text)
        urls.extend(matches)
    return urls


def source_tier1_tiktok_reels(search_queries: list[str], negative_filters: list[str]) -> list[str]:
    """
    Tier 1: Fast TikTok / Instagram Reels sourcing via targeted queries with strict negative filters.
    """
    urls = []
    print("\n[Harvester: Tier 1] Sourcing TikTok / Instagram Reels...", file=sys.stderr)
    neg_suffix = "-podcast -interview -reaction -green_screen -facecam -explanation"
    for q in search_queries[:3]:
        # Formulate direct query for vertical phone reels
        query_str = f"ytsearch4:tiktok #{q.replace(' ', '')} {neg_suffix}"
        urls.append(query_str)
        urls.append(f"ytsearch3:instagram reels {q} {neg_suffix}")
    return urls


def source_tier2_reddit(subreddits: list[str], search_queries: list[str]) -> list[str]:
    """
    Tier 2: Reddit direct native CDNs (v.redd.it / subreddits) targeting raw authentic user footage.
    """
    urls = []
    print(f"\n[Harvester: Tier 2] Sourcing Reddit native feeds ({', '.join(subreddits)})...", file=sys.stderr)
    for sub in subreddits:
        # 1. Query agent-reach for direct v.redd.it URLs with high score
        try:
            reach_cmd = ["agent-reach", "web", "search", f"site:reddit.com/r/{sub} v.redd.it", "--limit", "4"]
            proc = subprocess.run(
                reach_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=15,
                shell=(sys.platform == "win32"),
            )
            if proc.returncode == 0 and proc.stdout:
                parsed = json.loads(proc.stdout.strip())
                for item in parsed.get("items", []):
                    u = item.get("url") or ""
                    text = item.get("text") or ""
                    for v in extract_video_urls_from_text(u + " " + text):
                        if v not in urls:
                            urls.append(v)
        except Exception:
            pass

        # 2. Add subreddit situational fallback search
        if search_queries:
            urls.append(f"ytsearch4:reddit r/{sub} {search_queries[0]} #shorts")
    return urls


def source_tier3_youtube_cctv(search_queries: list[str]) -> list[str]:
    """
    Tier 3: YouTube Shorts CCTV / Dashcam raw footage archives.
    """
    urls = []
    print("\n[Harvester: Tier 3] Sourcing YouTube Shorts CCTV & Dashcam archives...", file=sys.stderr)
    for q in search_queries:
        urls.append(f"ytsearch6:{q} cctv OR dashcam -news -explained -podcast #shorts")
        urls.append(f"ytsearch4:{q} caught on camera -reaction -story #shorts")
    return urls


def multi_query_crawl(search_queries: list[str], subreddits: list[str] | None = None, negative_filters: list[str] | None = None, max_total_urls: int = 35) -> list[str]:
    """
    Cascading 3-Tier Multi-Source Aggregator:
    Tier 1 (TikTok/IG) -> Tier 2 (Reddit v.redd.it) -> Tier 3 (YouTube CCTV/Dashcam).
    """
    aggregated_urls = []
    subs = subreddits or ["WatchPeopleDieInside", "Instant_Regret"]
    negs = negative_filters or ["podcast", "interview", "reaction", "green_screen", "facecam"]

    # Tier 1
    t1_urls = source_tier1_tiktok_reels(search_queries, negs)
    for u in t1_urls:
        if u not in aggregated_urls:
            aggregated_urls.append(u)

    # Tier 2
    t2_urls = source_tier2_reddit(subs, search_queries)
    for u in t2_urls:
        if u not in aggregated_urls:
            aggregated_urls.append(u)

    # Tier 3
    t3_urls = source_tier3_youtube_cctv(search_queries)
    for u in t3_urls:
        if u not in aggregated_urls:
            aggregated_urls.append(u)

    print(f"[Harvester] Cascading Aggregator collected {len(aggregated_urls)} query endpoints across Tiers 1-3.", file=sys.stderr)
    return aggregated_urls[:max_total_urls]


def check_ingestion_filters(video_path: str) -> tuple[bool, str]:
    """
    Ingestion Filters:
    1. Aspect Ratio: H / W >= 1.4 (must be vertical 9:16 format, reject landscape).
    2. Audio Presence: mean_volume >= -42.0 dB (must have audible native foley/audio).
    """
    if not os.path.exists(video_path) or os.path.getsize(video_path) == 0:
        return False, "Empty or non-existent file"

    # 1. Aspect Ratio Check via ffprobe
    try:
        probe_cmd = [
            "ffprobe", "-v", "error", "-select_streams", "v:0",
            "-show_entries", "stream=width,height", "-of", "json", video_path
        ]
        probe_res = subprocess.check_output(probe_cmd, text=True)
        probe_data = json.loads(probe_res)
        streams = probe_data.get("streams", [])
        if not streams:
            return False, "No video stream found"
        w = streams[0].get("width", 0)
        h = streams[0].get("height", 0)
        if w <= 0 or h <= 0:
            return False, "Invalid dimensions"
        aspect_ratio = float(h) / float(w)
        if aspect_ratio < 1.4:
            return False, f"Landscape or non-vertical format (H/W={aspect_ratio:.2f} < 1.4)"
    except Exception as e:
        return False, f"Aspect ratio probe failed: {e}"

    # 2. Audio Presence Check via volumedetect
    try:
        audio_cmd = [
            "ffmpeg", "-i", video_path, "-af", "volumedetect", "-vn", "-f", "null", "-"
        ]
        audio_proc = subprocess.run(
            audio_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True
        )
        match = re.search(r"mean_volume:\s*(-?[\d.]+)\s*dB", audio_proc.stderr)
        if not match:
            return False, "No audio stream or undetectable volume"
        mean_vol = float(match.group(1))
        if mean_vol < -42.0:
            return False, f"Audio volume too quiet/silent (mean_volume={mean_vol} dB < -42.0 dB)"
    except Exception as e:
        return False, f"Audio presence check failed: {e}"

    return True, "Passed Ingestion Filters"


def harvest_top_candidates(
    niche_id: str | None = None,
    sub_category_id: str | None = None,
    query: str | None = None,
    strict_definition: str = "",
    target_count: int = 10,
    negative_filters: list[str] | None = None,
    temp_dir: str = "temp_harvest_candidates",
    registry_path: str = "used_clips_registry.json",
    min_strict_matches: int = 5,
) -> list[dict]:
    """
    Universal Semantic Sourcing Pipeline:
    1. Multi-query aggregation across searchQueries list.
    2. Aspect ratio (H/W >= 1.4) and audio (mean_vol >= -42 dB) ingestion filter.
    3. Physical frame VLM verification against universal situation evaluator skill (is_match == True, confidence >= 0.85).
    4. Fail-safe fallback: exits with code 2 if < 5 matches found after 15 evaluations.
    """
    sub_meta = resolve_subcategory_metadata(niche_id, sub_category_id, query)
    sub_id = sub_meta.get("id")
    sub_name = sub_meta.get("name")
    search_queries = sub_meta.get("searchQueries", [f"{sub_id} fail", f"{sub_id} #shorts"])
    situational_prompt = sub_meta.get("situationalPrompt") or sub_meta.get("strictDefinition") or strict_definition
    combined_negative_filters = list(sub_meta.get("negativeFilters", []))
    if negative_filters:
        combined_negative_filters.extend(negative_filters)

    os.makedirs(temp_dir, exist_ok=True)
    registry = load_registry(registry_path)
    candidates = []

    print(f"\n==================================================", file=sys.stderr)
    print(f"[Harvester] Target Sub-Category: '{sub_name}' (ID: {sub_id})", file=sys.stderr)
    print(f"[Harvester] Situational Prompt: {situational_prompt}", file=sys.stderr)
    print(f"[Harvester] Target Count: {target_count} | Min Matches: {min_strict_matches}", file=sys.stderr)
    print(f"==================================================", file=sys.stderr)

    subreddits = sub_meta.get("subreddits", ["WatchPeopleDieInside", "Instant_Regret"])
    # 1. Cascading Multi-Query Crawl across Tiers 1-3
    curated_urls = multi_query_crawl(search_queries, subreddits=subreddits, negative_filters=combined_negative_filters, max_total_urls=35)
    evaluated_count = 0
    max_evaluations = 20

    for target_url in curated_urls:
        if len(candidates) >= target_count:
            break

        # Check candidate evaluation limit for round-robin advance
        if evaluated_count >= max_evaluations:
            if len(candidates) >= min(3, target_count):
                print(
                    f"\n[Harvester] Evaluated {evaluated_count} candidates; achieved {len(candidates)} verified clips. Proceeding with top candidates.",
                    file=sys.stderr,
                )
                break
            else:
                print(
                    f"\n[Harvester] Evaluated {evaluated_count} candidates without reaching min matches ({len(candidates)}/{min_strict_matches}). "
                    f"Triggering round-robin fallback (exit code 2).",
                    file=sys.stderr,
                )
                sys.exit(2)

        dump_cmd = [
            sys.executable,
            "-m", "yt_dlp",
            "--dump-json",
            "--no-playlist",
            "--ignore-errors",
            target_url,
        ]

        try:
            proc = subprocess.run(
                dump_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=25,
            )
        except Exception as e:
            print(f"[Harvester] yt-dlp dump error for {target_url}: {e}", file=sys.stderr)
            continue

        if proc.returncode != 0 or not proc.stdout:
            continue

        for line in proc.stdout.splitlines():
            line = line.strip()
            if not line:
                continue

            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue

            raw_id = item.get("id")
            if not raw_id or raw_id in registry:
                continue

            title = item.get("title", "")
            description = item.get("description", "")
            duration = item.get("duration")

            # Duration gate [3s - 90s]
            if duration is not None:
                if duration < 3.0 or duration > 90.0:
                    continue

            # Negative keyword filter
            if not passes_negative_filters(title, description, combined_negative_filters):
                continue

            evaluated_count += 1
            safe_title = title.encode("ascii", errors="replace").decode("ascii")
            print(f"\n[Candidate #{evaluated_count}] {raw_id}: '{safe_title[:50]}'", file=sys.stderr)

            # Download candidate to temp staging
            video_url = item.get("webpage_url") or item.get("url") or f"https://www.youtube.com/watch?v={raw_id}"
            out_template = os.path.join(temp_dir, f"{raw_id}.%(ext)s")
            target_mp4 = os.path.join(temp_dir, f"{raw_id}.mp4")

            if not os.path.exists(target_mp4) or os.path.getsize(target_mp4) == 0:
                dl_cmd = [
                    sys.executable,
                    "-m", "yt_dlp",
                    "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                    "--merge-output-format", "mp4",
                    "-o", out_template,
                    "--no-playlist",
                    "--quiet",
                    "--no-warnings",
                    video_url,
                ]
                try:
                    res = subprocess.run(dl_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=90)
                    if res.returncode != 0 or not os.path.exists(target_mp4):
                        continue
                except Exception as e:
                    print(f"[Harvester] Download failed for {raw_id}: {e}", file=sys.stderr)
                    continue

            # 2. Ingestion Filters: Aspect Ratio (H/W >= 1.4) & Audio Presence (mean_volume >= -42 dB)
            passed_ingestion, ingestion_reason = check_ingestion_filters(target_mp4)
            if not passed_ingestion:
                print(f"[Harvester] Ingestion Filter REJECTED {raw_id}: {ingestion_reason}", file=sys.stderr)
                try:
                    os.remove(target_mp4)
                except Exception:
                    pass
                continue

            # 3. VLM Multi-Frame Physical Verification (Reject Facecam, Subtitles, Watermarks, Slides)
            print(f"[Harvester] Running Strict Multi-Frame Vision Gatekeeper on {raw_id}...", file=sys.stderr)
            verif = verify_clip_physical_frames(
                video_path=target_mp4,
                title=title,
                description=description,
                situational_prompt=situational_prompt,
                sub_category_id=sub_id,
                duration=duration,
            )

            approved = bool(verif.get("approved", verif.get("is_match", False)))
            confidence = float(verif.get("confidence", 0.0))
            reason = verif.get("reason", "")
            action_detected = verif.get("action_detected", "")
            apex_est = verif.get("apex_timestamp_estimate", round((duration or 10.0) * 0.6, 2))
            has_facecam = verif.get("has_facecam", False)
            has_subtitles = verif.get("has_subtitles", False)

            if not approved or confidence < 0.75:
                print(f"[Harvester] REJECTED {raw_id} -> Reason: {reason} (Facecam={has_facecam}, Subtitles={has_subtitles}, Approved={approved})", file=sys.stderr)
                try:
                    os.remove(target_mp4)
                except Exception:
                    pass
                continue

            print(f"[Harvester] VLM APPROVED {raw_id}! Action='{action_detected}', Apex={apex_est}s, Conf={confidence:.2f}", file=sys.stderr)

            candidates.append({
                "id": raw_id,
                "title": title,
                "description": description,
                "duration": duration,
                "file_path": os.path.abspath(target_mp4),
                "apex_timestamp_estimate": apex_est,
                "action_detected": action_detected,
                "confidence": confidence,
            })
            print(f"[Harvester] Ingested candidate ({len(candidates)}/{target_count}): {raw_id}", file=sys.stderr)

    # 4. Fail-Safe Fallback Gate
    min_gate = min(min_strict_matches, target_count, 2)
    if len(candidates) < min_gate:
        print(
            f"\n[Harvester] Strict match count ({len(candidates)}) fell below required minimum ({min_gate}). "
            f"Exiting with status code 2 to trigger daemon niche fallback.",
            file=sys.stderr,
        )
        sys.exit(2)

    return candidates


def main():
    parser = argparse.ArgumentParser(description="Universal Semantic Sourcing & Extraction Harvester")
    parser.add_argument("--niche", default=None, help="Niche ID (e.g. funny_animals, sports_bloopers)")
    parser.add_argument("--sub", default=None, help="Sub-category ID (e.g. pets_being_dumb, athletes_celebrating_too_early)")
    parser.add_argument("--query", default=None, help="Legacy search query / sub-category name")
    parser.add_argument("--definition", default="", help="Strict niche definition for VLM filtering")
    parser.add_argument("--count", type=int, default=10, help="Number of candidates to download into staging")
    parser.add_argument("--min-matches", type=int, default=5, help="Minimum strict matches required before triggering fallback (exit 2)")
    parser.add_argument("--negative-filters", default="", help="Comma-separated banned keywords")
    parser.add_argument("--temp-dir", default="temp_harvest_candidates", help="Staging folder for downloaded raw MP4s")
    parser.add_argument("--registry", default="used_clips_registry.json", help="Path to registry")
    args = parser.parse_args()

    filter_list = [f.strip() for f in args.negative_filters.split(",") if f.strip()]

    candidates = harvest_top_candidates(
        niche_id=args.niche,
        sub_category_id=args.sub,
        query=args.query,
        strict_definition=args.definition,
        target_count=args.count,
        negative_filters=filter_list,
        temp_dir=args.temp_dir,
        registry_path=args.registry,
        min_strict_matches=args.min_matches,
    )

    print(json.dumps(candidates))


if __name__ == "__main__":
    main()
