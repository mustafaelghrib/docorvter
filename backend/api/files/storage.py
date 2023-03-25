import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):
    """
    Overrides the default storage system to allow overwriting of existing files.

    This class inherits from Django's FileSystemStorage class and overrides the `get_available_name`
    method to check if a file with the same name already exists. If so, it deletes the old file before
    returning the name, allowing the new file to overwrite the old one.
    """

    def get_available_name(self, name, max_length=None):
        """
        Returns a filename that's available for new content to be written to.

        If the file already exists, it is deleted to allow overwriting.

        Parameters:
            name (str): The desired filename.
            max_length (int, optional): The maximum length of the filename. Defaults to None.

        Returns:
            str: The new filename that's available for use.
        """
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name
