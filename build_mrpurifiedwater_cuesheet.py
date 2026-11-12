import os
import json
import subprocess

CUE_SHEET_PATH = "cue_sheet.json"
SKYFALL_HOOK = os.path.abspath("public/audio/stems/skyfall_this_is_the_end.mp3")

clips_data = [
    {
        "id": "this_is_the_end_5",
        "videoPath": os.path.abspath("public/clips/this_is_the_end_5_trimmed.mp4"),
        "voPath": os.path.abspath("public/audio/vo_fate_5.mp3"),
        "subtitleText": "He completely gave up on balance.",
        "durationInFrames": 120,
        "voDuration": 2.976,
        "freezeFrameOffset": 50, # Frame where belly slide surrender begins
        "freezeDurationFrames": 36,
        "audioHookPath": SKYFALL_HOOK
    },
    {
        "id": "this_is_the_end_4",
        "videoPath": os.path.abspath("public/clips/this_is_the_end_4_trimmed.mp4"),
        "voPath": os.path.abspath("public/audio/vo_fate_4.mp3"),
        "subtitleText": "Accepted his slide to the street.",
        "durationInFrames": 146,
        "voDuration": 2.736,
        "freezeFrameOffset": 60, # Frame where flat on back slide begins
        "freezeDurationFrames": 36,
        "audioHookPath": SKYFALL_HOOK
    },
    {
        "id": "this_is_the_end_3",
        "videoPath": os.path.abspath("public/clips/this_is_the_end_3_trimmed.mp4"),
        "voPath": os.path.abspath("public/audio/vo_fate_3.mp3"),
        "subtitleText": "Zero resistance, total surrender.",
        "durationInFrames": 150,
        "voDuration": 3.384,
        "freezeFrameOffset": 65, # Moment of sliding past the driveway
        "freezeDurationFrames": 36,
        "audioHookPath": SKYFALL_HOOK
    },
    {
        "id": "this_is_the_end_2",
        "videoPath": os.path.abspath("public/clips/this_is_the_end_2_trimmed.mp4"),
        "voPath": os.path.abspath("public/audio/vo_fate_2.mp3"),
        "subtitleText": "When the entire roof takes you with it.",
        "durationInFrames": 120,
        "voDuration": 2.904,
        "freezeFrameOffset": 45, # Frame where roof snow breaks off
        "freezeDurationFrames": 36,
        "audioHookPath": SKYFALL_HOOK
    },
    {
        "id": "this_is_the_end_1",
        "videoPath": os.path.abspath("public/clips/this_is_the_end_1_trimmed.mp4"),
        "voPath": os.path.abspath("public/audio/vo_fate_1.mp3"),
        "subtitleText": "It do go down, Robert.",
        "durationInFrames": 180,
        "voDuration": 2.616,
        "freezeFrameOffset": 85, # The exact iconic frame where Robert stares at the drop: "It DO go down!"
        "freezeDurationFrames": 45,
        "audioHookPath": SKYFALL_HOOK
    }
]

cue_sheet = {
    "titleHeader": "Ranking Best Of",
    "subjectHeader": "This Is The End Moments",
    "versionTag": "(Surrender Version)",
    "subCategoryId": "people_accepting_fate",
    "subCategoryName": "THIS IS THE END",
    "clips": clips_data
}

with open(CUE_SHEET_PATH, "w", encoding="utf-8") as f:
    json.dump(cue_sheet, f, indent=2)

print("Updated cue_sheet.json with @MrPurifiedWater visual architecture and Skyfall 'This is the end...' meme audio hook!")
