import requests
import os
from flask import request
from contextlib import contextmanager

class FileTransferer:
    def __init__(self, save_dir_="static"):
        self.save_dir_ = save_dir_
        os.makedirs(save_dir_, exist_ok=True)

    def get_files(self, keys):
        for key in keys:
            if key in request.files:
                ext = request.files[key].filename.split('.')[-1]
                request.files[key].save(os.path.join(self.save_dir_, f"{key}.{ext}"))

    def send_files(self, url, files_):
        with self._open_files(files_) as files:
            results = requests.post(url, files=files)
        return results
    
@contextmanager
def _open_files(self, files_):
    handles = {k: open(p, "rb") for k, p in files_.items()}
    try:
        yield {k: v for k, v in handles.items()}
    finally:
        for h in handles.values():
            h.close()