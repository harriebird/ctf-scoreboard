"""
WSGI config for scoreboard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.path.exists('local_settings.py'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'local_settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scoreboard.settings')

application = get_wsgi_application()
