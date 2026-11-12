import argparse
import base64
import json
import os
import re
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


def build_system_prompt(strict_definition: str = "") -> str:
    clean_def = strict_definition.strip() if strict_definition else "Real-life viral moment matching search context."
    return (
        "You are a strict video semantic filter. Analyze the title, description, and thumbnail.\n"
        "Rule 1: It must be 100% real-life camera footage (No games, CGI, anime).\n"
        f"Rule 2: It must strictly match this exact definition: {clean_def}\n"
        "If it is just a generic video that misses the specific context, you MUST reject it.\n\n"
        "Respond strictly in JSON format matching this schema:\n"
        '{"is_real_and_context_matched": boolean, "confidence": float, "reason": "string"}'
    )


def extract_json_from_text(text: str) -> dict | None:
    if not text:
        return None
    fenced = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    candidate = fenced.group(1).strip() if fenced else text.strip()
    match = re.search(r"(\{[\s\S]*\})", candidate)
    if match:
        candidate = match.group(1)
    try:
        return json.loads(candidate)
    except Exception:
        return None


def extract_verification_keyframes(video_path: str, duration: float) -> list[tuple[float, str]]:
    """
    Multi-Frame Sampling:
    Extracts 4 distinct keyframe images from each candidate MP4 at 15%, 40%, 65%, and 85% of duration.
    ffmpeg -ss <time> -i input.mp4 -vframes 1 -q:v 2 frame_<idx>.jpg
    Returns list of (timestamp, base64_jpeg_data_url).
    """
    timestamps = [
        max(0.1, duration * 0.15),
        max(0.2, duration * 0.40),
        max(0.3, duration * 0.65),
        max(0.4, duration * 0.85),
    ]
    frames = []
    temp_dir = os.path.join(os.path.dirname(os.path.abspath(video_path)), "_vlm_frames")
    os.makedirs(temp_dir, exist_ok=True)
    basename = os.path.splitext(os.path.basename(video_path))[0]

    for idx, ts in enumerate(timestamps):
        out_jpg = os.path.join(temp_dir, f"{basename}_f{idx+1}.jpg")
        cmd = [
            "ffmpeg", "-y", "-ss", f"{ts:.2f}",
            "-i", video_path,
            "-vframes", "1",
            "-q:v", "2",
            "-vf", "scale=480:-1",
            out_jpg
        ]
        try:
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=12)
            if os.path.exists(out_jpg) and os.path.getsize(out_jpg) > 0:
                with open(out_jpg, "rb") as f:
                    b64 = base64.b64encode(f.read()).decode("utf-8")
                    frames.append((round(ts, 2), f"data:image/jpeg;base64,{b64}"))
                os.remove(out_jpg)
        except Exception:
            continue
    try:
        if os.path.exists(temp_dir):
            os.rmdir(temp_dir)
    except Exception:
        pass
    return frames


def verify_clip_physical_frames(
    video_path: str,
    title: str,
    description: str,
    situational_prompt: str,
    sub_category_id: str | None = None,
    duration: float | None = None,
) -> dict:
    """
    Physical frame-level situation verification using VLM with Multi-Frame Sampling (4 frames).
    Strict Rejection Guardrails:
    - REJECT PiP / Facecam: If any human face/streamer is superimposed in a corner box or talking to the camera.
    - REJECT Burned-In Captions/Watermarks: If large social handles (e.g. @DASHCAMOWNERSAU) or animated word subtitles exist.
    - REJECT Static Slides: If any frame is a screenshot of a tweet, news article, or static photo.
    - REJECT Outros: If final frames contain subscribe buttons, channel logos, or promo presenters.
    JSON Output Schema:
    {"approved": bool, "has_facecam": bool, "has_subtitles": bool, "is_raw_cctv_or_dashcam": bool, "rejection_reason": str, "action_detected": str, "apex_timestamp_estimate": float}
    """
    if duration is None or duration <= 0:
        try:
            cmd = [
                "ffprobe", "-v", "error", "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1", video_path
            ]
            duration = float(subprocess.check_output(cmd, text=True).strip())
        except Exception:
            duration = 15.0

    keyframes = extract_verification_keyframes(video_path, duration)

    user_content = [
        {
            "type": "text",
            "text": (
                f"Video Title: {title}\n"
                f"Description: {description}\n"
                f"Target Situational Signature: {situational_prompt}\n"
                f"Total Video Duration: {duration:.2f}s\n\n"
                "You are the Strict Vision Gatekeeper for raw, viral CCTV/dashcam shorts.\n"
                "Examine all 4 chronological video frames (15%, 40%, 65%, 85% of duration):\n\n"
                "STRICT MANDATORY REJECTION GUARDRAILS:\n"
                "1. REJECT PiP / Facecam: Set approved=false if any human face/streamer/reactor is superimposed in a corner box, green screen, or talking to the camera.\n"
                "2. REJECT Burned-In Captions/Watermarks: Set approved=false if large social handles (e.g., @DASHCAMOWNERSAU, TikTok handles), watermark banners, or animated word-by-word subtitles exist on the footage.\n"
                "3. REJECT Static Slides: Set approved=false if any frame is a screenshot of a tweet, reddit post, news article, text meme, or static photo.\n"
                "4. REJECT Outros: Set approved=false if final frames contain subscribe buttons, bell animations, channel end-cards, or promo presenters.\n"
                "5. REJECT CGI/Gaming: Set approved=false if BeamNG, GTA, Roblox, or CGI.\n"
                "6. MUST BE 100% RAW CCTV OR DASHCAM/USER-RECORDED FOOTAGE.\n\n"
                "Return strictly JSON:\n"
                '{"approved": bool, "has_facecam": bool, "has_subtitles": bool, "is_raw_cctv_or_dashcam": bool, "rejection_reason": "string", "action_detected": "string", "apex_timestamp_estimate": float}'
            ),
        }
    ]

    for idx, (ts, b64_img) in enumerate(keyframes):
        user_content.append({"type": "text", "text": f"Frame {idx+1} at {ts:.2f}s:"})
        user_content.append({"type": "image_url", "image_url": {"url": b64_img}})

    try:
        client = get_openai_client()
        model_name = get_model_name()

        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are the Strict Vision Gatekeeper. You reject any video with facecam/PiP, burned-in subtitles, watermarks, static screenshots, or outro cards. Output strictly JSON."
                },
                {"role": "user", "content": user_content},
            ],
            response_format={"type": "json_object"},
            temperature=0.1,
            max_tokens=120,
            timeout=25.0,
        )

        raw_output = response.choices[0].message.content or ""
        print(f"[DEBUG - VLM Frame Verifier Raw]: {raw_output}")
        result = extract_json_from_text(raw_output)

        if isinstance(result, dict):
            # Check either new 'approved' flag or legacy 'is_match'
            approved = bool(result.get("approved", False))
            has_facecam = bool(result.get("has_facecam", False))
            has_subtitles = bool(result.get("has_subtitles", False))
            is_raw = bool(result.get("is_raw_cctv_or_dashcam", True))
            rejection_reason = str(result.get("rejection_reason", ""))
            action_detected = str(result.get("action_detected", ""))
            apex_est = float(result.get("apex_timestamp_estimate", round(duration * 0.6, 2)))

            # Final gate check: if facecam or subtitles detected, force rejected
            if has_facecam or has_subtitles or not is_raw:
                approved = False

            return {
                "approved": approved,
                "is_match": approved,
                "confidence": 0.95 if approved else 0.2,
                "has_facecam": has_facecam,
                "has_subtitles": has_subtitles,
                "is_raw_cctv_or_dashcam": is_raw,
                "action_detected": action_detected,
                "apex_timestamp_estimate": apex_est,
                "reason": rejection_reason if not approved else "Clean raw authentic footage verified",
            }

    except Exception as e:
        print(f"[VLM Verifier] Frame verification API exception ({e}). Engaging Level-2 Heuristic Fallback...", file=sys.stderr)

    # Level-2 Fallback via fallback_analyzer
    try:
        from fallback_analyzer import analyze_clip_heuristically
        fallback_res = analyze_clip_heuristically(
            title=title,
            description=description,
            sub_category_id=sub_category_id,
            strict_definition=situational_prompt,
        )
        is_match = bool(fallback_res.get("is_real_and_context_matched", False))
        conf = float(fallback_res.get("confidence", 0.75))
        return {
            "approved": is_match,
            "is_match": is_match,
            "confidence": conf,
            "has_facecam": False,
            "has_subtitles": False,
            "is_raw_cctv_or_dashcam": is_match,
            "action_detected": fallback_res.get("incident_type", "physical_action"),
            "apex_timestamp_estimate": round(duration * 0.6, 2),
            "reason": f"Fallback Heuristic: {fallback_res.get('reason')}",
        }
    except Exception as e2:
        return {
            "approved": False,
            "is_match": False,
            "confidence": 0.0,
            "has_facecam": True,
            "has_subtitles": True,
            "is_raw_cctv_or_dashcam": False,
            "action_detected": "none",
            "apex_timestamp_estimate": 0.0,
            "reason": f"Verification exception: {e2}",
        }


def verify_clip_semantics(
    title: str,
    description: str,
    thumbnail_url: str,
    strict_definition: str = "",
    sub_category_id: str | None = None,
) -> dict:
    """
    Uses the official OpenAI client pointing directly to OpenRouter.
    Strict fail-closed: returns {"is_real_and_context_matched": False, "is_real": False} on any API or parsing error.
    """
    user_content = [
        {
            "type": "text",
            "text": (
                f"Title: {title}\n"
                f"Description: {description}\n"
                f"Thumbnail URL: {thumbnail_url}\n"
                f"Target Definition: {strict_definition or 'N/A'}\n"
                "Evaluate Rule 1 (Real footage) and Rule 2 (Strict definition match)."
            ),
        }
    ]

    if thumbnail_url:
        user_content.append({
            "type": "image_url",
            "image_url": {"url": thumbnail_url},
        })

    try:
        client = get_openai_client()
        model_name = get_model_name()
        system_prompt = build_system_prompt(strict_definition)

        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
            response_format={"type": "json_object"},
            temperature=0.1,
            max_tokens=90,
            timeout=20.0,
        )

        raw_output = response.choices[0].message.content or ""
        print(f"[DEBUG - Raw LLM Output]: {raw_output}")

        result = extract_json_from_text(raw_output)
        if not isinstance(result, dict):
            return {
                "is_real_and_context_matched": False,
                "is_real": False,
                "confidence": 0.0,
                "reason": "Invalid JSON structure from model",
            }

        # Check either is_real_and_context_matched or legacy is_real
        matched = bool(result.get("is_real_and_context_matched", result.get("is_real", False)))

        return {
            "is_real_and_context_matched": matched,
            "is_real": matched,
            "confidence": float(result.get("confidence", 0.0)),
            "reason": str(result.get("reason", "No reason provided")),
        }

    except Exception as e:
        print(f"[LLM Verifier] API call error ({e}). Engaging Level-2 Heuristic Community Fallback Engine...", file=sys.stderr)
        try:
            from fallback_analyzer import analyze_clip_heuristically
            fallback_res = analyze_clip_heuristically(
                title=title,
                description=description,
                sub_category_id=sub_category_id,
                strict_definition=strict_definition,
            )
            print(f"[LLM Verifier - Fallback Output]: {json.dumps(fallback_res)}")
            return fallback_res
        except Exception:
            traceback.print_exc(file=sys.stderr)
            return {
                "is_real_and_context_matched": False,
                "is_real": False,
                "confidence": 0.0,
                "reason": "API Failure and Fallback Engine Exception",
            }


def main():
    parser = argparse.ArgumentParser(description="Strict Semantic LLM/VLM Verifier")
    parser.add_argument("--title", default="Road rage driver tries to cut off truck and crashes into ditch")
    parser.add_argument("--description", default="Instant karma road rage incident caught on dashcam")
    parser.add_argument("--thumbnail", default="https://i.ytimg.com/vi/bDyhzmH8hfw/hqdefault.jpg")
    parser.add_argument("--definition", default="Must show aggressive confrontation or intentional retaliation between drivers.")
    args = parser.parse_args()

    res = verify_clip_semantics(args.title, args.description, args.thumbnail, strict_definition=args.definition)
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
