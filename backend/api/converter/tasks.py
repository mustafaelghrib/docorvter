"""
A module that contains all Celery tasks of the converter.

Functions:
    - `convert_html_file(file_id)`: A function that convert html file to pdf file asynchronously.
    - `rename_html_file(html_file, file_id)`: A function that rename the html file.
    - `rename_output_file(output_file, file_id)`: A function that rename the output file.
"""

import os
import shutil
from datetime import datetime

from celery import shared_task
from django.conf import settings

from .document_converter.converter.html_converter import HtmlConverter
from ..files.models import File


@shared_task
def convert_html_file(file_id: str) -> None:
    """Convert an HTML file to PDF asynchronously using the HtmlConverter class.

    Args:
        file_id: The ID of the File object to be converted.
    """
    file = File.objects.get(file_id=file_id)

    output_file = f"{settings.MEDIA_ROOT}/out.pdf"

    html_converter = HtmlConverter()
    html_converter.convert(file=file.html_file.path, output=output_file)

    file.converted_at = datetime.now()
    file.html_file = rename_html_file(file.html_file.path, file_id)
    file.pdf_file = rename_output_file(output_file, file_id)
    file.save()

    os.remove(output_file)


def rename_html_file(html_file: str, file_id: str) -> str:
    """Rename the html file.

    Args:
        html_file: the html file path
        file_id: the file id to renamed to

    Returns:
        The new renamed html file path
    """
    HTML_FILES_DIR = f'{settings.MEDIA_ROOT}/html_files'

    new_html_file = f'{HTML_FILES_DIR}/{file_id}.html'
    os.rename(html_file, new_html_file)

    return new_html_file


def rename_output_file(output_file: str, file_id: str) -> str:
    """Rename the output file.

    Args:
        output_file: the old output file path
        file_id: the file id to renamed to

    Returns:
        The new renamed output file path
    """
    PDF_FILES_DIR = f'{settings.MEDIA_ROOT}/pdf_files'

    if not os.path.exists(PDF_FILES_DIR):
        os.makedirs(PDF_FILES_DIR)

    new_output_file = f"{PDF_FILES_DIR}/{file_id}.pdf"
    shutil.copy(output_file, new_output_file)

    return new_output_file
