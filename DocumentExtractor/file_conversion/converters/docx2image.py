from os.path import abspath, join, basename
from tempfile import TemporaryDirectory
import zipfile
import mimetypes


class Document2ImageConverter(object):

    def __init__(self):
        self.tmpdir = "/tmp/dadocex"
        self.min_image_size = 30 * 1024  # 30kB

    def __call__(self, filepath: str):
        archive = zipfile.ZipFile(filepath)
        images = []
        for file in archive.filelist:
            if file.filename.startswith('word/media/') and \
                file.file_size > self.min_image_size and \
                    "image" in mimetypes.guess_type(file.filename)[0]:
                print(basename(file.filename))
                images.append(archive.extract(file, path=self.tmpdir))
        return images


if __name__ == '__main__':
    converter = Document2ImageConverter()
    image_paths = converter("Enter Location Here")
    print(image_paths)