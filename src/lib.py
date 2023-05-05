# CAMS Software - CTCL 2021-2023
# May 4, 2023 - May 4, 2023
# Purpose: Commonly used functions, similar to lib.rs in Rust

from datetime import datetime, timezone
import json

# Timestamp to formatted date
def ts2fmt(ts):
    # TODO: have strfstr read from a config file
    strfstr = "%H:%M, %b %m, %Y %Z"

    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime(strfstr)

# "Human size" data size formatting
def hsize(fsize):
    suffix = " Bytes"
    
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(fsize) < 1024.0:
            return f"{fsize:3.0f}{unit}{suffix}"
        fsize /= 1024.0
        
    return f"{num:.1f}Yi{suffix}"
    
def navbar(active, cfgpath="config/navbar.json"):
    with open(cfgpath) as f:
        jdata = dict(json.load(f))
        
    return jdata
