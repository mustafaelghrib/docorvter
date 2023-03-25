import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from rest_framework.request import Request
from .models import AuthUser


class JWTAuthentication(authentication.BaseAuthentication):
    """Custom JWT Authentication Class."""

    def authenticate(self, request: Request) -> (AuthUser, None):
        """Authenticate user based on JWT token in request header.

        Args:
            request: The HTTP request object.

        Raises:
            AuthenticationFailed: If the JWT token is invalid or not present in the request header.

        Returns:
            A tuple of (user, None) if authentication succeeds, or None if it fails.
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
    """Generates a JSON Web Token (JWT) using the provided email and key.

    Args:
        email: The email address to include in the token's payload.
        key: The key to use for encoding the token.

    Returns:
        A string representation of the generated token.
    """

    token = jwt.encode(
        payload={"email": email},
        key=key,
        algorithm="HS256"
    )
    return token


def verify_token(token: str, key: str) -> dict:
    """Verifies a JSON Web Token (JWT) using the provided key.

    Args:
        token: The JWT to verify.
        key: The key to use for verifying the JWT.

    Raises:
        jwt.InvalidTokenError: If the token cannot be verified or decoded.

    Returns:
        A dictionary representation of the decoded payload.
    """
    payload = jwt.decode(
        jwt=token,
        key=key,
        algorithms=["HS256"]
    )
    return payload
