import os

from django.http import HttpResponse


def index_view(request):
    return HttpResponse(f"<h1>Welcome {os.environ.get('DJANGO_SETTINGS_MODULE')}</h1>")
