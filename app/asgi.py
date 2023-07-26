# CAMS Asset Management System - CTCL 2017-2023
# File: asgi.py
# Purpose: ASGI config for Django
# Created: June 6, 2023
# Modified: July 25, 2023

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_asgi_application()
