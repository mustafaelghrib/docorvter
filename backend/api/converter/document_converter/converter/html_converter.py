"""
This module contains class for the html converter.

Classes:
    - `HtmlConverter`: A class that convert html files.
"""


from .converter import Converter
from ..document.document import Document
from ..document.pdf_document import PdfDocument


class HtmlConverter(Converter):
    """
    A concrete class inheriting from Converter and used to convert HTML files to PDF files.

    Methods:
        - `_create_document()`: A protected method for creating documents.
    """

    def create_document(self, file: str, output: str) -> Document:
        """Create a PdfDocument object.

        Args:
            file: The path to the HTML file to be converted.
            output: The path where the output PDF file should be saved.

        Returns:
            A document object.
        """
        return PdfDocument(file, output)
