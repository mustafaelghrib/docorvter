from abc import ABC, abstractmethod

from ..document.document import Document


class Converter(ABC):

    def convert(self, file, output):
        document: Document = self._create_document(file, output)
        document.convert_file()
        return document

    @abstractmethod
    def _create_document(self, file, output_path):
        pass
