# CAMS Software
# Purpose: Main Flask Blueprint
# Date: March 6, 2023 - March 7, 2023
# CTCL 2023

import os
from flask import Blueprint, redirect, render_template, request
from flask_login import current_user, login_required, logout_user

main_bp = Blueprint("main_bp", __name__, template_folder="templates", static_folder="static")

@main_bp.route("/")
def main_root():
    return "test"




@main_bp.before_request 
def before_every_request():
    try:
        if os.environ["CAMSDBISINIT"] == "1":
            dbisinit = True
        else:
            dbisinit = False
    except KeyError:
        dbisinit = False
    
    rqpath = request.path
    # Still let the user access the built-in documentation even if the app is not set up yet
    if dbisinit == False and not (rqpath.startswith("/setup") or rqpath.startswith("/about")):
        return render_template("setup/not_setup.jinja2", title = "Not set up")
        
    # If setup is already done, redirect any setup page to root
    if dbisinit and rqpath.startswith("/setup"):
        return redirect("/")
