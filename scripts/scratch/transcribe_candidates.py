import glob
import os
import subprocess
import json
import speech_recognition as sr

r = sr.Recognizer()

mp4s = glob.glob("temp_harvest/dialogue_loop_real_life/*.mp4")

for mp4 in sorted(mp4s):
    base = os.path.splitext(os.path.basename(mp4))[0]
    wav = f"temp_harvest/dialogue_loop_real_life/{base}.wav"
    if not os.path.exists(wav):
        cmd = [
            "ffmpeg", "-y", "-i", mp4,
            "-vn", "-ac", "1", "-ar", "16000",
            wav
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    try:
        with sr.AudioFile(wav) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data)
            print(f"[{base}] -> {text}")
    except Exception as e:
        print(f"[{base}] -> (No transcript or error: {e})")
