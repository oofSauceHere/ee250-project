import os
import speech_recognition as sr

# locate audio file
AUDIO_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), f"audio/transcription.wav")
audio_src = sr.AudioFile(AUDIO_FILE)

# create speech recognizer instance
rec = sr.Recognizer()

with audio_src as source:
    # record from file
    audio = rec.record(source)

    try:
        # transcribe using openai whisper and write to file
        out = open(f"Handwriting-Transformers/mytext.txt", "x")
        out.write(rec.recognize_whisper(audio))
    except FileExistsError:
        out = open(f"Handwriting-Transformers/mytext.txt", "w")
        out.write(rec.recognize_whisper(audio))