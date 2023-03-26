"""
This package contains classes of the converters that convert documents.

Modules:
    - [`converter`][backend.api.converter.document_converter.converter.converter]:
    A module that contain converter interface.
    - [`html_converter`][backend.api.converter.document_converter.converter.html_converter]:
    A module that contain the HTML converter.
"""

from .converter import Converter
from .html_converter import HtmlConverter
