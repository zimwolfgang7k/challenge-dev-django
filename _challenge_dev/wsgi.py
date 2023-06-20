"""
WSGI config for _challenge_dev project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.auth.models import User

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_challenge_dev.settings")

application = get_wsgi_application()

# Criacao de usuario default para acesso do django admin

users = User.objects.all()
if not users:
    User.objects.create_superuser(
        username="username",
        email="user@example.com",
        password="admin1234",
        is_active=True,
        is_staff=True,
    )
