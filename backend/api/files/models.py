from uuid import uuid4

from django.db import models

from .storage import OverwriteStorage


class File(models.Model):
    class Meta:
        db_table = "api_files"

    file_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, db_index=True)

    html_file = models.FileField(upload_to="html_files/", storage=OverwriteStorage(), null=True)
    pdf_file = models.FileField(upload_to="pdf_files/", storage=OverwriteStorage(), null=True)

    uploaded_at = models.DateTimeField(null=True)
    converted_at = models.DateTimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
