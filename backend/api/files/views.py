"""
This module contains the views of the files package.

Classes:
    - `FilesAPI`: A class that handles the files endpoints
    - `FileAPI`: A class that handle the file details
"""

from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.authentication import BaseAuthentication

from .models import File
from .serializers import FileSerializer
from ..users.jwt_auth import JWTAuthentication


class FileListAPI(views.APIView):
    """API endpoint for managing files.

    Attributes:
        `authentication_classes`: List of authentication classes. Default is JWTAuthentication.

    Methods:
        - `get(request)`: Handles GET requests to get list of files.
        - `delete(request)`: Handles DELETE requests to delete all files.
    """

    authentication_classes = [JWTAuthentication]

    def get(self, request: Request) -> Response:
        """Retrieve a list of all files.

        Args:
            request: HTTP request object.

        Returns:
            HTTP response containing a list of all files.
        """
        if not request.user:
            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Access denied!",
            })

        files = request.user.files.all()

        return Response({
            "status": status.HTTP_200_OK,
            "message": "Files fetched successfully",
            "file": FileSerializer(files, many=True, context={"request": request}).data,
        })

    def delete(self, request: Request) -> Response:
        """Delete all files.

        Args:
            request: HTTP request object.

        Returns:
            HTTP response with message ans status code.
        """
        if not request.user:
            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Access denied!",
            })

        request.user.files.all().delete()

        return Response({
            "status": status.HTTP_200_OK,
            "message": "All files deleted successfully",
        })


class FileDetailAPI(views.APIView):
    """View for fetching and deleting individual files.

    Attributes:
        `authentication_classes`: List of authentication classes. Default is JWTAuthentication.

    Methods:
        - `get(request)`: Handles GET requests to get a file.
        - `delete(request)`: Handles DELETE requests to delete a file.
    """

    authentication_classes = [JWTAuthentication]

    def get(self, request: Request, file_id: str) -> Response:
        """Get the details of a file.

        Args:
            request: The HTTP request object.
            file_id: The ID of the file to fetch.

        Returns:
            The response containing the file details.
        """
        if not request.user:
            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Access denied!",
            })

        file = request.user.files.filter(file_id=file_id).first()

        if not file:
            return Response({
                "status": status.HTTP_404_NOT_FOUND,
                "message": "File not found",
            })

        return Response({
            "status": status.HTTP_200_OK,
            "message": "File fetched successfully",
            "file": FileSerializer(file, context={"request": request}).data,
        })

    def delete(self, request: Request, file_id: str) -> Response:
        """Delete a file.

        Args:
            request: HTTP request
            file_id: The ID of the file to delete.

        Returns:
            The response indicating whether the file was successfully deleted.
        """
        if not request.user:
            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Access denied!",
            })

        file = request.user.files.filter(file_id=file_id).first()

        if not file:
            return Response({
                "status": status.HTTP_404_NOT_FOUND,
                "message": "File not found",
            })

        file.delete()

        return Response({
            "status": status.HTTP_200_OK,
            "message": "File deleted successfully",
        })
