import jwt
from django.conf import settings
from rest_framework import authentication, exceptions


class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
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


def generate_token(email, key):
    token = jwt.encode(
        payload={"email": email},
        key=key,
        algorithm="HS256"
    )
    return token


def verify_token(token, key):
    payload = jwt.decode(
        jwt=token,
        key=key,
        algorithms=["HS256"]
    )
    return payload
