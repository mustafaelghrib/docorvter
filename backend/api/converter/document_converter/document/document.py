from abc import ABC, abstractmethod


class Document(ABC):
    """Abstract base class for document conversion."""

    def __init__(self, file, output):
        """Initialize the Document object.

        Args:
            file (str): A string representing the path of the file to be converted.
            output (str): A string representing the path of output file.
        """
        self._file = file
        self._output = output

    @abstractmethod
    def convert_file(self):
        """Abstract method that converts the file to the desired output format."""
        pass
