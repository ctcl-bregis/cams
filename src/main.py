# CAMS Software - CTCL 2021-2023
# April 21, 2023 - April 24, 2023
# Purpose: Flask blueprint for unspecified pages

from flask import Blueprint, render_template, abort, request

bp = Blueprint("main", __name__, template_folder="templates/docs")

