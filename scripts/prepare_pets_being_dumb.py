import json
import os
import subprocess

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CLIPS_DIR = os.path.join(BASE_DIR, "public", "clips")
STEMS_DIR = os.path.join(BASE_DIR, "public", "audio", "stems")
TEMP_DIR = os.path.join(BASE_DIR, "temp_harvest")

os.makedirs(CLIPS_DIR, exist_ok=True)

CLIP_SPECS = [
    {
        "id": "pets_dumb_5",
        "rank": 5,
        "level": 1,
        "raw_file": os.path.join(TEMP_DIR, "pet_y_wJMveFiz57A.mp4"),
        "trim_start": 1.50,
        "trim_duration": 5.50,   # 165 frames: cat stretches on table edge -> rolls off onto floor
        "duration_frames": 165,
    },
    {
        "id": "pets_dumb_4",
        "rank": 4,
        "level": 2,
        "raw_file": os.path.join(TEMP_DIR, "pet_r8_s37dl15ourq71.mp4"),
        "trim_start": 6.00,
        "trim_duration": 8.00,   # 240 frames: dog stuck in open door -> owner "opens" invisible door -> walks in
        "duration_frames": 240,
    },
    {
        "id": "pets_dumb_3",
        "rank": 3,
        "level": 3,
        "raw_file": os.path.join(TEMP_DIR, "pet_r1_5pmp33azi0da1.mp4"),
        "trim_start": 0.00,
        "trim_duration": 8.50,   # 255 frames: orange kitten hops & launches full-send off bed missing mirror
        "duration_frames": 255,
    },
    {
        "id": "pets_dumb_2",
        "rank": 2,
        "level": 4,
        "raw_file": os.path.join(TEMP_DIR, "pet_y_QE-T_kikIKI.mp4"),
        "trim_start": 0.00,
        "trim_duration": 8.50,   # 255 frames: cat licks ice cream -> instant wide-eyed open-mouth brain freeze
        "duration_frames": 255,
    },
    {
        "id": "pets_dumb_1",
        "rank": 1,
        "level": 5,
        "raw_file": os.path.join(TEMP_DIR, "pet_y_7AXzLdttiUY.mp4"),
        "trim_start": 6.50,
        "trim_duration": 7.00,   # 210 frames: excited Doberman jumps straight through glass coffee table
        "duration_frames": 210,
    },
]


def prepare_clips():
    print("Preparing 5 Clips for PETS BEING DUMB...\n")
    cue_clips = []

    for spec in CLIP_SPECS:
        clip_id = spec["id"]
        out_clip_path = os.path.join(CLIPS_DIR, f"{clip_id}_trimmed.mp4")

        print(
            f"Trimming Rank {spec['rank']} [{clip_id}] from {os.path.basename(spec['raw_file'])} "
            f"(start={spec['trim_start']}s, dur={spec['trim_duration']}s)..."
        )
        trim_cmd = [
            "ffmpeg", "-y",
            "-ss", f"{spec['trim_start']:.2f}",
            "-t", f"{spec['trim_duration']:.2f}",
            "-i", spec["raw_file"],
            "-r", "30",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            out_clip_path,
        ]
        subprocess.run(trim_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        cue_clips.append({
            "id": clip_id,
            "videoPath": out_clip_path,
            "durationInFrames": spec["duration_frames"],
        })

    cue_sheet = {
        "titleHeader": "Ranking Best Of",
        "subjectHeader": "Pets Being Dumb Moments",
        "versionTag": "(0 Braincells Edition)",
        "subCategoryId": "pets_being_dumb",
        "subCategoryName": "PETS BEING DUMB",
        "globalAudioPath": os.path.join(STEMS_DIR, "karma_comedy_master.mp3"),
        "clips": cue_clips,
    }

    cue_sheet_path = os.path.join(BASE_DIR, "cue_sheet.json")
    with open(cue_sheet_path, "w", encoding="utf-8") as f:
        json.dump(cue_sheet, f, indent=2)

    print("\nAll 5 Pets Being Dumb clips trimmed and cue_sheet.json updated!")


if __name__ == "__main__":
    prepare_clips()
