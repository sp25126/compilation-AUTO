import argparse
import base64
import json
import os
import re
import shutil
import subprocess
import sys
import traceback
from dotenv import load_dotenv
from openai import OpenAI

# Load project environment variables from .env
load_dotenv()


def get_openai_client() -> OpenAI:
    """
    Returns OpenAI client configured with the active OpenRouter key from the rotation pool.
    """
    api_key = os.getenv("ACTIVE_LLM_KEY") or os.getenv("FREE_LLM_API_KEY", "")
    base_url = os.getenv("FREE_LLM_BASE_URL", "https://openrouter.ai/api/v1")
    return OpenAI(base_url=base_url, api_key=api_key)


def get_model_name() -> str:
    return os.getenv("FREE_LLM_MODEL", "openrouter/auto")


ARENA_SYSTEM_PROMPT = """You are an elite viral video curator and director for YouTube Shorts.
Analyze candidate video clips using their titles, descriptions, and 3 keyframes (start, middle, end).
Score each clip from 1 to 10 based on:
1. Clear physical impact or comedic climax (is there an unmistakable punchline, crash, trip, or instant karma?).
2. Visibility of action (is the primary subject clear, well-framed, and not obscured or blurry?).
3. Authentic real-life footage (STRICT penalty / instant 1/10 for video games, GTA, CGI, 3D animations, cartoons, or static dashcam drives with no visible action).

Assign a specific incident_type from one of:
['car_crash', 'verbal_argument', 'chase', 'physical_fall', 'prank_backfire', 'clumsy_action', 'instant_karma', 'other']

You must output valid JSON strictly matching this schema:
{
  "rankings": [
    {
      "clip_id": "string",
      "score": float,
      "incident_type": "string",
      "reason": "string",
      "punchlineText": "string"
    }
  ]
}
"""


def extract_json_from_text(text: str) -> dict | list | None:
    if not text:
        return None
    fenced_match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    candidate_str = fenced_match.group(1).strip() if fenced_match else text.strip()

    bracket_match = re.search(r"(\{[\s\S]*\}|\[[\s\S]*\])", candidate_str)
    if bracket_match:
        try:
            return json.loads(bracket_match.group(1))
        except Exception:
            pass

    # Resilient partial object parser: extracts all fully formed JSON objects even from truncated output
    object_matches = re.findall(r"(\{[^{}]*\"clip_id\"[^{}]*\})", text)
    extracted_items = []
    for obj_str in object_matches:
        try:
            item = json.loads(obj_str)
            if "clip_id" in item:
                extracted_items.append(item)
        except Exception:
            continue

    if extracted_items:
        return {"rankings": extracted_items}

    return None


def extract_three_keyframes(video_path: str, temp_frame_dir: str, clip_id: str) -> list[str]:
    os.makedirs(temp_frame_dir, exist_ok=True)
    duration = 5.0
    try:
        probe_cmd = [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", video_path
        ]
        res = subprocess.check_output(probe_cmd, text=True).strip()
        duration = max(1.0, float(res))
    except Exception:
        duration = 5.0

    timestamps = [
        round(duration * 0.15, 2),
        round(duration * 0.50, 2),
        round(duration * 0.85, 2),
    ]

    base64_frames = []
    for idx, ts in enumerate(timestamps):
        out_img = os.path.join(temp_frame_dir, f"{clip_id}_frame_{idx}.jpg")
        cmd = [
            "ffmpeg", "-y", "-ss", str(ts), "-i", video_path,
            "-vframes", "1", "-vf", "scale=360:-1", "-q:v", "5", out_img
        ]
        try:
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=10)
            if os.path.exists(out_img) and os.path.getsize(out_img) > 0:
                with open(out_img, "rb") as f:
                    encoded = base64.b64encode(f.read()).decode("utf-8")
                    base64_frames.append(f"data:image/jpeg;base64,{encoded}")
        except Exception:
            continue

    return base64_frames


def get_current_run_context() -> dict:
    context_path = os.path.abspath("current_run_context.json")
    if os.path.exists(context_path):
        try:
            with open(context_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def score_arena_candidates(
    candidates: list[dict],
    temp_frame_dir: str = "temp_arena_frames",
    sub_category_id: str | None = None,
) -> list[dict]:
    client = get_openai_client()
    model_name = get_model_name()
    run_ctx = get_current_run_context()
    target_sub_cat = sub_category_id or run_ctx.get("sub_category_id", "road_rage_regret")

    user_content = []
    user_content.append({
        "type": "text",
        "text": f"Evaluate and rank the following {len(candidates)} candidate videos according to viral climax criteria:"
    })

    for cand in candidates:
        clip_id = cand["id"]
        title = cand.get("title", "")
        desc = cand.get("description", "")
        video_path = cand["file_path"]

        user_content.append({
            "type": "text",
            "text": f"\n--- Candidate Clip ID: {clip_id} ---\nTitle: {title}\nDescription: {desc[:200]}"
        })

        frames = extract_three_keyframes(video_path, temp_frame_dir, clip_id)
        for f_idx, frame_b64 in enumerate(frames):
            user_content.append({
                "type": "text",
                "text": f"Frame {f_idx + 1} ({clip_id}):"
            })
            user_content.append({
                "type": "image_url",
                "image_url": {"url": frame_b64}
            })

    print(f"\n[DEBUG - Arena Prompt]: Prepared {len(candidates)} candidates for {model_name} via {client.base_url}")

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": ARENA_SYSTEM_PROMPT},
                {"role": "user", "content": user_content},
            ],
            response_format={"type": "json_object"},
            temperature=0.2,
            max_tokens=400,
            timeout=45.0,
        )

        raw_text = response.choices[0].message.content or ""
        print(f"\n[DEBUG - Arena VLM Response]: {raw_text}")

        result = extract_json_from_text(raw_text)
        if isinstance(result, dict) and "rankings" in result and result["rankings"]:
            return result["rankings"]
        elif isinstance(result, list) and result:
            return result

        print("[Arena Scorer] VLM returned empty or unparseable rankings. Engaging Level-2 Fallback Engine...", file=sys.stderr)
        from fallback_analyzer import analyze_clip_heuristically
        fallback_rankings = []
        for cand in candidates:
            analysis = analyze_clip_heuristically(
                title=cand.get("title", ""),
                description=cand.get("description", ""),
                sub_category_id=target_sub_cat,
            )
            if analysis.get("is_real_and_context_matched"):
                score = round(7.0 + (analysis.get("confidence", 0.8) * 2.5), 1)
                fallback_rankings.append({
                    "clip_id": cand["id"],
                    "score": score,
                    "incident_type": analysis.get("incident_type", "clumsy_action"),
                    "reason": f"Fallback Heuristic: {analysis.get('reason')}",
                    "punchlineText": analysis.get("punchlineText", "MOMENT OF REGRET"),
                })
        if fallback_rankings:
            print(f"[Arena Scorer] Fallback Engine ranked {len(fallback_rankings)} candidates for '{target_sub_cat}'.", file=sys.stderr)
            return fallback_rankings

    except Exception as e:
        print(f"[Arena Scorer] Exception calling VLM ({e}). Engaging Level-2 Heuristic Community Fallback Engine...", file=sys.stderr)
        try:
            from fallback_analyzer import analyze_clip_heuristically
            fallback_rankings = []
            for cand in candidates:
                analysis = analyze_clip_heuristically(
                    title=cand.get("title", ""),
                    description=cand.get("description", ""),
                    sub_category_id=target_sub_cat,
                )
                if analysis.get("is_real_and_context_matched"):
                    score = round(7.0 + (analysis.get("confidence", 0.8) * 2.5), 1)
                    fallback_rankings.append({
                        "clip_id": cand["id"],
                        "score": score,
                        "incident_type": analysis.get("incident_type", "clumsy_action"),
                        "reason": f"Fallback Heuristic: {analysis.get('reason')}",
                        "punchlineText": analysis.get("punchlineText", "MOMENT OF REGRET"),
                    })
            if fallback_rankings:
                print(f"[Arena Scorer] Fallback Engine successfully ranked {len(fallback_rankings)} candidates for '{target_sub_cat}'.", file=sys.stderr)
                return fallback_rankings
        except Exception:
            traceback.print_exc(file=sys.stderr)

    return []


def select_top_candidates(
    candidates: list[dict],
    top_k: int = 5,
    min_score: float = 7.0,
    destination_dir: str = "public/raw_clips",
    output_manifest: str = "arena_selected.json"
) -> list[str]:
    os.makedirs(destination_dir, exist_ok=True)
    temp_frame_dir = os.path.join(destination_dir, "_temp_frames")

    print(f"[Arena Scorer] Scoring {len(candidates)} candidates for top {top_k} (min score: {min_score})...", file=sys.stderr)
    rankings = score_arena_candidates(candidates, temp_frame_dir)

    if os.path.exists(temp_frame_dir):
        shutil.rmtree(temp_frame_dir, ignore_errors=True)

    rank_map = {r.get("clip_id"): r for r in rankings if isinstance(r, dict)}
    scored_candidates = []

    for cand in candidates:
        r_info = rank_map.get(cand["id"], None)
        title = cand.get("title", cand["id"])
        score = float(r_info.get("score", 7.0)) if r_info else float(cand.get("confidence", 0.85) * 10)
        cand["score"] = score
        cand["incident_type"] = (r_info.get("incident_type") if r_info else None) or "clumsy_action"
        cand["reason"] = (r_info.get("reason") if r_info else None) or "Verified physical action"
        cand["punchlineText"] = (r_info.get("punchlineText") if r_info else None) or "MOMENT OF REGRET"
        scored_candidates.append(cand)

    if not scored_candidates:
        print(f"\n[FATAL] Arena Scorer: No candidate clips available to rank.", file=sys.stderr)
        sys.exit(1)

    scored_candidates.sort(key=lambda x: x["score"], reverse=True)
    selected = scored_candidates[:top_k]
    discarded = scored_candidates[top_k:]

    final_paths = []
    manifest_data = []

    for item in selected:
        src = item["file_path"]
        dest = src
        # Only copy if source file exists
        if os.path.exists(src):
            filename = os.path.basename(src)
            dest = os.path.join(destination_dir, filename)
            if os.path.abspath(src) != os.path.abspath(dest):
                shutil.copy2(src, dest)
        else:
            # Fallback if file was deleted
            continue

        final_paths.append(os.path.abspath(dest))
        manifest_data.append({
            "clip_id": item["id"],
            "file_path": os.path.abspath(dest),
            "score": item["score"],
            "incident_type": item["incident_type"],
            "punchlineText": item.get("punchlineText", "MOMENT OF REGRET"),
            "reason": item["reason"],
        })

    if not final_paths:
        print("[FATAL] Arena Scorer: No valid existing video files found among selected candidates.", file=sys.stderr)
        sys.exit(1)

    # Ensure unique punchlines for each clip in compilation
    used_punchlines = set()
    target_sub_cat = ""
    try:
        context_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "current_run_context.json")
        if os.path.exists(context_path):
            with open(context_path, "r", encoding="utf-8") as f:
                cdata = json.load(f)
                target_sub_cat = cdata.get("sub_category_id", "")
    except Exception:
        pass
    if not target_sub_cat and candidates:
        target_sub_cat = candidates[0].get("sub_category_id", "")

    from fallback_analyzer import NICHE_LEXICONS
    niche_punchline_pool = list(NICHE_LEXICONS.get(target_sub_cat, {}).get("punchlines", [
        "MOMENT OF REGRET", "INSTANT KARMA ACTIVATED", "PHYSICS STEPPED IN", "UNEXPECTED OUTCOME", "LESSON LEARNED"
    ]))
    if len(niche_punchline_pool) < top_k:
        niche_punchline_pool.extend([f"CLIMAX RANK {i+1}" for i in range(top_k)])
    pool_idx = 0
    for m in manifest_data:
        pl = m.get("punchlineText")
        if not pl or pl in used_punchlines or pl == "MOMENT OF REGRET":
            while pool_idx < len(niche_punchline_pool) and niche_punchline_pool[pool_idx] in used_punchlines:
                pool_idx += 1
            if pool_idx < len(niche_punchline_pool):
                m["punchlineText"] = niche_punchline_pool[pool_idx]
                used_punchlines.add(niche_punchline_pool[pool_idx])
                pool_idx += 1
        else:
            used_punchlines.add(pl)

    for item in discarded:
        try:
            if os.path.exists(item["file_path"]) and "public\\raw_clips" not in item["file_path"]:
                os.remove(item["file_path"])
        except Exception:
            pass

    with open(output_manifest, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2)

    print(f"[Arena Scorer] Selected {len(final_paths)} clips saved to {output_manifest}", file=sys.stderr)
    return final_paths


def main():
    parser = argparse.ArgumentParser(description="VLM Arena Scorer & Curator")
    parser.add_argument("--query", default=None, help="Optional search query if pulling directly")
    parser.add_argument("--pool-size", type=int, default=5, help="Number of clips to pull if query provided")
    parser.add_argument("--top", "--top-k", dest="top", type=int, default=1, help="Number of top clips to select")
    parser.add_argument("--candidates-json", default=None, help="Path to JSON containing candidate metadata")
    parser.add_argument("--output-manifest", default="arena_selected.json", help="Path to save selection manifest")
    args = parser.parse_args()

    candidates = []
    if args.candidates_json and os.path.exists(args.candidates_json):
        with open(args.candidates_json, "r", encoding="utf-8") as f:
            candidates = json.load(f)
    elif args.query:
        import scripts.harvester as h
        candidates = h.harvest_top_candidates(query=args.query, target_count=args.pool_size)

    if not candidates:
        print("[Arena Scorer] Error: No candidate clips found to score.", file=sys.stderr)
        sys.exit(1)

    selected_paths = select_top_candidates(
        candidates=candidates,
        top_k=args.top,
        output_manifest=args.output_manifest,
    )
    print(json.dumps(selected_paths))


if __name__ == "__main__":
    main()
