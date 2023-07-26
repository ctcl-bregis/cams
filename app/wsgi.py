# CAMS Asset Management System - CTCL 2017-2023
# File: wsgi.py
# Purpose: WSGI config for Django
# Created: June 6, 2023
# Modified: July 25, 2023

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
application = get_wsgi_application()
