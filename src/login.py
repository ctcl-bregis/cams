# CAMS Software
# Purpose: User Login Blueprint
# Date: March 7, 2023 - March 8, 2023
# CTCL 2023

import os
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user
from . import login_manager
from .forms import LoginForm, SignupForm

try:
    if os.environ["CAMSDBISINIT"] == "1":
        from .models import User, db
    else:
        pass
except KeyError:
    pass
    
login_bp = Blueprint("login_bp", __name__, template_folder="templates", static_folder="static")
    
@login_manager.user_loader
def load_user(user_id):
    if user is not None:
        return User.query.get(user)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    flash("You must be logged in to view that page.")
    return redirect("/login/")
