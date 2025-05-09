import requests
import os
from flask import request
from contextlib import contextmanager

class FileTransferer:
    def __init__(self, save_dir="static"):
        self.save_dir_ = save_dir
        os.makedirs(save_dir, exist_ok=True)
        print("saving to dir",self.save_dir_)

    def get_files(self, keys, get_recording=False):
        for key in keys:
            if key in request.files:
                file_extension = request.files[key].filename.split('.')[-1]
                if get_recording:
                    request.files[key].save(os.path.join(self.save_dir_, f"audio_file.{file_extension}"))
                else:
                    request.files[key].save(os.path.join(self.save_dir_, f"{key}.{file_extension}"))

    def send_files(self, url, file_dict):
        with self._open_files(file_dict) as files:
            results = requests.post(url, files=files)
        return results
    
    @contextmanager
    # opens the files to be sent so that they can be accessed and sent (then close the files after-- yield )
    def _open_files(self, file_dict):
        # iterate through the files from the file_dict, open them in binary read mode, and store the open file handles in the handles dict
        # creates a new dictionary "handles", the keys are the sames but the values are changed to the file handles for the files in the file_dict
        handles = {k: open(p, "rb") for k, p in file_dict.items()}
        try:
            yield {k: v for k, v in handles.items()}
        finally:
            for h in handles.values():
                h.close()