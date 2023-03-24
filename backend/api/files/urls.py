from django.urls import path

from .views import *

urlpatterns = [
    path('files', FilesAPI.as_view()),
    path('files/<str:file_id>', FileAPI.as_view()),
]
