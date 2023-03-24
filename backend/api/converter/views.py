import os
import shutil
from datetime import datetime

from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response

from .document_converter.converter.html_converter import HtmlConverter
from ..files.models import File
from ..files.serializers import FileSerializer
from ..users.jwt_auth import JWTAuthentication


class HtmlConvertAPI(views.APIView):

    authentication_classes = [JWTAuthentication]

    @staticmethod
    def convert_html_file(request):

        if 'html_file' not in request.data:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "You should provide an html file to convert!",
            })

        html_file = request.data.get('html_file')

        file = File.objects.create(html_file=html_file, uploaded_at=datetime.now())

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

        return Response({
            "status": status.HTTP_200_OK,
            "message": "File converted successfully",
            "file": FileSerializer(file, context={"request": request}).data,
        })

    def post(self, request):
        if not request.user:
            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Access denied!",
            })
        return self.convert_html_file(request)
