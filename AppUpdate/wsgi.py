"""
WSGI config for AppUpdate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppUpdate.settings")
#
# application = get_wsgi_application()

import os
import django.conf
from django.core.handlers.wsgi import WSGIHandler

django.conf.ENVIRONMENT_VARIABLE = 'DJANGO_APPUPDATE_SETTINGS_MODULE'

os.environ.setdefault("DJANGO_APPUPDATE_SETTINGS_MODULE", "AppUpdate.settings")

application = WSGIHandler()
