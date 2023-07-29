# CAMS Asset Management System - CTCL 2017-2023
# File: views.py
# Purpose: Integrated Documentation Views
# Created: July 5, 2023
# Modified: July 29, 2023

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader
from django.template.defaulttags import register
from django.db.models import CharField, TextField, Q
from datetime import datetime, timezone
from cams.lib import printe, hsize, getconfig, mkcontext
import csv, io, os, markdown

basepath = "config/"
urlprefix = "/docs/"

docsconfig = getconfig("docs")
relpath = docsconfig["path"]

strfstr = getconfig("misc")["strftime"]

# {{ dict|get_item:key }}
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def getfiledata(path):
    # In case there is a Windows-style path
    file = path.replace('\\', '/')
    file = os.path.basename(file)
    
    filedata = {}
    filedata["name"] = file
    mtime = datetime.fromtimestamp(os.path.getmtime(path), timezone.utc)

    if os.path.isdir(path):
        filedata["link"] = f"/{path}"
        filedata["size"] = ""
        # "dtype" is what is shown to the user under "Type", not what is used to determine how to render a file
        filedata["dtype"] = "Directory"
        filedata["modt"] = mtime.strftime(strfstr)
        filedata["type"] = "directory"

        return filedata
    elif os.path.isfile(path):
        extension = os.path.splitext(path)[1]
        if extension in docsconfig["knowntypes"].keys():
            filedata["dtype"] = docsconfig["knowntypes"][extension]["name"]
            print(docsconfig["knowntypes"][extension]["type"])
            if docsconfig["knowntypes"][extension]["type"] in ["markdown", "source", "text", "source", ""]:
                filedata["link"] = f"/{path}"
                filedata["type"] = docsconfig["knowntypes"][extension]["type"]
            else:
                filedata["type"] = None
                filedata["link"] = None
                
        else:
            # When unknown, have the type as "EXTENSION file", similar to how Windows Explorer handles unknown file types
            extension = extension.upper()
            filedata["dtype"] = f"{extension} file"
            # Assume the file is not plain text
            filedata["type"] = "binary"
            filedata["link"] = None

        filedata["size"] = hsize(os.path.getsize(path))
        filedata["modt"] = mtime.strftime(strfstr)

        return filedata
    else:
        # In case the file is not a file or directory
        return None
    
def listfiles(path):
    files = os.listdir(path)
    data = []
    for file in files:
        # Files starting with "." are hidden on UNIX-like platforms
        if file.startswith(".") and docsconfig["showhidden"] == "False":
            continue

        filedata = getfiledata(file)

        if filedata != None:
            data.append(filedata)

    return data

# "root" page
def docs(request, path = ""):
    context = mkcontext(request, "Documentation")
    context["dir"] = path
    context["headers"] = docsconfig["table"]

    path = relpath + path
    if os.path.isdir(path):
        context["data"] = listfiles(path)

        return render(request, "docs_dir.html", context = context)
    elif os.path.isfile(path):
        # Make sure the file was given a link
        if getfiledata(path)["link"] == None:
            return HttpResponseNotFound()

        context = mkcontext(request, f"Documentation - {path}")
        filetype = getfiledata(path)["type"]

        if filetype == "markdown":
            with open(path) as f:
                context["content"] = markdown.markdown(f.read())
        elif filetype == "text":
            with open(path) as f:
                content = f.read()
                context["content"] = f"<p>\n{content}\n</p>"
        elif filetype == "source":
            with open(path) as f:
                content = f.read()
                context["content"] = f"<code>\n{content}\n</code>"

        return render(request, "docs_page.html", context = context)

    
    return HttpResponseNotFound()
