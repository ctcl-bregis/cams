#!/usr/bin/env python
# CAMS - CTCL 2017-2023
# Date: June 5, 2023 - July 24, 2023
# Purpose: Django manage.py

import os, sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
