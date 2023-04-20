# CAMS Software
# CTCL 2021-2023
# March 23, 2023 - March 27, 2023
# Purpose: Flask Blueprint for the integrated documentation feature

from flask import Blueprint, render_template, abort
from flask_mdeditor import MDEditor
import os

docs_bp = Blueprint("docs", __name__, template_folder = "templates")

# TODO: Document editing should be only available when the admin user is logged in

#@docs_bp.route("/<path>/")
