from flask import Flask, render_template, request
import os
from data_transfer import FileTransferer

app = Flask(__name__)
ft = FileTransferer(save_dir="static")

@app.route("/")
def index():
    return render_template("visualiser.html")

@app.route("/receive", methods=["POST"])
def receive():
    ft.get_files(['original', 'filtered_audio', 'letter'])
    return "Files Received!"

@app.route("/status")
def status():
    ready = all(os.path.exists(f"static/{f}.wav") for f in ['original', 'filtered']) and os.path.exists("static/image.png")
    return {"ready": ready}

app.run(host="0.0.0.0", port=5001)