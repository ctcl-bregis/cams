# CAMS Software
# Purpose: Setup Flask Blueprint
# Date: March 6, 2023 - March 6, 2023
# CTCL 2023

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user

from . import login_manager
#from .forms import LoginForm, SignupForm
#from .models import User, db

setup_bp = Blueprint("setup_bp", __name__, template_folder="templates", static_folder="static")

@setup_bp.route("/setup/adminuser/", methods=["GET", "POST"])
def adminuser():
    form = SignupForm()
    if form.validate_on_submit():
        return "test"
        
