from os.path import splitext
from pdf2image import convert_from_bytes, pdfinfo_from_bytes


class PDF2ImageConverter(object):

    def __init__(self, max_images_per_pdf=10, dpi=400, fmt='jpeg', thread_count=4, transparent=False,
                 single_file=False, grayscale=False, use_pdf2cairo=True):
        self.tmpdir = "/tmp/dadocex"
        self.max_images_per_pdf = max_images_per_pdf
        self.dpi = dpi
        self.fmt = fmt
        self.thread_count = thread_count
        self.transparent = transparent
        self.single_file = single_file
        self.grayscale = grayscale
        self.use_pdf2cairo = use_pdf2cairo

    def read_file_bytes(self, file_path: str):
        pdf_file = open(file_path, 'rb').read()
        return pdf_file

    def validate_pdf_extension(self, path) -> bool:
        return str.endswith(splitext(path)[-1], ".pdf")

    def __call__(self, file):
        if type(file) == str:
            if self.validate_pdf_extension(file):
                file = self.read_file_bytes(file_path=file)
            else:
                raise Exception("File is not a PDF according to the extension, at least.")
        information = pdfinfo_from_bytes(file)
        pages = information["Pages"]
        last_page = self.max_images_per_pdf if pages > self.max_images_per_pdf else pages

        images = convert_from_bytes(file, output_folder=self.tmpdir, dpi=self.dpi, fmt=self.fmt,
                                    thread_count=self.thread_count, transparent=self.transparent,
                                    single_file=self.single_file, grayscale=self.grayscale,
                                    use_pdftocairo=self.use_pdf2cairo, last_page=last_page)
        if len(images) > self.max_images_per_pdf:
            images = images[:self.max_images_per_pdf]
        return images


if __name__ == '__main__':
    from PIL import Image
    converter = PDF2ImageConverter()

    images = converter("Enter Location Here")
    print(len(images))