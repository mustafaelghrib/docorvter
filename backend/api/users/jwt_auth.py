import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from rest_framework.request import Request
from .models import AuthUser


class JWTAuthentication(authentication.BaseAuthentication):
    """
    JWT Authentication Class.

    This class implements JWT Authentication for Django REST Framework.

    """

    def authenticate(self, request: Request) -> (AuthUser, None):
        """
        Authenticate user based on JWT token in request header.

        Args:
            request (rest_framework.request.Request): The HTTP request object.

        Returns:
            Tuple[AuthUser, None]: A tuple of (user, None) if authentication succeeds, or None if it fails.

        Raises:
            AuthenticationFailed: If the JWT token is invalid or not present in the request header.

        """

        token = request.headers.get('Authorization')
        if token:
            try:
                payload = verify_token(token, settings.SECRET_KEY)
                from .models import AuthUser
                user = AuthUser.objects.filter(email=payload["email"]).first()
            except jwt.InvalidTokenError:
                raise exceptions.AuthenticationFailed('Invalid token')
        else:
            raise exceptions.AuthenticationFailed('Token required')

        return user, None


def generate_token(email: str, key: str) -> str:
    """
    Generates a JSON Web Token (JWT) using the provided email and key.

    Args:
        email (str): The email address to include in the token's payload.
        key (str): The key to use for encoding the token.

    Returns:
        str: A string representation of the generated token.

    """

    token = jwt.encode(
        payload={"email": email},
        key=key,
        algorithm="HS256"
    )
    return token


def verify_token(token: str, key: str) -> dict:
    """
    Verifies a JSON Web Token (JWT) using the provided key and returns the decoded payload as a dictionary.

    Args:
        token (str): The JWT to verify.
        key (str): The key to use for verifying the JWT.

    Returns:
        dict: A dictionary representation of the decoded payload.

    Raises:
        jwt.InvalidTokenError: If the token cannot be verified or decoded.

    """
    payload = jwt.decode(
        jwt=token,
        key=key,
        algorithms=["HS256"]
    )
    return payload
