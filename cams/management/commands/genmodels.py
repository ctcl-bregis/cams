# CAMS - CTCL 2017-2023
# Date: July 6, 2023 - July 6, 2023 
# Purpose: Management command for generating database models, form data and other files

# Valid data types
# - date: datetime.date object, editable via Django DateField form class
# - select: Value chosen by a dropdown menu
# - string: Text input with a text length limit
# - text: Text input that is displayed using a textarea

from django.core.management.base import BaseCommand, CommandError
import os, json, shutil
from datetime import datetime, timezone
from csscompressor import compress

