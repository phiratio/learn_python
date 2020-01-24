"""
WSGI config for todo_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
"""

import os

from django.core.wsgi import get_wsgi_application
# from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo_app.settings")

application = get_wsgi_application()
# application = WhiteNoise(application)
