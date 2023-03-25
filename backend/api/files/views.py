from rest_framework import views, status
from rest_framework.response import Response

from .models import File
from .serializers import FileSerializer
from ..users.jwt_auth import JWTAuthentication


class FilesAPI(views.APIView):

    authentication_classes = [JWTAuthentication]

    @staticmethod
    def get_files_list(request):

        files = File.objects.all()

        return Response({
            "status": status.HTTP_200_OK,
            "message": "Files fetched successfully",
            "file": FileSerializer(files, many=True, context={"request": request}).data,
        })

    @staticmethod
    def delete_all_files():

        File.objects.all().delete()

        return Response({
            "status": status.HTTP_200_OK,
            "message": "All files deleted successfully",
        })

    def get(self, request):
        if not request.user:
            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Access denied!",
            })
        return self.get_files_list(request)

    def delete(self, request):
        if not request.user:
            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Access denied!",
            })
        return self.delete_all_files()


class FileAPI(views.APIView):

    authentication_classes = [JWTAuthentication]

    @staticmethod
    def get_file(request, file_id):

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
        if not request.user:
            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Access denied!",
            })
        return self.get_file(request, file_id)

    def delete(self, request, file_id):
        if not request.user:
            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Access denied!",
            })
        return self.delete_file(request, file_id)
