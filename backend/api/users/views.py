from rest_framework import views, status
from rest_framework.response import Response

from .models import AuthUser
from .serializers import UserSerializer


class UserRegisterAPI(views.APIView):
    """
    API View for user registration.

    This view handles the registration of new users by accepting a POST request with user details.

    """

    def post(self, request):
        """
        Handle POST requests for user registration.

        Args:
            request (rest_framework.request.Request): The HTTP request object.

        Returns:
            rest_framework.response.Response: The HTTP response object.

        """

        payload = request.data

        user_serializer = UserSerializer(data=payload)

        if user_serializer.is_valid():
            user = AuthUser(
                username=payload["username"],
                email=payload["email"],
            )
            user.set_password(payload["password"])
            user.set_token(payload["email"])
            user.save()

            return Response({
                "status": status.HTTP_200_OK,
                "message": "User registered successfully!",
                "user": UserSerializer(user).data
            })
        else:

            email_error = None
            username_error = None
            password_error = None

            if "email" in user_serializer.errors:
                email_error = user_serializer.errors["email"][0]
            if "username" in user_serializer.errors:
                username_error = user_serializer.errors["username"][0]
            if "password" in user_serializer.errors:
                password_error = user_serializer.errors["password"][0]

            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Please correct the errors",
                "email_error": email_error,
                "username_error": username_error,
                "password_error": password_error,
            })


class UserLoginAPI(views.APIView):
    """
    API view for user login.

    This view handles the login of users by accepting a POST request with user details.

    """

    def post(self, request):
        """
        Handles POST request for user login.

        Args:
            request (rest_framework.request.Request): The HTTP request object.

        Returns:
            rest_framework.response.Response: The HTTP response object.
        """

        payload = request.data

        if "email" not in payload or payload["email"] == "":
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Please correct the errors",
                "email_error": "Email is required",
            })

        if "password" not in payload or payload["password"] == "":
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Please correct the errors",
                "password_error": "Password is required",
            })

        user = AuthUser.objects.filter(email=payload["email"]).first()

        if not user:
            return Response({
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Please correct the errors",
                "email_error": "User with this email is not found!",
            })

        if not user.check_password(payload["password"]):
            return Response({
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Please correct the errors",
                "password_error": "Password is not correct!",
            })

        if user.token is None or user.token == "":
            user.set_token(user.email)
            user.save()

        return Response({
            "status": status.HTTP_200_OK,
            "message": "User logged successfully!",
            "token": user.token,
        })
