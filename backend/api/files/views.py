from rest_framework import views, status
from rest_framework.response import Response

from .models import File
from .serializers import FileSerializer
from ..users.jwt_auth import JWTAuthentication


class FilesAPI(views.APIView):
    """
    API endpoint for managing files.

    Attributes:
        authentication_classes (list):
            List of authentication classes used for authenticating requests.
    """

    authentication_classes = [JWTAuthentication]

    @staticmethod
    def get_files_list(request):
        """
        Retrieve a list of all files.

        Args:
            request (rest_framework.request.Request): HTTP request object.

        Returns:
            Response (rest_framework.response.Response): HTTP response containing a list of all files.
        """

        files = File.objects.all()

        return Response({
            "status": status.HTTP_200_OK,
            "message": "Files fetched successfully",
            "file": FileSerializer(files, many=True, context={"request": request}).data,
        })

    @staticmethod
    def delete_all_files():
        """
        Delete all files.

        Returns:
            Response (rest_framework.response.Response): HTTP response indicating success or failure of the operation.
        """

        File.objects.all().delete()

        return Response({
            "status": status.HTTP_200_OK,
            "message": "All files deleted successfully",
        })

    def get(self, request):
        """
        Handle GET requests to retrieve a list of all files.

        Args:
            request (rest_framework.request.Request): HTTP request object.

        Returns:
            Response (rest_framework.response.Response): HTTP response containing a list of all files.
        """

        if not request.user:
            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Access denied!",
            })
        return self.get_files_list(request)

    def delete(self, request):
        """
        Handle DELETE requests to delete all files.

        Args:
            request (rest_framework.request.Request): HTTP request object.

        Returns:
            Response (rest_framework.response.Response): HTTP response indicating success or failure of the operation.
        """

        if not request.user:
            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Access denied!",
            })
        return self.delete_all_files()


class FileAPI(views.APIView):
    """
    View for fetching and deleting individual files.
    """

    authentication_classes = [JWTAuthentication]

    @staticmethod
    def get_file(request, file_id):
        """
        Get the details of a file.

        Args:
            request (rest_framework.request.Request): The HTTP request object.
            file_id (UUID): The ID of the file to fetch.

        Returns:
            Response (rest_framework.response.Response): The response containing the file details.
        """

        file = File.objects.filter(file_id=file_id).first()

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

    @staticmethod
    def delete_file(request, file_id):
        """
        Delete a file.

        Args:
            request (rest_framework.request.Request): The HTTP request object.
            file_id (UUID): The ID of the file to delete.

        Returns:
            Response (rest_framework.response.Response): The response indicating whether the file was successfully deleted.
        """

        file = File.objects.filter(file_id=file_id).first()

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

    def get(self, request, file_id):
        """
        Handler for GET requests to fetch a file.

        Args:
            request (rest_framework.request.Request): The HTTP request object.
            file_id (UUID): The ID of the file to fetch.

        Returns:
            Response (rest_framework.response.Response): The response containing the file details.
        """

        if not request.user:
            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Access denied!",
            })
        return self.get_file(request, file_id)

    def delete(self, request, file_id):
        """
        Handler for DELETE requests to delete a file.

        Args:
            request (rest_framework.request.Request): The HTTP request object.
            file_id (UUID): The ID of the file to delete.

        Returns:
            Response (rest_framework.response.Response): The response indicating whether the file was successfully deleted.
        """

        if not request.user:
            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Access denied!",
            })
        return self.delete_file(request, file_id)
