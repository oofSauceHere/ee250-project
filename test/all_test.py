from handwritinggenerator import HandwritingGenerator

HG = HandwritingGenerator("server_files/audio_file.mp3")
print("filtering...")
HG.filter()

print("transcribing...")
HG.transcribe()

print("generating handwriting...")
HG.generate_handwriting()

print("finalizing image...")
HG.crop()