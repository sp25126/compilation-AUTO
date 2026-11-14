import whisper, sys

video_path = sys.argv[1]
model = whisper.load_model('base')
res = model.transcribe(video_path, word_timestamps=True)
for seg in res['segments']:
    print(f"{seg['start']:.2f} -> {seg['end']:.2f}: {seg['text']}")
    for w in seg.get('words', []):
        print(f"   {w['start']:.2f} -> {w['end']:.2f}: {w['word']}")
