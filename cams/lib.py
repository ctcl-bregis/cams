# CAMS - CTCL 2017-2023
# Date: May 4, 2023 - July 7, 2023
# Purpose: Commonly used functions, similar to lib.rs in Rust

from datetime import datetime, timezone
import json, base64, pathlib
from os import listdir, walk
from os.path import isdir, join, exists, getsize
from . import __version__

# printe statement that does not raise an exception if the code is running headless
def printe(text):
    try:
        print(text)
    except OSError:
        pass

# Load the config on startup instead of every time a function needs it
try:
    with open("config/config.json") as f:
        jsondata = json.loads(f.read())["config"]
except (json.JSONDecodeError, json.decoder.JSONDecodeError) as e:
    printe(f"lib.py ERROR: Exception \"{e}\" raised by JSON library")

# Get a specific part/key of the config
def getconfig(part):
    try:
        return jsondata[part]
    except KeyError:
        printe(f"lib.py WARNING: Key \"{part}\" does not exist in config/config.json")
        return None

# Timestamp to formatted date
def dt2fmt(dt):
    # TODO: have strfstr read from a config file
    strfstr = getconfig("misc")["strftime"]

    return dt.strftime(strfstr)

# "Human size" data size formatting
def hsize(fsize):
    suffix = "Bytes"
    
    for unit in [" ", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(fsize) < 1024.0:
            return f"{fsize:3.0f}{unit}{suffix}"
        fsize /= 1024.0
        
    return f"{num:.1f}Yi{suffix}"

# Function to prefill context data to make views smaller
def mkcontext(request, title, scripts="none"):
    context = {"title": title, "styling": theme(request.COOKIES.get("theme")), "misc": getconfig("misc"), "navbar": getconfig("navbar"), "ver": __version__}
    
    # font - Load just fontawesome
    # form - Load JQuery and Select2
    # table - Load JQuery, fontawesome and tablesorter
    if scripts == "font":
        context["fa"] = True
        context["jq"] = False
        context["ts"] = False
        context["s2"] = False
    elif scripts == "form":
        context["fa"] = False
        context["jq"] = True
        context["ts"] = False
        context["s2"] = True
    elif scripts == "table":
        context["fa"] = True
        context["jq"] = True
        context["ts"] = True
        context["s2"] = False
    else:
        context["fa"] = False
        context["jq"] = False
        context["ts"] = False
        context["s2"] = False
    
    return context

if exists("themecfg.json"):
    with open("themecfg.json") as f:
        themes = json.loads(f.read())
else:
    printe("lib.py ERROR: themecfg.json does not exist, it may not have been generated yet")
    themes = {}

# Return theme data
def theme(tname):    
    try:
        return themes[tname]
    except KeyError:
        printe(f"lib.py WARNING: Theme \"{tname}\" not found, using default")
        return themes["default"]
        
# Get file/directory listing of a directory
def getdir(directory, showhidden = False):
    listing = []
    filetypes = getconfig("filetypes")
    
    for root, dirs, files in walk(directory, topdown = False):
        for name in files:
            # Files that start with "." are hidden on UNIX-like platforms
            if name.startswith("."):
                if showhidden:
                    listing.append({"type": "Plain Text", "size": getsize(name)})
            else:
                ext = pathlib.Path(name).suffix

                if ext in getconfig("filetypes"):
                    listing.append({"type": filetypes[ext], "size": getsize(name)})
    
    


