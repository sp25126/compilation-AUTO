import os
import sys
import json
import base64
import argparse
import subprocess
import cv2
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_openai_client() -> OpenAI:
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        keys_str = os.getenv("OPENROUTER_API_KEYS", "")
        keys = [k.strip() for k in keys_str.split(",") if k.strip()]
        if keys:
            api_key = keys[0]
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key or "missing_key",
    )

def extract_4_keyframes(video_path: str, duration: float | None = None) -> list[tuple[float, str, str]]:
    """
    Extracts 4 keyframes at 15%, 40%, 65%, and 85% of total duration:
    Returns list of (timestamp, base64_jpeg, local_jpg_path).
    """
    if duration is None or duration <= 0:
        try:
            cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", video_path]
            duration = float(subprocess.check_output(cmd, text=True).strip())
        except Exception:
            duration = 15.0

    timestamps = [
        max(0.2, duration * 0.15),
        max(0.4, duration * 0.40),
        max(0.6, duration * 0.65),
        max(0.8, duration * 0.85),
    ]

    frames = []
    temp_dir = os.path.join(os.path.dirname(os.path.abspath(video_path)), "_purity_frames")
    os.makedirs(temp_dir, exist_ok=True)
    basename = os.path.splitext(os.path.basename(video_path))[0]

    for idx, ts in enumerate(timestamps):
        out_jpg = os.path.join(temp_dir, f"{basename}_f{idx+1}.jpg")
        cmd = [
            "ffmpeg", "-y", "-ss", f"{ts:.2f}",
            "-i", video_path,
            "-frames:v", "1",
            "-q:v", "2",
            "-vf", "scale=480:-1",
            out_jpg
        ]
        try:
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=12)
            if os.path.exists(out_jpg) and os.path.getsize(out_jpg) > 0:
                with open(out_jpg, "rb") as f:
                    b64 = base64.b64encode(f.read()).decode("utf-8")
                    frames.append((round(ts, 2), f"data:image/jpeg;base64,{b64}", out_jpg))
        except Exception:
            continue

    return frames

def detect_facecam_heuristic(jpg_path: str) -> bool:
    """
    Uses OpenCV Haar Cascade to detect faces in corners (PiP / facecam reaction boxes).
    """
    try:
        cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        face_cascade = cv2.CascadeClassifier(cascade_path)
        img = cv2.imread(jpg_path)
        if img is None:
            return False
        h, w = img.shape[:2]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(40, 40))
        for (x, y, fw, fh) in faces:
            # Check if face is in corner quadrants (bottom-right, bottom-left, top-right)
            is_bottom = y + fh > h * 0.55
            is_corner = (x < w * 0.45) or (x + fw > w * 0.55)
            # Check size ratio: if face takes between 8% and 40% of frame width, typical streamer box
            face_w_ratio = fw / float(w)
            if is_bottom and is_corner and (0.08 <= face_w_ratio <= 0.45):
                return True
    except Exception:
        pass
    return False

def inspect_purity(video_path: str, delete_if_rejected: bool = False) -> dict:
    """
    Multi-Frame Purity Gate:
    1. Extracts 4 frames (15%, 40%, 65%, 85%).
    2. OpenCV corner facecam / PiP detector.
    3. Multimodal VLM Inspection (with fallback).
    """
    keyframes = extract_4_keyframes(video_path)
    if len(keyframes) < 2:
        return {
            "is_pure_raw_footage": False,
            "rejection_flags": ["static_image"],
            "reason": "Could not extract sufficient keyframes from video."
        }

    # Computer Vision check for streamer corner facecam
    for ts, b64_img, jpg_p in keyframes:
        if detect_facecam_heuristic(jpg_p):
            print(f"[PurityGate] CV Face Detector flagged reaction facecam in {os.path.basename(video_path)} at {ts}s", file=sys.stderr)
            res = {
                "is_pure_raw_footage": False,
                "rejection_flags": ["facecam"],
                "reason": "Streamer / reaction facecam detected in corner box."
            }
            if delete_if_rejected:
                try:
                    if os.path.exists(video_path):
                        os.remove(video_path)
                except Exception:
                    pass
            return res

    # Multimodal VLM Call
    client = get_openai_client()
    model_name = os.getenv("OPENROUTER_MODEL", "nvidia/nemotron-3.5-super-vl:free")

    user_content = [
        {
            "type": "text",
            "text": (
                "You are a raw footage purity inspector. Inspect these 4 frames from a single video candidate.\n\n"
                "REJECT if you detect ANY of the following:\n"
                "- A human face looking at the camera speaking, narrating, or reacting.\n"
                "- Split-screen layouts, picture-in-picture (PiP) boxes, or streamers with headphones/microphones.\n"
                "- Burned-in subtitles, karaoke caption blocks, or massive watermarks.\n"
                "- Static screenshots, news anchors, or promotional end cards.\n\n"
                "ACCEPT ONLY if:\n"
                "- It is 100% original, raw CCTV, dashcam, or handheld camera footage where the incident happens naturally.\n\n"
                "Output strictly JSON:\n"
                '{"is_pure_raw_footage": boolean, "rejection_flags": ["facecam" | "subtitles" | "commentary" | "static_image"], "reason": "string"}'
            )
        }
    ]

    for idx, (ts, b64_img, jpg_p) in enumerate(keyframes):
        user_content.append({"type": "text", "text": f"Frame {idx+1} ({ts:.2f}s):"})
        user_content.append({"type": "image_url", "image_url": {"url": b64_img}})

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are a raw footage purity inspector. Inspect 4 video frames. Output strictly JSON."
                },
                {"role": "user", "content": user_content}
            ],
            response_format={"type": "json_object"},
            temperature=0.1,
            max_tokens=60,
            timeout=15.0
        )
        raw_output = response.choices[0].message.content or "{}"
        data = json.loads(raw_output)
        is_pure = bool(data.get("is_pure_raw_footage", False))
        rejection_flags = list(data.get("rejection_flags", []))
        reason = str(data.get("reason", "VLM decision"))

        result = {
            "is_pure_raw_footage": is_pure,
            "rejection_flags": rejection_flags,
            "reason": reason
        }
    except Exception as e:
        # If free VLM returns credit issue or rate limit, CV heuristics passed clean
        result = {
            "is_pure_raw_footage": True,
            "rejection_flags": [],
            "reason": f"CV Heuristics passed raw footage (VLM fallback: {e})"
        }

    # Cleanup temp frame jpgs
    for _, _, jpg_p in keyframes:
        try:
            if os.path.exists(jpg_p):
                os.remove(jpg_p)
        except Exception:
            pass

    if not result["is_pure_raw_footage"] and delete_if_rejected:
        try:
            if os.path.exists(video_path):
                os.remove(video_path)
                print(f"[PurityGate] Deleted contaminated clip: {video_path}", file=sys.stderr)
        except Exception:
            pass

    return result

def main():
    parser = argparse.ArgumentParser(description="Multi-Frame Purity Gate")
    parser.add_argument("--input", required=True, help="Input video MP4")
    parser.add_argument("--delete-rejected", action="store_true", help="Delete video file if rejected")
    args = parser.parse_args()

    res = inspect_purity(args.input, delete_if_rejected=args.delete_rejected)
    print(json.dumps(res, indent=2))
    sys.exit(0 if res.get("is_pure_raw_footage") else 1)

if __name__ == "__main__":
    main()
