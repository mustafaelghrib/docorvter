"""
This module defines the urls of the files views.

Variables:
    - urlpatterns: A list of url patterns of files views.
"""

from django.urls import path

from .views import *

urlpatterns = [
    path('files', FileListAPI.as_view()),
    path('files/<str:file_id>', FileDetailAPI.as_view()),
]
