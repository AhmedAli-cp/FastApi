from fastapi import UploadFile
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Callable


def save_upload_file_tmp(file: UploadFile) -> Path:
    try:
        suffix = Path(file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        file.file.close()
    return tmp_path


def handle_upload_file(
        upload_file: UploadFile, handler: Callable[[Path], str]
) -> str:
    tmp_path = save_upload_file_tmp(upload_file)
    img = ""
    try:
        img = handler(tmp_path)

    finally:
        tmp_path.unlink()  # Delete the temp file
        return img
