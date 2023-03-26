"""
This module defines the urls of the converter views.

Variables:
    - urlpatterns: A list of url patterns of converter views.
"""


from django.urls import path

from .views import *

urlpatterns = [
    path('html/convert', HtmlConvertAPI.as_view()),
]
