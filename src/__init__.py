# CAMS Software
# CTCL 2021-2023
# March 27, 2023 - March 27, 2023
# Purpose: App initialization

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

# Flask Login Manager
flm = LoginManager()

def mkapp():
    app = Flask(__name__)
    
    # Check environment variable
    # If the environment variable is not set to "True", assume the database is not initialized but clear it anyway.
    if os.environ["CAMS_DBINIT"] != "True":
        with open("test.txt", "w") as f:
            f.write("test")
        
        
    return app
    
