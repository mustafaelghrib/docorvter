from datetime import datetime

from rest_framework import views, status
from rest_framework.response import Response

from .tasks import convert_html_file
from ..files.models import File
from ..users.jwt_auth import JWTAuthentication


class HtmlConvertAPI(views.APIView):
    """Converts an HTML file to PDF asynchronously and returns the file ID.

    This class handles POST requests to convert an HTML file to a PDF file
    using Celery worker to process the conversion task asynchronously.

    Attributes:
        authentication_classes: List of authentication classes. Default is JWTAuthentication.

    Methods:
        convert_html_file(request):
            Static method that performs the conversion and returns a response.
        post(request):
            Handles POST requests and returns the response.
    """

    authentication_classes = [JWTAuthentication]

    @staticmethod
    def convert_html_file(request):
        """Static method to perform HTML to PDF conversion and return a response.

        Args:
            request: HTTP request containing the HTML file to convert.

        Returns:
            Response with status code and message.
        """

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
        """Handles POST requests to convert HTML file to PDF and returns the response.

        Args:
            request: HTTP request containing the HTML file to convert.

        Returns:
            Response with status code and message.
        """
        if not request.user:
            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Access denied!",
            })
        return self.convert_html_file(request)
