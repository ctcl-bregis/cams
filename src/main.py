# CAMS Software - CTCL 2021-2023
# April 21, 2023 - April 24, 2023
# Purpose: Flask blueprint for unspecified pages and user authentication

from flask import Blueprint, render_template, abort, request
from flask_login import login_required

main_bp = Blueprint("main", __name__, template_folder="templates/docs")

main_bp.
