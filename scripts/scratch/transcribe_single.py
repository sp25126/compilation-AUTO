import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile("temp_harvest/dialogue_loop_real_life/688z.wav") as source:
    audio = r.record(source)
    print("Transcript:", r.recognize_google(audio))
