from flask import Flask, request
import requests
import os
from data_transfer import FileTransferer
from audiofilter import AudioFilterer

app = Flask(__name__)
ft = FileTransferer(save_dir="server_files")

@app.route("/upload", methods=["POST"])
def send_letter():
    ft.get_files(['audio'], True)

    for f in os.listdir("server_files"):
        if f.startswith("audio_file."):
            audio_path = os.path.join("server_files", f)
            break
    else:
        return "Audio file not found!", 400

    # code for generating the filtered audio here
    af = AudioFilterer(audio_path)
    af.filter_audio()

    # send the letter, filtered audio, and original audio
    # REMEMBER TO CHANGE THE IP ADDRESS T_T
    ft.send_files("http://127.0.0.1:5001/receive", {
        'letter': "./static/ageofstars.jpg",
        'filtered_audio': "server_files/filtered.wav",
        'original': audio_path
    })

    return "Processed and Sent Over!"

app.run(host="0.0.0.0", port=5000)