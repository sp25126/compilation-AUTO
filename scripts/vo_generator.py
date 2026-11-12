import os
import sys
import json
import asyncio
import argparse
import subprocess
import edge_tts

DEFAULT_VOICE = "en-US-ChristopherNeural"

def generate_witty_vo_text(sub_category_name: str, rank: int, incident_desc: str = "") -> str:
    """
    Generates a single dry, witty setup sentence (4 to 7 words maximum).
    Category-aware templates.
    """
    cat_lower = sub_category_name.lower()
    if any(k in cat_lower for k in ["dog", "pet", "animal", "cat"]):
        dog_templates = [
            "The calculation was completely wrong.",
            "He thought the glass was open.",
            "Confidence was high, traction was zero.",
            "Bro forgot how his legs work.",
            "The zoomies claimed another victim.",
            "Not a single braincell was found.",
            "He accepted his fate mid-air."
        ]
        return dog_templates[(rank - 1) % len(dog_templates)]

    templates = [
        "Confidence was high, traction was zero.",
        "He realized his mistake immediately.",
        "Bro thought he had the right of way.",
        "Instant karma came without a warning.",
        "That maneuver did not go as planned.",
        "Physics always has the final word.",
        "He tried to show off, and failed."
    ]
    idx = (rank - 1) % len(templates)
    return templates[idx]

async def synthesize_vo(text: str, output_audio: str, voice: str = DEFAULT_VOICE):
    os.makedirs(os.path.dirname(os.path.abspath(output_audio)), exist_ok=True)
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_audio)

def get_audio_duration(file_path: str) -> float:
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    try:
        res = subprocess.check_output(cmd, text=True).strip()
        return float(res)
    except Exception:
        return 2.0

def generate_entry_for_clip(
    video_path: str,
    rank: int,
    sub_category_name: str,
    output_dir: str = "public/audio",
    custom_text: str | None = None
) -> dict:
    """
    Synthesizes edge-tts audio and returns metadata entry for cue_sheet.json.
    """
    os.makedirs(output_dir, exist_ok=True)
    vo_text = custom_text or generate_witty_vo_text(sub_category_name, rank)
    audio_filename = f"vo_rank_{rank}.mp3"
    audio_path = os.path.join(output_dir, audio_filename)

    asyncio.run(synthesize_vo(vo_text, audio_path))

    vo_dur = get_audio_duration(audio_path)

    # Get video duration to set frames
    vid_dur = 6.0
    try:
        cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", video_path]
        vid_dur = float(subprocess.check_output(cmd, text=True).strip())
    except Exception:
        pass

    fps = 30
    duration_frames = max(int(vid_dur * fps), int((vo_dur + 1.0) * fps))

    return {
        "videoPath": os.path.abspath(video_path),
        "voPath": os.path.abspath(audio_path),
        "subtitleText": vo_text,
        "voDuration": vo_dur,
        "durationInFrames": duration_frames,
        "rank": rank
    }

def main():
    parser = argparse.ArgumentParser(description="Minimal Voiceover & Subtitle Generator")
    parser.add_argument("--video", required=True, help="Path to trimmed video")
    parser.add_argument("--rank", type=int, default=1, help="Rank number (1-5)")
    parser.add_argument("--category", default="Instant Karma", help="Category name")
    parser.add_argument("--text", default=None, help="Custom VO text")
    args = parser.parse_args()

    entry = generate_entry_for_clip(
        video_path=args.video,
        rank=args.rank,
        sub_category_name=args.category,
        custom_text=args.text
    )
    print(json.dumps(entry, indent=2))

if __name__ == "__main__":
    main()
