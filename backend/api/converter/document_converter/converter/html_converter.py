from .converter import Converter
from ..document.document import Document
from ..document.pdf_document import PdfDocument


class HtmlConverter(Converter):
    """A concrete class inheriting from Converter.

    This class is used to convert HTML files to PDF files.
    """

    def _create_document(self, file: str, output: str) -> Document:
        """Creates a PdfDocument object.

        Args:
            file: The path to the HTML file to be converted.
            output: The path where the output PDF file should be saved.

        Returns:
            A PdfDocument object with input HTML file and output PDF file.
        """

        return PdfDocument(file, output)
