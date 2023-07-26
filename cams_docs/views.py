# CAMS Asset Management System - CTCL 2017-2023
# File: views.py
# Purpose: Integrated Documentation Views
# Created: July 5, 2023
# Modified: July 26, 2023

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader
from django.template.defaulttags import register
from django.db.models import CharField, TextField, Q
from datetime import datetime
from cams.lib import printe, hsize
import csv, io, os


def listfiles(relpath):
    files = os.listdir(relpath)

    return data

docs_root = "docs"

# {{ dict|get_item:key }}
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# "root" page
def docs(request, path = "/"):
    if os.path.isdir(path):
        dirinfo = listfiles(path)

    elif os.path.isfile(path):
        pass

    return HttpResponseNotFound()