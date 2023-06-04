# CAMS Asset Management System - CTCL 2021-2023
# May 4, 2023 - May 24, 2023
# Purpose: Commonly used functions, similar to lib.rs in Rust

from datetime import datetime, timezone
import json, base64
from os import listdir
from os.path import isdir, join, exists


themes = {}

themedir = [f for f in listdir("config/themes") if isdir(join("config/themes", f))]
for i in themedir:
    tdata = {}
    try:
        with open(f"config/themes/{i}/index.json") as f:
            jdata = dict(json.load(f))
        
        temppath = jdata["theme"]["css"]
        with open(f"config/themes/{i}/{temppath}") as f:
            tdata["themecss"] = f.read()
        
        temppath = jdata["theme"]["logo"]
        with open(f"config/themes/{i}/{temppath}") as f:
            tdata["logo"] = "data:image/svg+xml;base64," + base64.b64encode(f.read().encode("utf-8")).decode("utf-8")
            
        themes[i] = tdata
    except FileNotFoundError:
        print(f"WARNING: Theme {i} does not have a index.json, it would not be available")
        pass


# Timestamp to formatted date
def ts2fmt(ts):
    # TODO: have strfstr read from a config file
    strfstr = "%H:%M, %b %m, %Y %Z"

    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime(strfstr)

# "Human size" data size formatting
def hsize(fsize):
    suffix = "Bytes"
    
    for unit in [" ", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(fsize) < 1024.0:
            return f"{fsize:3.0f}{unit}{suffix}"
        fsize /= 1024.0
        
    return f"{num:.1f}Yi{suffix}"
   
# Active page, cfgpath has a default value that can be overridden
def navbar(active, cfgpath="config/navbar.json"):
    with open(cfgpath) as f:
        jdata = dict(json.load(f))
        
    return jdata


def theme(tname):
    try:
        tdata = themes[tname]
        return tdata
    except KeyError:
        print(f"CAMS Warning: Theme \"{tname}\" not found, using default")
        
    
