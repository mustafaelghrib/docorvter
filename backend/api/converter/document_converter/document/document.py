from abc import ABC, abstractmethod


class Document(ABC):

    def __init__(self, file, output):
        self._file = file
        self._output = output

    @abstractmethod
    def convert_file(self):
        pass
