from abc import ABC, abstractmethod


class Document(ABC):
    """Abstract base class for document conversion."""

    def __init__(self, file: str, output: str) -> None:
        """Initialize the Document object.

        Args:
            file (str): A string representing the path of the file to be converted.
            output (str): A string representing the path of output file.
        """
        self._file: str = file
        self._output: str = output

    @abstractmethod
    def convert_file(self) -> None:
        """Abstract method that converts the file to the desired output format."""
        pass
