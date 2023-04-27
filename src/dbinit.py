
from .. import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

fileheader = """# CAMS Software - CTCL 2021 - 2023
# Generated: 
# Purpose: Automatically generated database models
"""
