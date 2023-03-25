import os
from decouple import config

from django.http import HttpResponse


def index_view(request):
    return HttpResponse(f"<h1>Welcome {config('DJANGO_SETTINGS_MODULE')}</h1>")
