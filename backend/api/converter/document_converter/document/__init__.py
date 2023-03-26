"""
This package contains classes of documents produced by the converter.

Modules:
    - [`document`][backend.api.converter.document_converter.document.document]:
    A module that contains the document interface.
    - [`pdf_document`][backend.api.converter.document_converter.document.pdf_document]:
    A module that contain the PDF document.
"""

from .document import Document
from .pdf_document import PdfDocument
