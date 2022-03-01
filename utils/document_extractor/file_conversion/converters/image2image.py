from os.path import join, abspath, dirname, basename
import cv2
from mimetypes import guess_type


class Image2ImageConverter(object):

    def __init__(self):
        self.tmpdir = "/tmp/dadocex"
        self.optimal_formats = ["png", "jpeg"]
        self.not_supported_formats = ["gif"]

    def validate_path_type(self, file_path: str):
        result = guess_type(abspath(file_path))
        return "image" in result[0] and all([val not in result[0] for val in self.not_supported_formats])

    def __call__(self, file):
        if type(file) is str:
            if not self.validate_path_type(file):
                raise Exception("File is not an Image Media Type? Why??")
        for fmt in self.optimal_formats:
            if str.endswith(file, fmt):
                return file
        new_path = join(self.tmpdir, f"{basename(file).split('.')[0]}.{self.optimal_formats[0]}")
        cv2.imwrite(new_path,
                    cv2.imread(abspath(file)))
        return new_path


if __name__ == '__main__':
    converter = Image2ImageConverter()
    name = converter("Enter Location Here")
    print(name)