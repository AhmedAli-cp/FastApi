from os.path import abspath, exists, isdir, isfile
from mimetypes import guess_type

from utils.document_extractor.file_conversion.converters import ImageConverter, PDFConverter, DocConverter


class FormatConversionManager(object):

    def __init__(self):
        self.pdf_converter = PDFConverter()
        self.doc_converter = DocConverter()
        self.img_converter = ImageConverter()

        self.mimetyes = {
            "pdf": ["application/pdf"],
            "images": ["image"],
            "docs": ["application/msword", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]
        }

    def select_type(self, path: str):
        result = guess_type(path)[0]
        print(result)
        if any([val in result for val in self.mimetyes["pdf"]]):
            return self.pdf_converter(path)
        elif any([val in result for val in self.mimetyes["images"]]):
            return self.img_converter(path)
        elif any([val in result for val in self.mimetyes["docs"]]):
            return self.doc_converter(path)
        else:
            raise Exception(f"File is of type {result} which is not included in the predefined appropriate file types.")

    def validate_file(self, path: str):
        if not exists(path):
            raise Exception(f"File {path} does not exist")

        path = abspath(path)
        if isdir(path):
            raise Exception(f"File being processed is a directory?: {path}")
        if not isfile(path):
            raise Exception(f"File is not a directory and not a file??: {path}")
        return path

    def __call__(self, path: str):
        path = self.validate_file(path)
        return self.select_type(path)


if __name__ == '__main__':
    converter = FormatConversionManager()
    print(converter("Enter Location Here"))
