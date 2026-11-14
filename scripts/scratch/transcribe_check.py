import whisper

model = whisper.load_model('base')
res = model.transcribe('temp_harvest/dialogue_loop_real_life/UrJcxXMYujk.mp4')
for seg in res['segments']:
    print(f"{seg['start']:.2f} -> {seg['end']:.2f}: {seg['text']}")
