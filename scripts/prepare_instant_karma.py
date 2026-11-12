import json
import os
import subprocess

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CLIPS_DIR = os.path.join(BASE_DIR, "public", "clips")
STEMS_DIR = os.path.join(BASE_DIR, "public", "audio", "stems")
TEMP_DIR = os.path.join(BASE_DIR, "temp_harvest")

os.makedirs(CLIPS_DIR, exist_ok=True)

# Every clip below preserves 100% of the story: Cause -> Payoff -> Reaction/Aftermath.
CLIP_SPECS = [
    {
        "id": "instant_karma_5",
        "rank": 5,
        "level": 1,
        "raw_file": os.path.join(TEMP_DIR, "karma_y1.mp4"),
        "trim_start": 0.00,
        "trim_duration": 13.50,  # full story: scare -> fall -> costume wearer panics -> guy laughs
        "speed": 1.40,           # 13.50 / 1.40 = 9.64s -> 289 frames
        "duration_frames": 289,
    },
    {
        "id": "instant_karma_4",
        "rank": 4,
        "level": 2,
        "raw_file": os.path.join(TEMP_DIR, "ik_vWa9iYYPYF4.mp4"),
        "trim_start": 10.50,
        "trim_duration": 9.00,   # 10.5->19.5s: raises arms -> rival passes at finish line -> collapses on track
        "speed": 1.00,
        "duration_frames": 270,
    },
    {
        "id": "instant_karma_3",
        "rank": 3,
        "level": 3,
        "raw_file": os.path.join(TEMP_DIR, "karma_y2.mp4"),
        "trim_start": 0.00,
        "trim_duration": 11.00,  # 0.0->11.0s: blows red air horn -> man confronts -> instant slap
        "speed": 1.25,           # 11.00 / 1.25 = 8.80s -> 264 frames
        "duration_frames": 264,
    },
    {
        "id": "instant_karma_2",
        "rank": 2,
        "level": 4,
        "raw_file": os.path.join(TEMP_DIR, "ik3_6yCia4DGigs.mp4"),
        "trim_start": 3.00,
        "trim_duration": 9.50,   # 3.0->12.5s: kicks concrete fence -> upper slab slams down & traps his leg
        "speed": 1.00,
        "duration_frames": 285,
    },
    {
        "id": "instant_karma_1",
        "rank": 1,
        "level": 5,
        "raw_file": os.path.join(TEMP_DIR, "karma_y3.mp4"),
        "trim_start": 1.00,
        "trim_duration": 7.50,   # 1.0->8.5s: air horn on bridge -> picked up -> tossed over railing -> splash
        "speed": 1.00,
        "duration_frames": 225,
    },
]


def prepare_clips():
    print("Preparing 5 Complete-Story Clips for INSTANT KARMA...\n")
    cue_clips = []

    for spec in CLIP_SPECS:
        clip_id = spec["id"]
        out_clip_path = os.path.join(CLIPS_DIR, f"{clip_id}_trimmed.mp4")
        spd = spec.get("speed", 1.0)

        print(
            f"Trimming Rank {spec['rank']} [{clip_id}] from {os.path.basename(spec['raw_file'])} "
            f"(start={spec['trim_start']}s, src_dur={spec['trim_duration']}s, speed={spd}x, out_frames={spec['duration_frames']})..."
        )
        filter_args = []
        if abs(spd - 1.0) > 0.01:
            filter_args = ["-vf", f"setpts=PTS/{spd}", "-af", f"atempo={spd}"]

        trim_cmd = [
            "ffmpeg", "-y",
            "-ss", f"{spec['trim_start']:.2f}",
            "-t", f"{spec['trim_duration']:.2f}",
            "-i", spec["raw_file"],
            *filter_args,
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
        "subjectHeader": "Instant Karma Moments",
        "versionTag": "(Caught On Camera)",
        "subCategoryId": "instant_karma",
        "subCategoryName": "INSTANT KARMA",
        "globalAudioPath": os.path.join(STEMS_DIR, "karma_comedy_master.mp3"),
        "clips": cue_clips,
    }

    cue_sheet_path = os.path.join(BASE_DIR, "cue_sheet.json")
    with open(cue_sheet_path, "w", encoding="utf-8") as f:
        json.dump(cue_sheet, f, indent=2)

    print("\nAll 5 Instant Karma clips trimmed and cue_sheet.json updated!")


if __name__ == "__main__":
    prepare_clips()
