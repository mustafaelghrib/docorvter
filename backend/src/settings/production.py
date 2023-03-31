from .development import *

DEBUG = config("DJANGO_DEBUG", default=False)

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_BUCKET_DOMAIN_NAME = config('AWS_BUCKET_DOMAIN_NAME')

STATIC_URL = f'https://{AWS_BUCKET_DOMAIN_NAME}/static/'
STATICFILES_STORAGE = 'src.storage.StaticStorage'

MEDIA_URL = f'https://{AWS_BUCKET_DOMAIN_NAME}/media/'
DEFAULT_FILE_STORAGE = 'src.storage.MediaStorage'
