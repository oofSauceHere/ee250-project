from audiofilter import AudioFilterer
from transcribe import Transcriber
import os
import cv2
import numpy as np

class HandwritingGenerator:
    def __init__(self, audio_path):
        self.AF = AudioFilterer(audio_path)
        self.TS = Transcriber("server_files/filtered.wav", "Handwriting-Transformers/mytext.txt")
    
    def filter(self):
        self.AF.filter_audio()

    def transcribe(self):
        self.TS.transcribe()
    
    def generate_handwriting(self):
        os.system("python Handwriting-Transformers/hwt.py")

    def crop(self):
        # read image
        img = cv2.imread("Handwriting-Transformers/results/image0.png")
        height, width, _ = img.shape

        # crop image
        cropped = img[0:height//8, 725:width]

        # write image
        cv2.imwrite("out/document.png", cropped)