# CAMS Software
# Purpose: Configuration class that reads from config.js
# Date: March 1, 2023 - March 7, 2023
# CTCL 2023

import json
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))

# Values left blank are filled in later
defaultconfig = {
    "FLASK_APP": "wsgi.py",
    "FLASK_ENV": "",
    "SECRET_KEY": "tempkey",
    "STATIC_DIR": "static",
    "TEMPLATES_DIR": "templates",
    "SQLALCHEMY_DATABASE_URI": "",
    "SQLALCHEMY_ECHO": False,
    "SQLALCHEMY_TRACK_MODIFICATIONS": False
    }

if path.exists("./config.json"):
    with open("config.json", "r") as f:
        configdata = json.load(f)
        for i in configdata:
            environ[i] = str(configdata[i])
else:
    print("config.json does not exist in the current directory, creating one now")
    with open("config.json", "w") as f:
        json.dump(defaultconfig, f)
        configdata = defaultconfig
        for i in configdata:
            environ[i] = str(configdata[i])

class Config:
    # Bad idea?
    for i in configdata:
        locals()[i] = configdata[i]
        
