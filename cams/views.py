# CAMS - CTCL 2017-2023
# Date: June 9, 2023 (Reused from ContactList) - July 4, 2023
# Purpose: Main application views

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.template.defaulttags import register
from django.db.models import CharField, TextField, Q
from datetime import datetime
from . import lib
from .lib import printe
import csv, io

# {{ dict|get_item:key }}
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
