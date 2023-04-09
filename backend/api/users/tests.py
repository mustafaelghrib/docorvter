import pytest
from rest_framework import status
from rest_framework.test import APIRequestFactory

from .views import UserRegisterAPI, UserLoginAPI


@pytest.fixture
def api_factory():
    return APIRequestFactory()


@pytest.mark.django_db
def test_user_register_api(api_factory):
    url = "/api/register/"
    data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123",
    }

    request = api_factory.post(url, data, format="json")
    view = UserRegisterAPI.as_view()
    response = view(request)

    assert response.status_code == status.HTTP_200_OK
    assert "user" in response.data
    assert response.data["user"]["username"] == data["username"]
    assert response.data["user"]["email"] == data["email"]


@pytest.mark.django_db
def test_user_register_api_invalid_data(api_factory):
    url = "/api/register/"
    data = {
        "username": "",
        "email": "invalidemail",
        "password": "password",
    }

    request = api_factory.post(url, data, format="json")
    view = UserRegisterAPI.as_view()
    response = view(request)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "email_error" in response.data
    assert "username_error" in response.data
    assert "password_error" in response.data


@pytest.mark.django_db
def test_user_login_api(api_factory, auth_user):
    url = "/api/login/"
    data = {
        "email": auth_user.email,
        "password": "password",
    }

    request = api_factory.post(url, data, format="json")
    view = UserLoginAPI.as_view()
    response = view(request)

    assert response.status_code == status.HTTP_200_OK
    assert "token" in response.data
    assert response.data["token"] == auth_user.token


@pytest.mark.django_db
def test_user_login_api_invalid_data(api_factory, auth_user):
    url = "/api/login/"
    data = {
        "email": "",
        "password": "",
    }

    request = api_factory.post(url, data, format="json")
    view = UserLoginAPI.as_view()
    response = view(request)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "email_error" in response.data
    assert "password_error" in response.data


@pytest.mark.django_db
def test_user_login_api_user_not_found(api_factory):
    url = "/api/login/"
    data = {
        "email": "invalid@example.com",
        "password": "password",
    }

    request = api_factory.post(url, data, format="json")
    view = UserLoginAPI.as_view()
    response = view(request)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "email_error" in response.data


@pytest.mark.django_db
def test_user_login_api_invalid_password(api_factory, auth_user):
    url = "/api/login/"
    data = {
        "email": auth_user.email,
        "password": "invalidpassword",
    }

    request = api_factory.post(url, data, format="json")
    view = UserLoginAPI.as_view()
    response = view(request)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "password_error" in response.data
