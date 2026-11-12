import json
import os
import subprocess

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMP_DIR = os.path.join(BASE_DIR, "temp_harvest", "one_million_aura_loss")
OUT_DIR = os.path.join(BASE_DIR, "public", "clips", "one_million_aura_loss")
os.makedirs(OUT_DIR, exist_ok=True)

CLIPS = [
    {
        "rank": 5,
        "level": 1,
        "name": "josh_hart_self_highfive",
        "aura_loss": "-10,000 AURA",
        "input": os.path.join(TEMP_DIR, "josh_hart_vertical.mp4"),
        "ss": 0.0,
        "t": 3.4,
        "speed": 0.85, # 3.4 / 0.85 = 4.0s (120 frames)
        "dur_frames": 120,
    },
    {
        "rank": 4,
        "level": 2,
        "name": "bridge_swagger_jacket_wind",
        "aura_loss": "-50,000 AURA",
        "input": os.path.join(TEMP_DIR, "aura_price_with_audio.mp4"),
        "ss": 0.0,
        "t": 6.2,
        "speed": 1.0, # 6.2s (186 frames)
        "dur_frames": 186,
    },
    {
        "rank": 3,
        "level": 3,
        "name": "impress_girls_bench_flip_faceplant",
        "aura_loss": "-100,000 AURA",
        "input": os.path.join(TEMP_DIR, "yt_boy_falls_impress.mp4"),
        "ss": 0.0,
        "t": 5.9,
        "speed": 1.0, # 5.9s (177 frames)
        "dur_frames": 177,
    },
    {
        "rank": 2,
        "level": 4,
        "name": "billiard_trickshot_bellyflop",
        "aura_loss": "-500,000 AURA",
        "input": os.path.join(TEMP_DIR, "aura_wcgw_trying_cool_3_lcdi0r4po98b1.mp4"),
        "ss": 0.0,
        "t": 7.5,
        "speed": 1.0, # 7.5s (225 frames)
        "dur_frames": 225,
    },
    {
        "rank": 1,
        "level": 5,
        "name": "river_stairs_20_step_mudslide",
        "aura_loss": "-1,000,000 AURA",
        "input": os.path.join(TEMP_DIR, "river_stairs_with_splash.mp4"),
        "ss": 0.0,
        "t": 10.0,
        "speed": 1.0, # 10.0s (300 frames)
        "dur_frames": 300,
    },
]

def render_clips():
    results = []
    for c in CLIPS:
        out_file = os.path.join(OUT_DIR, f"rank_{c['rank']}.mp4")
        spd = c["speed"]
        ss = c["ss"]
        t = c["t"]
        inp = c["input"]
        
        # Build filtergraph
        # Normalize audio volume with loudnorm or volume boost
        vf = f"setpts=PTS/{spd},fps=30,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black"
        af = f"atempo={spd},volume=1.8"
        
        cmd = [
            "ffmpeg", "-y",
            "-ss", str(ss),
            "-t", str(t),
            "-i", inp,
            "-vf", vf,
            "-af", af,
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "18",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-b:a", "192k",
            "-ar", "48000",
            out_file
        ]
        print(f"Processing Rank {c['rank']} (Level {c['level']})...")
        subprocess.run(cmd, check=True)
        
        # Get actual duration in frames
        probe = subprocess.check_output(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", out_file],
            text=True
        )
        dur_sec = float(json.loads(probe)["format"]["duration"])
        actual_frames = int(round(dur_sec * 30))
        print(f"  Rank {c['rank']} done -> {dur_sec:.2f}s ({actual_frames} frames)")
        
        results.append({
            "rank": c["rank"],
            "level": c["level"],
            "name": c["name"],
            "aura_loss": c["aura_loss"],
            "filePath": f"public/clips/one_million_aura_loss/rank_{c['rank']}.mp4",
            "durationInFrames": actual_frames,
            "freezeFrameOffset": int(actual_frames * 0.65),
            "freezeDurationFrames": 0,
        })
    
    with open(os.path.join(OUT_DIR, "clips_info.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("All 5 clips rendered successfully!")

if __name__ == "__main__":
    render_clips()
