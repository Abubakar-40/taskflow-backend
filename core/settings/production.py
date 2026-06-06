from .base import *

DEBUG = False

ALLOWED_HOSTS = [os.getenv('AZURE_APP_URL')]

CORS_ALLOWED_ORIGINS = [
    os.getenv('FRONTEND_URL'),
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')