"""
This module contains class for the document.

Classes:
    - `Document`: An interface for the document object.
"""

from abc import ABC, abstractmethod


class Document(ABC):
    """
    Abstract base class for the document.

    Attributes:
        _file: The file source to be converted.
        _output: The output path of the converted file.

    Methods:
        - `convert_file()`: Abstract method for converting file.
    """

    def __init__(self, file: str, output: str) -> None:
        """Initialize the Document object.

        Args:
            file: A string representing the path of the file to be converted.
            output: A string representing the path of output file.
        """
        self._file: str = file
        self._output: str = output

    @abstractmethod
    def convert_file(self) -> None:
        """Abstract method that converts the file to the desired output format."""
        pass
