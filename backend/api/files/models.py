"""
A module that contains models of the files package.

Classes:
    - `File`: A class that creating the file model.
"""

from uuid import uuid4

from django.db import models

from .storage import OverwriteStorage
from ..users.models import AuthUser


class File(models.Model):
    """A model representing an uploaded file and its converted version.

    Attributes:
        file_id: The id of the file
        html_file: The html file that uploaded for conversion
        pdf_file: The pdf file path that converted
        uploaded_at: The datetime when uploading the file
        converted_at: The datetime when converting the file
        created_at: The datetime when the file is created
        updated_at: The updated datatime when updating the file
        user: A foreign key to AuthUser model
    """

    class Meta:
        """Metaclass for File model.

        Attributes:
            db_table: the table name
        """

        db_table: str = "api_files"

    file_id: models.UUIDField = models.UUIDField(primary_key=True, default=uuid4, editable=False, db_index=True)

    html_file: models.FileField = models.FileField(upload_to="html_files/", max_length=255, storage=OverwriteStorage(), null=True)
    pdf_file: models.FileField = models.FileField(upload_to="pdf_files/", max_length=255, storage=OverwriteStorage(), null=True)

    uploaded_at: models.DateTimeField = models.DateTimeField(max_length=255, null=True)
    converted_at: models.DateTimeField = models.DateTimeField(max_length=255, null=True)

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True, null=True)

    user = models.ForeignKey(
        AuthUser,
        related_name='files',
        on_delete=models.CASCADE,
        null=True,
    )
