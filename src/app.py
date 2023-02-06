# CAMS Software
# Purpose: Main application code
# Date: ???, 2022 - Febuary 5, 2023
# CrazyblocksTechnologies Computer Laboratories 2022-2023

# External libraries
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from os.path import exists
import csv, json, os, stat, flask_login
from markdown2 import Markdown
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

# Libraries within cams directory
from dbinit import initdb, checkdb
import forms
import mktag
from lib import csv2list

# Hard-coded user "database", this data should be stored in the DB later on and created during app setup
users = {'user': {'password': 'test123'}}

class User(flask_login.UserMixin):
    pass

cams = Flask(__name__, template_folder = "../templates/", static_folder = "../static/")
    
# Location of the database file
dbfile = "data/data.db"

basedir = os.path.abspath(os.path.dirname(__file__))
cams.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, dbfile)
cams.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
db = SQLAlchemy(cams)
db.init_app(cams)

# Path for documentation
docs = "./docs"

with open("key.txt", "r") as f:
    key = f.readlines()[0]
    cams.secret_key = key
    del key

# flask-login
login_manager = flask_login.LoginManager()
login_manager.init_app(cams)

# Callback for login failure.
@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect("/login/")

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
@cams.route('/logout/')
def logout():
    flask_login.logout_user()
    return render_template("logout.html", title = "Logged out")

# Run every time
@cams.before_request
def before_request():
    # Check if the DB is ready
    if checkdb(dbfile):
        pass
    else:
        redirect("/setup/")
        
# Login page
@cams.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html", title = "Login")
    
    email = request.form['username']
    if email in users and request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('main'))

    return render_template("login.html", title = "Login Error")

# Root page
@cams.route("/")
def root():
    # Get the login cookie, if it exists or not
    login_cookie = request.cookies.get('session')
    
    # NoneType if the cookie was not set
    if login_cookie == None:
        return redirect("/login/")
    else:
        return redirect("/main/")

@cams.route('/about/')
def main_about_doc_root():
    filelist = []
    for i in os.listdir(docs):
        print(i)
        if os.path.isdir(f"{docs}/{i}/"):
            tempdict = {"disp": f"{i}/", "link": f"/about/{i}"}
            filelist.append(tempdict)
        elif i.endswith(".md"):
            tempdict = {"disp": f"{i}", "link": f"/about/{i}"}
            filelist.append(tempdict)
    
    return render_template('docs_dir.html', title = "Documentation", filelist = filelist)


# Documentation pages are basically a file browser
@cams.route("/about/<path:path>")
def main_about_docs(path):
    docs_path = f"{docs}/{path}"
    
    if os.path.isdir(docs_path):
        filelist = []
        
        for i in os.listdir(docs_path):
            if os.path.isdir(f"{docs_path}/{i}"):
                tempdict = {"disp": f"{i}/", "link": f"/about/{path}/{i}/"}
                filelist.append(tempdict)
            elif i.endswith(".md"):
                tempdict = {"disp": f"{i}", "link": f"/about/{path}/{i}"}
                filelist.append(tempdict)
    
        return render_template("docs_dir.html", title = f"Documentation - {path}", filelist = filelist)
        
    elif os.path.isfile(docs_path):
        md_converter = Markdown()
        
        with open(docs_path, "r") as f:
            content = md_converter.convert(f.read())
        
        return render_template("docs_file.html", title = f"Documentation - {path}", content = content)
    else:
        return docs_path + " not found", 404
    
    

# Main, "dashboard" page
@cams.route("/main/")
@flask_login.login_required
def main():
    currentuser = flask_login.current_user.id

    menulist = csv2list("config/menu.csv")
        
    return render_template("main.html", title = "Main Menu", user = currentuser, menu = menulist)

@cams.route("/main/search")
@flask_login.login_required
def main_search():
    currentuser = flask_login.current_user.id
    
    return render_template("search.html", title = "Search", user = currentuser)

# New Item
@cams.route("/main/new")
@flask_login.login_required
def main_new():
    currentuser = flask_login.current_user.id
    
    menulist = csv2list("config/devtypes/devtypes.csv")
    
    return render_template("item_new_menu.html", title = "New Entry", user = currentuser, menu = menulist)
    
# Interactions with entries fall under this URL and actions are passed as parameters (e.g. /main/id/12345678?action=delete)
# Planned actions: delete, mktag (make id tag), edit
@cams.route("/main/id/<cid>/<action>")
@flask_login.login_required
def main_id(cid, action):
    return "Not Implemented", 404
    
# New device entry
@cams.route("/main/new/<devtype>", methods=["GET", "POST"])
@flask_login.login_required
def main_new_entry(devtype):
    
    currentuser = flask_login.current_user.id

    with open("config/devtypes/devtypes.csv") as tables:
        tables = csv.DictReader(tables)
        tables = list(tables)
        table_keys = [i['table'] for i in tables]

        if not devtype in table_keys:
            return "Not Found", 404
        else:
            devtype_name = next((item for item in tables if item["table"] == devtype), None)
            devtype_name = devtype_name["name"]
        
        
    cols = csv2list(f"config/devtypes/{devtype}/cols.csv")
    # TODO: Forms should be not initialized every time a page is loaded that uses them
    form = forms.form_printer(cols)()
    
    if form.validate_on_submit():
        return redirect("/")
    else:
        return render_template("item_new.html", form = form, title = "New Entry", devtype = devtype_name, user = currentuser)
