from abc import ABC, abstractmethod

from ..document.document import Document


class Converter(ABC):
    """Abstract class for a document converter."""

    def convert(self, file: str, output: str) -> Document:
        """
        Converts a file to a desired format.

        Args:
            file (str): The path to the file to be converted.
            output (str): The desired output format.

        Returns:
            A document object.
        """
        document: Document = self._create_document(file, output)
        document.convert_file()
        return document

    @abstractmethod
    def _create_document(self, file: str, output: str) -> Document:
        """
        Creates a document object given a file and output path.

        Args:
            file (str): The path to the file to be converted.
            output (str): The desired path of the converted file.

        Returns:
            A document object.
        """
        pass
