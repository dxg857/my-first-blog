"""
WSGI config for FirstSite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

current_path = os.path.abspath('.')
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FirstSite.settings')

application = get_wsgi_application()
