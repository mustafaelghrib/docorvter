"""
A module that contains the converter views.

Classes:
    - `HtmlConvertAPI`: A class that hold the endpoint of converting html files.
"""

from datetime import datetime

from rest_framework.request import Request
from rest_framework import views, status
from rest_framework.response import Response

from .tasks import convert_html_file
from ..files.models import File
from ..users.jwt_auth import JWTAuthentication


class HtmlConvertAPI(views.APIView):
    """API View for converting an HTML file to PDF asynchronously.

    This class handles POST requests to convert an HTML file to a PDF file
    using Celery worker to process the conversion task asynchronously.

    Attributes:
        `authentication_classes`: List of authentication classes. Default is JWTAuthentication.

    Methods:
        - `post(request)`: Handles POST requests and performs the HTML to PDF conversion.
    """

    authentication_classes = [JWTAuthentication]

    def post(self, request: Request) -> Response:
        """Perform HTML to PDF conversion and return a response.

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

        if 'html_file' not in request.data:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "You should provide an html file to convert!",
            })

        html_file = request.data.get('html_file')
        file = File.objects.create(
            html_file=html_file,
            uploaded_at=datetime.now(),
            user=request.user
        )

        convert_html_file.delay(file.file_id)

        return Response({
            "status": status.HTTP_200_OK,
            "message": "We are converting your file! Wait a moment!",
        })

