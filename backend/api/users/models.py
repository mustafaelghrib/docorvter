from uuid import uuid4

from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.db import models

from .jwt_auth import generate_token


class AuthUser(models.Model):
    """
    Model for authenticated users.

    Attributes:
        user_id (UUIDField): Primary key for the user model.
        email (EmailField): Email of the user.
        username (CharField): Username of the user.
        password (CharField): Password of the user.
        token (CharField): Token generated for the user.
        created_at (DateTimeField): Date and time when the user model was created.
        updated_at (DateTimeField): Date and time when the user model was last updated.

    """

    class Meta:
        """
        Metaclass for AuthUser model.

        Attributes:
            db_table (str): Name of the database table for the AuthUser model.

        """
        db_table = "api_auth_users"

    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, db_index=True)

    email = models.EmailField(max_length=255, db_index=True, null=False, blank=False, unique=True)
    username = models.CharField(max_length=50, db_index=True, null=False, blank=False, unique=True)
    password = models.CharField(max_length=255, null=False, blank=False)
    token = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def set_password(self, raw_password):
        """
        Set password for the user.

        Args:
            raw_password (str): The raw password entered by the user.

        """
        self.password = make_password(raw_password)

    def check_password(self, new_password):
        """
        Check if the entered password is correct.

        Args:
            new_password (str): The new password entered by the user.

        Returns:
            bool: True if the password is correct, else False.

        """
        return check_password(new_password, self.password)

    def set_token(self, email):
        """
        Generate and set token for the user.

        Args:
            email (str): Email of the user.

        """
        self.token = generate_token(email, settings.SECRET_KEY)
