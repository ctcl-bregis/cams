# CAMS - CTCL 2017-2023
# Date: June 6, 2023 - July 6, 2023
# Purpose: WSGI config

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cams.settings')
application = get_wsgi_application()
