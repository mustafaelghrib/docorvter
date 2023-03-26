"""
This module contains class for the PDF document.

Classes:
    - `PdfDocument`: A class representing a PDF document.
"""

import pdfkit

from .document import Document


class PdfDocument(Document):
    """
    A class representing a PDF document.

    Methods:
        - `convert_file()`: A method for converting file.
    """

    def __init__(self, file: str, output: str) -> None:
        """Initialize the PdfDocument object.

        Args:
            file: A string representing the path of the file to be converted.
            output: A string representing the path of output file.
        """
        super().__init__(file, output)

    def convert_file(self) -> None:
        """Convert a html file to a PDF file using the pdfkit library."""
        options = {'encoding': 'UTF-8'}
        pdfkit.from_file(self._file, self._output, options=options)
