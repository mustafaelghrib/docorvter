from django.urls import path

from .views import *

urlpatterns = [
    path('users/register', UserRegisterAPI.as_view()),
    path('users/login', UserLoginAPI.as_view()),
]
