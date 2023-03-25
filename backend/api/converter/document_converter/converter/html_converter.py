from .converter import Converter
from ..document.pdf_document import PdfDocument


class HtmlConverter(Converter):
    """
    A concrete class inheriting from Converter. This class is used to convert HTML files to PDF files.
    """

    def _create_document(self, file, output):
        """
        Abstract method implemented by HtmlConverter. Creates a PdfDocument object with input HTML file
        and output PDF file.

        Args:
            file (str): The path to the HTML file to be converted.
            output (str): The path where the output PDF file should be saved.

        Returns:
            PdfDocument: A PdfDocument object with input HTML file and output PDF file.
        """

        return PdfDocument(file, output)
