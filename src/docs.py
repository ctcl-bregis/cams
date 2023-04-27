# CAMS Software - CTCL 2021-2023
# March 23, 2023 - April 26, 2023
# Purpose: Flask Blueprint for the integrated documentation feature

from flask import Blueprint, render_template, abort
from flask_mdeditor import MDEditor
from os import listdir
from os.path import isfile, join

docs_bp = Blueprint("docs", __name__, template_folder = "templates")

# TODO: Document editing should be only available when the admin user is logged in

@docs_bp.route("/", defaults = {"path": ""})
@docs_bp.route("/<path:path>")
def index(path):
    # TODO: Have this read from user preferences in DB
    theme = "themes/dark_flat.css"
    
    title = f"CAMS Integrated Documentation - {path}"
    
    contents = [["test"]]
    
    return render_template("docs_browse.jinja2", contents = contents, title = title, theme = theme)
