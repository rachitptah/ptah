import os
import sys

PROJECT_PATH = '/var/www/site/ptah'
PROJECT_PATH_MAIN = '/var/www/site/ptah/ptah/settings'

sys.path.insert(0, PROJECT_PATH)
sys.path.append(PROJECT_PATH_MAIN)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ptah.settings")

application = get_wsgi_application()
