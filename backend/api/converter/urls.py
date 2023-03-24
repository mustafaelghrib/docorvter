from django.urls import path

from .views import *

urlpatterns = [
    path('html/convert', HtmlConvertAPI.as_view()),
]
