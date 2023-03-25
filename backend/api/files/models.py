from uuid import uuid4

from django.db import models

from .storage import OverwriteStorage


class File(models.Model):
    """A model representing an uploaded file and its converted version."""

    class Meta:
        """Metaclass for File model."""
        db_table = "api_files"

    file_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, db_index=True)

    html_file = models.FileField(upload_to="html_files/", max_length=255, storage=OverwriteStorage(), null=True)
    pdf_file = models.FileField(upload_to="pdf_files/", max_length=255, storage=OverwriteStorage(), null=True)

    uploaded_at = models.DateTimeField(max_length=255, null=True)
    converted_at = models.DateTimeField(max_length=255, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
