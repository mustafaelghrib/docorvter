from rest_framework import serializers

from .models import AuthUser


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = AuthUser
        fields = [
            "user_id",
            "email",
            "username",
            "password",
            "created_at",
            "updated_at",
        ]

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError("Password must be more than 8 characters!")
        return password
