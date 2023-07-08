# CAMS - CTCL 2017-2023
# Date: June 6, 2023 - July 6, 2023
# Purpose: ASGI config

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cams.settings')

application = get_asgi_application()