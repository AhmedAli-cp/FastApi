from fastapi import UploadFile
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile


def save_upload_file_tmp(file: UploadFile) -> Path:
    try:
        suffix = Path(file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        file.file.close()
    return tmp_path
