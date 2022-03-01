from fastapi import FastAPI, UploadFile,  Request
from utils.document_extractor.file_conversion.format_conversion_manager import FormatConversionManager
from utils import utils

app = FastAPI()


@app.get("/")
def index():
    return {'path': ''}


@app.post("/ImageExtraction")
def upload_file(file: UploadFile):
    """
    :type file: Image, docx, PDF
    """
    # Creating temp file
    doc_path = utils.save_upload_file_tmp(file)

    fcm = FormatConversionManager()

    # Get image path/list
    img_list = fcm(doc_path)
    # print(img_list)

    return {"file": {"File Name": file.filename, "File Type": file.content_type}}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
