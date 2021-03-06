"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lambda-valley.settings')

application = get_wsgi_application()
