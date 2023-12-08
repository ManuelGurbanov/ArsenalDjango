# +++++++++++ DJANGO +++++++++++
import os
import sys

# le indicamos el path del project
path = '/home/montagut1/ArsenalDjango/arsenal'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application
# le indicamos el lugar de los settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arsenal.settings')
application = get_wsgi_application()