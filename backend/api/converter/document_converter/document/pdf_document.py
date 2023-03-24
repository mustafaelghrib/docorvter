import pdfkit

from .document import Document


class PdfDocument(Document):

    def __init__(self, file, output):
        super().__init__(file, output)

    def convert_file(self):
        options = {'encoding': 'UTF-8'}
        pdfkit.from_file(self._file, self._output, options=options)
