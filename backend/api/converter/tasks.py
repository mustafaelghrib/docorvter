import os
import shutil
from datetime import datetime

from celery import shared_task
from django.conf import settings

from .document_converter.converter.html_converter import HtmlConverter
from ..files.models import File


@shared_task
def convert_html_file(file_id: str) -> None:
    """
    Converts an HTML file to PDF asynchronously using the HtmlConverter class.

    Args:
    file_id (UUID): The ID of the File object to be converted.

    Returns:
    None.
    """

    file = File.objects.get(file_id=file_id)

    output_file = f"{settings.MEDIA_ROOT}/out.pdf"

    html_converter = HtmlConverter()
    html_converter.convert(file=file.html_file.path, output=output_file)

    file.converted_at = datetime.now()

    HTML_FILES_DIR = f'{settings.MEDIA_ROOT}/html_files'
    PDF_FILES_DIR = f'{settings.MEDIA_ROOT}/pdf_files'

    new_html_file = f'{HTML_FILES_DIR}/{file.file_id}.html'
    os.rename(file.html_file.path, new_html_file)
    file.html_file = new_html_file

    if not os.path.exists(PDF_FILES_DIR):
        os.makedirs(PDF_FILES_DIR)

    new_output_file = f"{PDF_FILES_DIR}/{file.file_id}.pdf"
    shutil.copy(output_file, new_output_file)
    file.pdf_file = new_output_file

    file.save()

    os.remove(output_file)
