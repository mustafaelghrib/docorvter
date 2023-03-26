"""
This module contains class for the converter.

Classes:
    - `Converter`: An interface for the converter object.
"""

from abc import ABC, abstractmethod

from ..document.document import Document


class Converter(ABC):
    """
    Abstract class for the converter.

    Methods:
        - `convert()`: A method for converting documents.
        - `_create_document()`: A protected abstract method for creating documents.
    """

    def convert(self, file: str, output: str) -> Document:
        """Create a document and convert it.

        Args:
            file: The file to be converted.
            output: The output path of the converted file.

        Returns:
            A document object.
        """
        document: Document = self.create_document(file, output)
        document.convert_file()
        return document

    @abstractmethod
    def create_document(self, file: str, output: str) -> Document:
        """Create a document object given a file and output path.

        Args:
            file: The path to the file to be converted.
            output: The desired path of the converted file.

        Returns:
            A document object.
        """
        pass
