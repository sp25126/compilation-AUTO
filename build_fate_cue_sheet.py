import os
import sys
import json
import asyncio
import subprocess
import edge_tts

PYTHON_EXE = r"C:\sp\ai-agent\ai_agent_env\Scripts\python.exe"
VOICE = "en-US-ChristopherNeural"

clips_config = [
    {
        "rank": 5,
        "video": "public/clips/this_is_the_end_5_trimmed.mp4",
        "audio": "public/audio/vo_fate_5.mp3",
        "subtitle": "He completely gave up on balance."
    },
    {
        "rank": 4,
        "video": "public/clips/this_is_the_end_4_trimmed.mp4",
        "audio": "public/audio/vo_fate_4.mp3",
        "subtitle": "Accepted his slide to the street."
    },
    {
        "rank": 3,
        "video": "public/clips/this_is_the_end_3_trimmed.mp4",
        "audio": "public/audio/vo_fate_3.mp3",
        "subtitle": "Zero resistance, total surrender."
    },
    {
        "rank": 2,
        "video": "public/clips/this_is_the_end_2_trimmed.mp4",
        "audio": "public/audio/vo_fate_2.mp3",
        "subtitle": "When the entire roof takes you with it."
    },
    {
        "rank": 1,
        "video": "public/clips/this_is_the_end_1_trimmed.mp4",
        "audio": "public/audio/vo_fate_1.mp3",
        "subtitle": "It do go down, Robert."
    }
]

async def gen_vo(text, path):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    comm = edge_tts.Communicate(text, VOICE)
    await comm.save(path)

def get_duration(fpath):
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", fpath]
    return float(subprocess.check_output(cmd, text=True).strip())

async def main():
    clips_list = []
    fps = 30
    
    for cfg in clips_config:
        print(f"Generating VO for Rank {cfg['rank']}: '{cfg['subtitle']}'")
        await gen_vo(cfg["subtitle"], cfg["audio"])
        vo_dur = get_duration(cfg["audio"])
        vid_dur = get_duration(cfg["video"])
        
        # durationInFrames should exactly match the video duration in frames
        duration_frames = int(round(vid_dur * fps))
        print(f"Rank {cfg['rank']}: vid_dur={vid_dur}s ({duration_frames} frames), vo_dur={vo_dur}s")
        
        clips_list.append({
            "id": f"this_is_the_end_{cfg['rank']}",
            "videoPath": os.path.abspath(cfg["video"]),
            "voPath": os.path.abspath(cfg["audio"]),
            "subtitleText": cfg["subtitle"],
            "durationInFrames": duration_frames,
            "voDuration": vo_dur
        })

    cue_sheet = {
        "subCategoryId": "this_is_the_end",
        "subCategoryName": "THIS IS THE END",
        "clips": clips_list
    }

    with open("cue_sheet.json", "w", encoding="utf-8") as f:
        json.dump(cue_sheet, f, indent=2)

    print("Successfully written cue_sheet.json with 5 ranked clips!")

if __name__ == "__main__":
    asyncio.run(main())
