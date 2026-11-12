import os
import subprocess
import json

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CLIPS_DIR = os.path.join(BASE_DIR, "public", "clips")
AUDIO_DIR = os.path.join(BASE_DIR, "public", "audio")
STEMS_DIR = os.path.join(AUDIO_DIR, "stems")
TEMP_DIR = os.path.join(BASE_DIR, "temp_harvest")

os.makedirs(CLIPS_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)

# Every clip below was visually inspected frame-by-frame at 2fps and 5fps:
#   trim_start -> buildup -> T_cause (point of no return) -> T_freeze (realization/mid-air)
#   freeze_offset (in frames @ 30fps) is strictly AFTER the cause occurs on screen.
CLIP_SPECS = [
    {
        "id": "this_is_the_end_5",
        "rank": 5,
        "level": 1,
        "raw_file": os.path.join(TEMP_DIR, "raw_a3CUaOtHQ4c.mp4"),
        "trim_start": 0.0,
        "trim_duration": 5.67,   # 170 frames (80f buildup + 90f freeze)
        "duration_frames": 170,
        "freeze_offset": 80,     # 2.67s: old man slips at ~2.0s and is completely horizontal mid-air over pool
        "freeze_duration": 90,   # 3.00s solid freeze so full "THIS IS THE END" vocal finishes cleanly
    },
    {
        "id": "this_is_the_end_4",
        "rank": 4,
        "level": 2,
        "raw_file": os.path.join(TEMP_DIR, "raw_8pvQ-6zmAzA.mp4"),
        "trim_start": 15.8,
        "trim_duration": 6.00,   # 180 frames (90f buildup + 90f freeze)
        "duration_frames": 180,
        "freeze_offset": 90,     # 3.00s (18.80s abs): leaped off dock, came up short, mid-air over dark water
        "freeze_duration": 90,   # 3.00s solid freeze
    },
    {
        "id": "this_is_the_end_3",
        "rank": 3,
        "level": 3,
        "raw_file": os.path.join(TEMP_DIR, "raw_zGNCEtg-acY.mp4"),
        "trim_start": 21.6,
        "trim_duration": 6.00,   # 180 frames (90f buildup + 90f freeze)
        "duration_frames": 180,
        "freeze_offset": 90,     # 3.00s (24.60s abs): swung over top bar, lost grip, upside-down mid-air
        "freeze_duration": 90,   # 3.00s solid freeze
    },
    {
        "id": "this_is_the_end_2",
        "rank": 2,
        "level": 4,
        "raw_file": os.path.join(TEMP_DIR, "raw__1iObgKLMVU.mp4"),
        "trim_start": 8.8,
        "trim_duration": 6.30,   # 189 frames (99f buildup + 90f freeze)
        "duration_frames": 189,
        "freeze_offset": 99,     # 3.30s (12.10s abs): rocketed off water slide ramp, flying 10ft over pool
        "freeze_duration": 90,   # 3.00s solid freeze
    },
    {
        "id": "this_is_the_end_1",
        "rank": 1,
        "level": 5,
        "raw_file": os.path.join(TEMP_DIR, "raw_DYzT-Pk6Ogw.mp4"),
        "trim_start": 17.8,
        "trim_duration": 6.60,   # 198 frames (108f buildup + 90f freeze)
        "duration_frames": 198,
        "freeze_offset": 108,    # 3.60s (21.40s abs): "IT DO GO DOWN!" boat tips over waterfall edge, Robert lunges
        "freeze_duration": 90,   # 3.00s solid freeze
    },
]


def prepare_clips():
    print("Preparing 5 Frame-Verified Clips for THIS IS THE END...\n")
    cue_clips = []

    for spec in CLIP_SPECS:
        clip_id = spec["id"]
        out_clip_path = os.path.join(CLIPS_DIR, f"{clip_id}_trimmed.mp4")
        freeze_img_path = os.path.join(CLIPS_DIR, f"{clip_id}_freeze.jpg")

        print(f"Trimming Rank {spec['rank']} [{clip_id}] from {os.path.basename(spec['raw_file'])} "
              f"(start={spec['trim_start']}s, dur={spec['trim_duration']}s, freeze@{spec['freeze_offset']}f)...")
        vf_args = ["-vf", "crop=ih*9/16:ih"] if spec["rank"] == 5 else []
        trim_cmd = [
            "ffmpeg", "-y",
            "-ss", f"{spec['trim_start']:.2f}",
            "-t", f"{spec['trim_duration']:.2f}",
            "-i", spec["raw_file"],
            *vf_args,
            "-r", "30",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            out_clip_path,
        ]
        subprocess.run(trim_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        freeze_sec = spec["freeze_offset"] / 30.0
        freeze_cmd = [
            "ffmpeg", "-y",
            "-ss", f"{freeze_sec:.3f}",
            "-i", out_clip_path,
            "-vframes", "1",
            "-q:v", "2",
            freeze_img_path,
        ]
        subprocess.run(freeze_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        cue_clips.append({
            "id": clip_id,
            "videoPath": out_clip_path,
            "freezeImagePath": freeze_img_path,
            "punchlineText": "THIS IS THE END",
            "durationInFrames": spec["duration_frames"],
            "freezeFrameOffset": spec["freeze_offset"],
            "freezeDurationFrames": spec["freeze_duration"],
            "audioHookPath": os.path.join(STEMS_DIR, "skyfall_this_is_the_end.mp3"),
        })

    cue_sheet = {
        "titleHeader": "Ranking Best Of",
        "subjectHeader": "This Is The End Moments",
        "versionTag": "(Surrender Version)",
        "subCategoryId": "people_accepting_fate",
        "subCategoryName": "THIS IS THE END",
        "clips": cue_clips,
    }

    cue_sheet_path = os.path.join(BASE_DIR, "cue_sheet.json")
    with open(cue_sheet_path, "w", encoding="utf-8") as f:
        json.dump(cue_sheet, f, indent=2)

    print("\nAll 5 clips trimmed, freeze frames extracted, and cue_sheet.json updated!")


if __name__ == "__main__":
    prepare_clips()
