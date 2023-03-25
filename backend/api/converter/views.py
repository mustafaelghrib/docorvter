from datetime import datetime

from rest_framework import views, status
from rest_framework.response import Response

from .tasks import convert_html_file
from ..files.models import File
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

        convert_html_file.delay(file.file_id)

        return Response({
            "status": status.HTTP_200_OK,
            "message": "We are converting your file! Wait a moment!",
        })

    def post(self, request):
        if not request.user:
            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Access denied!",
            })
        return self.convert_html_file(request)
