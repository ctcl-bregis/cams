# CAMS Software - CTCL 2021-2023
# March 27, 2023 - May 4, 2023
# Purpose: App initialization

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

# Flask Login Manager
flm = LoginManager()

def mkapp():
    
    
    app = Flask(__name__, instance_relative_config=False)
    app.url_map.strict_slashes = True
    
    # If this environment variable is set to True by supposedly ./runner_dev, run in "Development" mode
    if os.environ["CAMS_DEVMODE"] == "True":
        # Default to the "in-memory" db location in /dev/shm/
        os.environ["CAMSDB_URL"] = dburl = "./data/data.db"
        os.environ["CAMSDB_INIT"] = "False"
        dbinit = bool(os.environ["CAMSDB_INIT"])
        
        app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(dburl),
        )
        
    else:
        # For now, CAMS is "Development" only until it is ready to be used by CTCL
        raise NotImplementedError
    
    from src.docs import docs_bp
        
    #app.register_blueprint(auth.bp)
    app.register_blueprint(docs_bp, url_prefix = "/docs")
    #app.register_blueprint(main.bp)
    #app.register_blueprint(mktg.bp)
    
    
    return app
    
