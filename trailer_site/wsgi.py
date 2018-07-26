"""
WSGI config for trailer_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

# import sys
# root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.insert(0, os.path.abspath(os.path.join(root_path, 'trailer_site')))
# sys.path.insert(0, root_path)
# sys.path.insert(0, '/var/www/trailer_site/venv/lib/python3.6/site-packages/')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trailer_site.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
