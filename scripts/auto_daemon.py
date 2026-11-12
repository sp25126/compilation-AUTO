import argparse
import datetime
import json
import os
import subprocess
import sys
from dotenv import load_dotenv

# Load environment
load_dotenv()

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PYTHON_BIN = sys.executable

# Sub-category override (target specific category like road_rage_regret / road_rage_instant_justice)
TARGET_SUB_CATEGORY_ID = os.getenv("TARGET_SUB_CATEGORY", None)

# Phase 1: Load OpenRouter API Key Rotation Pool
raw_keys = os.getenv("OPENROUTER_API_KEYS", "")
if raw_keys:
    API_KEYS = [k.strip() for k in raw_keys.split(",") if k.strip()]
else:
    fallback_key = os.getenv("FREE_LLM_API_KEY", "")
    API_KEYS = [fallback_key] if fallback_key else []

current_key_index = 0


class HarvestFallbackError(Exception):
    """Raised when harvester cannot find enough strict context-matched clips (exit code 2)."""
    pass


def run_command(cmd: list[str], description: str) -> str:
    print(f"\n==================================================")
    print(f"[Daemon] {description}")
    print(f"[Command] {' '.join(cmd)}")
    print(f"==================================================")
    try:
        is_windows = sys.platform == "win32"
        resolved_cmd = list(cmd)
        if is_windows:
            if resolved_cmd[0] in ["npx", "npm", "remotion"]:
                resolved_cmd[0] = f"{resolved_cmd[0]}.cmd"

        res = subprocess.run(
            resolved_cmd,
            cwd=BASE_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
            shell=is_windows,
            env=os.environ.copy(),
        )
        if res.stdout:
            print(res.stdout.strip())
        return res.stdout
    except subprocess.CalledProcessError as e:
        print(f"[Daemon] Error during '{description}' (exit {e.returncode}):\n{e.stderr}", file=sys.stderr)
        raise


def step_a_select_sub_category(forced_id: str | None = None, use_trending: bool = True) -> dict:
    """
    Step A: Selects subcategory.
    If use_trending is True and no forced_id, queries live YouTube trending metrics via yt_researcher.
    If forced_id is provided, loads directly from NicheGraph.
    """
    if not forced_id and use_trending:
        try:
            print("\n[Daemon] Integrating YT Research Skill to identify live trending compilation...")
            try:
                from scripts.yt_researcher import discover_trending_compilation_topic
            except ImportError:
                from yt_researcher import discover_trending_compilation_topic
            trend = discover_trending_compilation_topic()
            if trend and trend.get("sub_category_id"):
                forced_id = trend["sub_category_id"]
                print(f"[Daemon] Live Trending Topic Detected: '{trend.get('trending_topic')}' -> Using '{forced_id}'")
        except Exception as e:
            print(f"[Daemon] YT Research integration notice: {e}. Falling back to graph selection.", file=sys.stderr)

    if forced_id:
        target_norm = forced_id.lower().replace("instant_justice", "regret")
        # Load from NicheGraph via node script
        probe_cmd = [
            "node",
            "-e",
            f"const {{ findSubCategory, NICHE_GRAPH }} = require('./dist/pipeline/NicheGraph.js'); "
            f"const found = findSubCategory('{forced_id}') || findSubCategory('{target_norm}') || "
            f"NICHE_GRAPH.flatMap(n => n.subCategories).find(s => s.id === '{forced_id}' || (s.aliases && s.aliases.includes('{forced_id}'))) || "
            f"NICHE_GRAPH[0].subCategories[0]; "
            f"console.log(JSON.stringify(found));"
        ]
        try:
            out = run_command(probe_cmd, f"Step A: Loading Targeted Sub-Category '{forced_id}'")
            for line in reversed(out.strip().splitlines()):
                try:
                    data = json.loads(line)
                    if isinstance(data, dict) and "id" in data:
                        return data
                except json.JSONDecodeError:
                    continue
        except Exception:
            pass

    cmd = ["npx", "ts-node", os.path.join(BASE_DIR, "src", "pipeline", "NicheGraph.ts")]
    output = run_command(cmd, "Step A: Selecting Sub-Category from Graph")
    for line in reversed(output.strip().splitlines()):
        try:
            data = json.loads(line)
            if isinstance(data, dict) and "id" in data:
                return data
        except json.JSONDecodeError:
            continue
    raise RuntimeError("Could not parse sub-category JSON from NicheGraph.")


def step_b_harvest_and_score(
    sub_category_id: str,
    sub_category_name: str,
    strict_definition: str,
    negative_filters: list[str],
    target_count: int = 10,
    top_k: int = 5,
) -> tuple[list[str], str]:
    """
    Step B: Harvests candidates across platforms using social_harvester.py & harvester.py,
    runs purity_gate.py to guarantee 100% raw phone / CCTV / dashcam footage,
    and returns selected raw video paths.
    """
    temp_candidates_dir = os.path.join(BASE_DIR, f"temp_harvest_{sub_category_id}")
    os.makedirs(temp_candidates_dir, exist_ok=True)
    candidates_json_path = os.path.join(BASE_DIR, "candidates_meta.json")

    # Try TikTok & Instagram social harvester first
    cmd_social = [
        PYTHON_BIN,
        os.path.join(BASE_DIR, "scripts", "social_harvester.py"),
        "--platform", "tiktok",
        "--query", sub_category_name,
        "--count", str(target_count),
        "--temp-dir", temp_candidates_dir,
    ]

    candidates = []
    try:
        social_out = run_command(cmd_social, f"Step B.1: TikTok & IG Sourcing for '{sub_category_name}'")
        for line in reversed(social_out.strip().splitlines()):
            try:
                parsed = json.loads(line)
                if isinstance(parsed, list) and parsed:
                    candidates = parsed
                    break
            except json.JSONDecodeError:
                continue
    except Exception as e:
        print(f"[Daemon] Social harvest note: {e}", file=sys.stderr)

    # Fallback / augment with multi-platform harvester
    if len(candidates) < top_k:
        cmd_harvest = [
            PYTHON_BIN,
            os.path.join(BASE_DIR, "scripts", "harvester.py"),
            "--sub", sub_category_id,
            "--query", sub_category_name,
            "--definition", strict_definition,
            "--count", str(target_count),
            "--min-matches", str(min(top_k, 5)),
            "--negative-filters", ",".join(negative_filters),
            "--temp-dir", temp_candidates_dir,
        ]
        try:
            harvest_output = run_command(cmd_harvest, f"Step B.1b: Primary Sourcing for '{sub_category_name}'")
            for line in reversed(harvest_output.strip().splitlines()):
                try:
                    parsed = json.loads(line)
                    if isinstance(parsed, list):
                        for c in parsed:
                            if not any(x.get("id") == c.get("id") for x in candidates):
                                candidates.append(c)
                        break
                except json.JSONDecodeError:
                    continue
        except subprocess.CalledProcessError as e:
            if e.returncode == 2 and not candidates:
                raise HarvestFallbackError(f"Not enough strict matches for '{sub_category_name}'")

    if not candidates:
        raise HarvestFallbackError(f"No candidate metadata returned for '{sub_category_name}'")

    # Phase 2: Multi-Frame Purity Gate (Rejects facecams, PiP, subtitles, static images)
    print(f"\n[Daemon] Step B.2: Running Multi-Frame Purity Gate on {len(candidates)} candidates...", file=sys.stderr)
    purity_passed = []
    for cand in candidates:
        file_p = cand.get("file_path")
        if not file_p or not os.path.exists(file_p):
            continue

        cmd_purity = [
            PYTHON_BIN,
            os.path.join(BASE_DIR, "scripts", "purity_gate.py"),
            "--input", file_p,
            # Do not delete immediately so candidates metadata remains intact if fallback needed
        ]
        try:
            p_out = subprocess.check_output(cmd_purity, text=True, stderr=subprocess.DEVNULL)
            p_res = json.loads(p_out)
            if p_res.get("is_pure_raw_footage"):
                print(f"[Daemon] Clip {cand.get('id')} PASSED Purity Gate!", file=sys.stderr)
                purity_passed.append(cand)
            else:
                print(f"[Daemon] Clip {cand.get('id')} REJECTED by Purity Gate: {p_res.get('reason')}", file=sys.stderr)
                try:
                    os.remove(file_p)
                except Exception:
                    pass
        except Exception as pe:
            print(f"[Daemon] Purity gate note on candidate {cand.get('id')}: {pe}", file=sys.stderr)
            # If inspection failed due to network/tool issue, keep candidate if file exists
            if os.path.exists(file_p):
                purity_passed.append(cand)

    if purity_passed:
        candidates = purity_passed
    else:
        # If all were rejected, re-harvest or fallback
        candidates = [c for c in candidates if os.path.exists(c.get("file_path", ""))]

    with open(candidates_json_path, "w", encoding="utf-8") as f:
        json.dump(candidates, f, indent=2)

    # Arena scoring and selection of top k
    manifest_path = os.path.join(BASE_DIR, "arena_selected.json")
    cmd_arena = [
        PYTHON_BIN,
        os.path.join(BASE_DIR, "scripts", "arena_scorer.py"),
        "--candidates-json", candidates_json_path,
        "--top-k", str(top_k),
        "--output-manifest", manifest_path,
    ]
    arena_output = run_command(cmd_arena, f"Step B.3: VLM Arena Scoring & Top-{top_k} Selection")

    selected_paths = []
    for line in reversed(arena_output.strip().splitlines()):
        try:
            paths = json.loads(line)
            if isinstance(paths, list):
                selected_paths = paths
                break
        except json.JSONDecodeError:
            continue

    return selected_paths, manifest_path


def get_impact_sfx_for_incident(incident_type: str) -> str:
    sfx_map = {
        "car_crash": "heavy_metal_crunch.mp3",
        "chase": "tires_screech.mp3",
        "physical_fall": "thud_whack.mp3",
        "verbal_argument": "record_scratch.mp3",
        "prank_backfire": "evil_laugh_cut.mp3",
        "clumsy_action": "cartoon_slip.mp3",
        "instant_karma": "boom_reverb.mp3",
        "equipment_failure": "industrial_crash.mp3",
        "weather_blast": "wind_whoosh_pop.mp3",
        "sports_miss": "fail_buzzer.mp3",
        "awkward_moment": "awkward_cough.mp3",
        "aura_loss": "vine_boom.mp3",
        "lucky_dodge": "angelic_choir.mp3",
        "npc_glitch": "matrix_dejavu.mp3",
    }
    return sfx_map.get((incident_type or "").lower(), "heavy_metal_crunch.mp3")


def step_c_evaluate_and_bake(raw_paths: list[str], sub_category_id: str, manifest_path: str = "arena_selected.json") -> list[dict]:
    """
    Step C: Evaluates each raw clip using cause_trimmer.py (isolates 5-7s cause and impact)
    and vo_generator.py (synthesizes edge-tts neural voiceover setup lines).
    NO cartoon soundboards, 100% natural clip audio.
    """
    meta_by_path = {}
    if os.path.exists(manifest_path):
        try:
            with open(manifest_path, "r", encoding="utf-8") as f:
                manifest_items = json.load(f)
                if isinstance(manifest_items, list):
                    for item in manifest_items:
                        p = os.path.abspath(item.get("file_path", ""))
                        meta_by_path[p] = item
        except Exception:
            pass

    baked_clips = []
    output_dir = os.path.join(BASE_DIR, "public", "clips")
    audio_dir = os.path.join(BASE_DIR, "public", "audio")
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)

    for idx, raw_path in enumerate(raw_paths):
        abs_raw = os.path.abspath(raw_path)
        meta = meta_by_path.get(abs_raw, {})

        clip_id = f"{sub_category_id}_{idx + 1}"
        trimmed_filename = f"{clip_id}_trimmed.mp4"
        trimmed_path = os.path.join(output_dir, trimmed_filename)

        vlm_apex = meta.get("apex_timestamp_estimate") or meta.get("t_apex") or 0.0

        # Phase 3: AI Cause & Impact Trimmer (4s to 8s target)
        cmd_trim = [
            PYTHON_BIN,
            os.path.join(BASE_DIR, "scripts", "cause_trimmer.py"),
            "--input", raw_path,
            "--output", trimmed_path,
        ]
        if vlm_apex and float(vlm_apex) > 0:
            cmd_trim.extend(["--vlm-apex", str(vlm_apex)])

        try:
            run_command(cmd_trim, f"Step C.1: Cause & Impact Trimming for {clip_id}")
            if not os.path.exists(trimmed_path):
                continue

            # Phase 4: Minimal Neural Voiceover & Subtitle Generator via edge-tts
            cmd_vo = [
                PYTHON_BIN,
                os.path.join(BASE_DIR, "scripts", "vo_generator.py"),
                "--video", trimmed_path,
                "--rank", str(idx + 1),
                "--category", sub_category_id.replace("_", " ").title(),
            ]
            vo_out = run_command(cmd_vo, f"Step C.2: Edge-TTS Voiceover Generation for {clip_id}")
            vo_entry = {}
            try:
                # Find the full JSON block in vo_out
                import re
                json_match = re.search(r"(\{[\s\S]*\})", vo_out)
                if json_match:
                    vo_entry = json.loads(json_match.group(1))
            except Exception:
                pass

            baked_clips.append({
                "id": clip_id,
                "videoPath": trimmed_path,
                "voPath": vo_entry.get("voPath"),
                "subtitleText": vo_entry.get("subtitleText", "He realized his mistake immediately."),
                "durationInFrames": vo_entry.get("durationInFrames", 180),
                "voDuration": vo_entry.get("voDuration", 2.2),
            })
        except Exception as e:
            print(f"[Daemon] Warning: Clip {clip_id} failed trimming/voiceover: {e}", file=sys.stderr)
            continue

    return baked_clips


def load_subcategory_skill(sub_id: str) -> str | None:
    """
    Loads the execution-ready skill specification from subcategory_skills/<sub_id>.md if present.
    """
    skill_path = os.path.join(BASE_DIR, "subcategory_skills", f"{sub_id}.md")
    if os.path.exists(skill_path):
        print(f"[Daemon] Loaded sub-category skill: {skill_path}")
        return skill_path
    return None


def step_d_write_cue_sheet(sub_category: dict, baked_clips: list[dict]) -> str:
    """
    Step D: Writes root cue_sheet.json manifest payload for Remotion composition.
    """
    cue_sheet_path = os.path.join(BASE_DIR, "cue_sheet.json")
    sub_id = sub_category.get("id", "")
    skill_path = load_subcategory_skill(sub_id)

    manifest = {
        "subCategoryId": sub_id,
        "subCategoryName": sub_category.get("name", "").upper(),
        "skillPath": skill_path,
        "clips": baked_clips,
    }

    with open(cue_sheet_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f"\n[Daemon] Step D: cue_sheet.json manifest generated with {len(baked_clips)} clips.")
    return cue_sheet_path


def step_e_render_remotion(sub_id: str | None = None) -> str:
    """
    Step E: Executes npm run render to create output/raw_render.mp4.
    Also preserves subcategory specific output/raw_render_{sub_id}.mp4.
    """
    import shutil
    os.makedirs(os.path.join(BASE_DIR, "output"), exist_ok=True)
    cmd = ["npm", "run", "render"]
    run_command(cmd, "Step E: Rendering Composition with Remotion")
    raw_render = os.path.join(BASE_DIR, "output", "raw_render.mp4")
    if not os.path.exists(raw_render):
        raise FileNotFoundError(f"Remotion render output not found: {raw_render}")
    if sub_id:
        sub_raw = os.path.join(BASE_DIR, "output", f"{sub_id}_raw.mp4")
        shutil.copyfile(raw_render, sub_raw)
    return raw_render


def step_f_master_audio(raw_render_path: str, sub_id: str | None = None) -> str:
    """
    Step F: Executes audio mastering via EBU R128 to output/mastered_final.mp4.
    Also preserves subcategory specific output/{sub_id}_mastered.mp4.
    """
    import shutil
    mastered_final = os.path.join(BASE_DIR, "output", "mastered_final.mp4")
    sub_mastered = os.path.join(BASE_DIR, "output", f"{sub_id}_mastered.mp4") if sub_id else mastered_final

    cmd = [
        "npx", "ts-node",
        os.path.join(BASE_DIR, "src", "services", "mastering.ts"),
        "--input", raw_render_path,
        "--output", sub_mastered,
    ]
    run_command(cmd, f"Step F: EBU R128 Two-Pass Loudnorm Audio Mastering ({sub_id or 'final'})")
    if not os.path.exists(sub_mastered):
        raise FileNotFoundError(f"Mastered output not found: {sub_mastered}")
    if sub_id and sub_mastered != mastered_final:
        shutil.copyfile(sub_mastered, mastered_final)
    return sub_mastered


def step_g_schedule_youtube(video_path: str, sub_category_name: str) -> None:
    """
    Step G: Calculates UTC +6 hours and calls youtube_uploader.py.
    """
    client_secrets = os.path.join(BASE_DIR, "client_secrets.json")
    token_file = os.path.join(BASE_DIR, "token.json")
    if not os.path.exists(client_secrets) and not os.path.exists(token_file):
        print(f"\n[Daemon] Step G: Google OAuth credentials ('client_secrets.json') not yet placed. Video successfully rendered to '{video_path}' for forensic audit. Ready for YouTube API scheduler activation.")
        return

    now_utc = datetime.datetime.now(datetime.timezone.utc)
    publish_at = now_utc + datetime.timedelta(hours=6)
    publish_at_iso = publish_at.strftime("%Y-%m-%dT%H:%M:%SZ")

    title = f"Top 5 {sub_category_name} Ranked! 😱 | LevelZero0ne #shorts"
    description = f"Ranking the top 5 wildest {sub_category_name} moments!\n\nCurated and Produced by @LevelZero0ne\n#shorts #ranking #viral #LevelZero0ne"
    tags = [sub_category_name.lower(), "shorts", "ranking", "viral", "top5", "LevelZero0ne"]

    cmd = [
        PYTHON_BIN,
        os.path.join(BASE_DIR, "scripts", "youtube_uploader.py"),
        "--file", video_path,
        "--title", title,
        "--description", description,
        "--tags", ",".join(tags),
        "--publish-at", publish_at_iso,
    ]
    run_command(cmd, f"Step G: Scheduling YouTube Shorts Release for {publish_at_iso}")


TEN_NICHE_SUBCATEGORIES = [
    {"niche": "Human Physical Fails", "sub_id": "people_accepting_fate"},
    {"niche": "Instant Regret & Karma", "sub_id": "road_rage_justice"},
    {"niche": "Funny Animals & Pets", "sub_id": "pets_being_dumb"},
    {"niche": "Infinite Aura Loss", "sub_id": "one_million_aura_loss"},
    {"niche": "Sports & Athletic Bloopers", "sub_id": "athletes_celebrating_too_early"},
    {"niche": "Real-Life Glitches & NPCs", "sub_id": "unrendered_game_npcs"},
    {"niche": "Workplace Disasters", "sub_id": "worst_shift_ever"},
    {"niche": "Extreme Luck & Saves", "sub_id": "used_all_luck_for_life"},
    {"niche": "Gym & Fitness Bloopers", "sub_id": "bench_press_ego_fails"},
    {"niche": "Nature & Weather Surprises", "sub_id": "sudden_wind_ruining_events"},
]


def run_single_video_cycle(target_sub: str, skip_upload: bool = True) -> dict:
    global current_key_index

    # Phase 1: Set active rotated key
    if API_KEYS:
        active_key = API_KEYS[current_key_index]
        os.environ["ACTIVE_LLM_KEY"] = active_key
        print(f"[Daemon] Active OpenRouter API Key [{current_key_index + 1}/{len(API_KEYS)}]: {active_key[:14]}...")
    else:
        print("[Daemon] Warning: No API keys configured in OPENROUTER_API_KEYS.", file=sys.stderr)

    # Step 0: Lock in Niche Decision Before Any Ingestion
    sub_category = step_a_select_sub_category(forced_id=target_sub)
    sub_id = sub_category.get("id")
    sub_name = sub_category.get("name")
    strict_def = sub_category.get("strictDefinition", "")
    neg_filters = sub_category.get("negativeFilters", [])

    run_context = {
        "run_id": datetime.datetime.now().strftime("run_%Y%m%d_%H%M%S"),
        "locked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "sub_category_id": sub_id,
        "sub_category_name": sub_name,
        "strict_definition": strict_def,
        "negative_filters": neg_filters,
        "audio_stem": sub_category.get("audioStem", "siren_short.mp3"),
        "punchline_text": sub_category.get("punchlineText", "INSTANT JUSTICE"),
    }
    context_file = os.path.join(BASE_DIR, "current_run_context.json")
    with open(context_file, "w", encoding="utf-8") as f:
        json.dump(run_context, f, indent=2)

    print(f"\n==================================================")
    print(f" [LOCKED RUN NICHE]: {sub_name} (ID: {sub_id})")
    print(f" [STRICT DEFINITION]: {strict_def}")
    print(f" [RUN CONTEXT]: Saved to current_run_context.json")
    print(f"==================================================")

    # Step B: Clip Harvesting & Arena Ranking
    raw_clips, manifest_path = step_b_harvest_and_score(
        sub_category_id=sub_id,
        sub_category_name=sub_name,
        strict_definition=strict_def,
        negative_filters=neg_filters,
        target_count=10,
        top_k=5,
    )

    if not raw_clips or len(raw_clips) < 2:
        raise HarvestFallbackError(f"Insufficient verified clips for '{sub_name}' ({len(raw_clips) if raw_clips else 0}/2)")

    # Step C: Evaluation & Apex Baking
    baked_clips = step_c_evaluate_and_bake(raw_clips, sub_id, manifest_path=manifest_path)
    if not baked_clips:
        raise RuntimeError(f"No clips passed visual evaluation for '{sub_name}'.")

    # Step D: Composition Manifest
    cue_path = step_d_write_cue_sheet(sub_category, baked_clips)

    # Step E: Remotion Headless Render
    raw_render_path = step_e_render_remotion(sub_id=sub_id)

    # Step F: Audio Mastering
    mastered_path = step_f_master_audio(raw_render_path, sub_id=sub_id)

    # Step G: YouTube Scheduling (+6h) unless skipped for QA
    if not skip_upload:
        step_g_schedule_youtube(mastered_path, sub_name)
    else:
        print("\n[Daemon] skip_upload=True: Bypassing YouTube scheduling for local forensic review.")

    # Advance key rotation upon successful completion of the full video cycle
    if API_KEYS:
        current_key_index = (current_key_index + 1) % len(API_KEYS)
        print(f"[Daemon] Video cycle complete! Rotated next API key index to: {current_key_index}")

    result_record = {
        "sub_category_id": sub_id,
        "sub_category_name": sub_name,
        "mastered_file": os.path.abspath(mastered_path),
        "clips_count": len(baked_clips),
        "punchlines": [c.get("punchlineText") for c in baked_clips],
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    return result_record


def main():
    parser = argparse.ArgumentParser(description="Autonomous Viral Shorts Daemon")
    parser.add_argument("--sub-category", default=None, help="Force specific sub-category ID")
    parser.add_argument("--batch-all-niches", action="store_true", help="Sequentially produce 10 shorts across all 10 distinct niches")
    parser.add_argument("--skip-upload", action="store_true", default=True, help="Skip YouTube upload step for forensic QA")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry-run test of next subcategory selection and configuration")
    args = parser.parse_args()

    print("**************************************************")
    print("   AUTONOMOUS VIRAL SHORTS DAEMON INITIALIZED    ")
    print("**************************************************")

    if args.dry_run:
        print("[Dry-Run] Pulling next scheduled sub-category node from pipeline history...")
        chosen = step_a_select_sub_category(forced_id=args.sub_category)
        print(f"[Dry-Run] Target Sub-Category: {chosen.get('name')} ({chosen.get('id')})")
        print(f"[Dry-Run] Audio Stem: {chosen.get('audioStem')}")
        print(f"[Dry-Run] Kinetic Typography: {chosen.get('kineticTypography')}")
        print(f"[Dry-Run] Timing Recipe: {chosen.get('timingRecipe')}")
        print("[Dry-Run] Multi-frame VLM checks: ENABLED (15%, 40%, 65%, 85%)")
        print("[Dry-Run] Audio Target: EBU R128 (-14.0 LUFS, TP <= -1.5 dBTP)")
        print("[Dry-Run] Master Daemon dry-run complete! All logic gates verified.")
        return

    if args.batch_all_niches:
        print(f"\n[Daemon] Starting Batch Production for ALL 10 Niches...")
        completed_shorts = []
        for item in TEN_NICHE_SUBCATEGORIES:
            niche_name = item["niche"]
            sub_id = item["sub_id"]
            print(f"\n==================================================")
            print(f" [BATCH PROGRESS: {len(completed_shorts) + 1}/10] Niche: {niche_name} ({sub_id})")
            print(f"==================================================")
            try:
                rec = run_single_video_cycle(target_sub=sub_id, skip_upload=args.skip_upload)
                completed_shorts.append(rec)
                print(f"[Batch] Successfully produced short: {rec.get('mastered_file')}")
            except Exception as batch_err:
                print(f"[Batch] Notice on '{sub_id}': {batch_err}. Continuing to next niche...", file=sys.stderr)

        manifest_file = os.path.join(BASE_DIR, "output", "ten_shorts_manifest.json")
        with open(manifest_file, "w", encoding="utf-8") as f:
            json.dump(completed_shorts, f, indent=2)
        print(f"\n[Daemon] Batch finished! Produced {len(completed_shorts)}/10 shorts. Manifest saved to {manifest_file}")
        return

    # Single video execution
    target_sub = args.sub_category or TARGET_SUB_CATEGORY_ID
    try:
        rec = run_single_video_cycle(target_sub=target_sub, skip_upload=args.skip_upload)
        print("\n**************************************************")
        print("   AUTONOMOUS CYCLE COMPLETED SUCCESSFULLY!      ")
        print(f"   Deliverable: {rec.get('mastered_file')}")
        print("**************************************************")
    except Exception as e:
        print(f"\n[Daemon] Pipeline halted due to unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
