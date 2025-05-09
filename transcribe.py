import os
import speech_recognition as sr

class Transcriber:
    def __init__(self, in_path, out_path):
        audio_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), in_path)
        self.AUDIO_SRC = sr.AudioFile(audio_file)
        self.REC = sr.Recognizer()
        self.OUT_PATH = out_path

    def transcribe(self):
        with self.AUDIO_SRC as source:
            # record from file
            audio = self.REC.record(source)

            try:
                # transcribe using openai whisper and write to file
                out = open(self.OUT_PATH, "x")
                out.write(self.REC.recognize_whisper(audio))
            except FileExistsError:
                out = open(self.OUT_PATH, "w")
                out.write(self.REC.recognize_whisper(audio))