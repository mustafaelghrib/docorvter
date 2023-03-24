from .converter import Converter
from ..document.pdf_document import PdfDocument


class HtmlConverter(Converter):

    def _create_document(self, file, output):
        return PdfDocument(file, output)
