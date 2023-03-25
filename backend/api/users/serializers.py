from rest_framework import serializers

from .models import AuthUser


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the AuthUser model.

    Attributes:
        password: Password of the user. Write-only field.

    """

    password = serializers.CharField(write_only=True)

    class Meta:
        """
        Metaclass for UserSerializer.

        Attributes:
            model: Model used for the serializer.
            fields: List of fields to be serialized.

        """
        model = AuthUser
        fields = [
            "user_id",
            "email",
            "username",
            "password",
            "created_at",
            "updated_at",
        ]

    def validate_password(self, password: str) -> str:
        """
        Validate the entered password.

        Args:
            password: The password entered by the user.

        Raises:
            serializers.ValidationError: If the password is less than 8 characters.

        Returns:
            The validated password.

        """
        if len(password) < 8:
            raise serializers.ValidationError("Password must be more than 8 characters!")
        return password
