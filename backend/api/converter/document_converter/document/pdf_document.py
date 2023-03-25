import pdfkit

from .document import Document


class PdfDocument(Document):
    """
    A class representing a PDF document that can be converted from a source file to an output file.
    """

    def __init__(self, file: str, output: str) -> None:
        super().__init__(file, output)

    def convert_file(self) -> None:
        """
        Converts the source file to a PDF document and saves it to the output file using the pdfkit library.
        """
        options = {'encoding': 'UTF-8'}
        pdfkit.from_file(self._file, self._output, options=options)
