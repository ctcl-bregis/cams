# CAMS Software
# Purpose: App initialization
# Date: March 1, 2023 - March 6, 2023
# CTCL 2023

import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy_utils import database_exists

db = SQLAlchemy()
login_manager = LoginManager()

def mkapp():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    
    login_manager.init_app(app)
    
    with app.app_context():
        from . import routes, setup, docs, login
        
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(setup.setup_bp)
        app.register_blueprint(docs.docs_bp)
        app.register_blueprint(login.login_bp)
        
        return app

def checkdb(app):
    # Set an environment variable, may be a better way to do this?
    if database_exists(app.config.SQLALCHEMY_DATABASE_URI):
        os.environ["CAMSDBISINIT"] = "1"
    else:
        os.environ["CAMSDBISINIT"] = "0"
