# CAMS by CrazyblocksTechnologies Computer Laboratories
# Created - Last Updated: October 19, 2022 - November 3, 2022
# Purpose: Main application code

# External libraries
from flask import Flask, render_template, request, redirect, url_for
from os.path import exists
import csv
import json
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

# Libraries within cams directory
import flask_login
from dbinit import init_db

# Hard-coded user "database", this data should be stored in the DB later on
users = {'ctcl': {'password': 'test123'}}

cams = Flask(__name__)

# Location of the database file
dbfile = "data/data.db"

basedir = os.path.abspath(os.path.dirname(__file__))
cams.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, dbfile)
cams.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(cams)

# Load key
with open("key.txt") as f:
    key = f.readlines()[0]
    cams.secret_key = key
    del key

# flask-login
login_manager = flask_login.LoginManager()
login_manager.init_app(cams)

class User(flask_login.UserMixin):
    pass

# Callback for login failure. May have this redirect to the login instead.
@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401

@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return

    user = User()
    user.id = username
    return user

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user

# Log out the user; clear the session cookie
@cams.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

# 
@cams.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("cams_login.html", title = "Login")
    
    email = request.form['username']
    if email in users and request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('main'))

    return render_template("cams_login.html", title = "Login Error")

# Root page
@cams.route("/")
def root():
    # Get the login cookie, if it exists or not
    login_cookie = request.cookies.get('session')

    # NoneType if the cookie was not set
    if login_cookie == None:
        return redirect("/login")
    else:
        return redirect("/main")
    
# About
# Does not require logim
@cams.route("/about")
def main_about():
    return render_template("cams_about.html", title = "About")

@cams.route("/about/docs_main")
def main_about_docs_main():
    return render_template("docs/docs_main.html", title = "Documentation")

# Main, "dashboard" page
@cams.route("/main")
@flask_login.login_required
def main():
    currentuser = flask_login.current_user.id

    with open("config/menu.csv") as f:
        menulist = list(csv.DictReader(f))
        
        

    return render_template("cams_main.html", title = "Main Menu", user = currentuser, menu = menulist)

@cams.route("/main/search")
@flask_login.login_required
def main_search():
    currentuser = flask_login.current_user.id
    
    return render_template("cams_search.html", title = "Search", user = currentuser)

# New Item
@cams.route("/main/new")
@flask_login.login_required
def main_new():
    currentuser = flask_login.current_user.id
    
    with open("config/types/index.csv") as f:
        menulist = list(csv.DictReader(f))
    
    
    return render_template("cams_new.html", title = "New Entry", user = currentuser, menu = menulist)
    
# Interactions with entries fall under this URL and actions are passed as parameters (e.g. /main/id/12345678?action=delete)
@cams.route("/main/id/<id>")
@flask_login.login_required
def main_id():
    return "Not Implemented", 404
        
@cams.route("/main/mktag")
@flask_login.login_required
def main_mktag():
    return "Not Implemented", 404


@cams.route('/initdb')
def initdb():
    init_db()
    return "db initialized"
