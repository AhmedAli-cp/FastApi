from fastapi import FastAPI, UploadFile, Request
from utils import utils
from utils.document_extractor.file_conversion.format_conversion_manager import FormatConversionManager

# import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {'path': ''}


@app.post("/ImageExtraction")
def upload_file(file: UploadFile):
    """
    :type file: Image, docx, PDF
    """

    # Handle Upload file
    img = utils.handle_upload_file(file, FormatConversionManager())

    #print(img)

    return {"file": {"File Name": file.filename, "File Type": file.content_type}}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
