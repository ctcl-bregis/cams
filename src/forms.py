# CAMS Software
# Purpose: Forms
# Date: March 6, 2023 - March 6, 2023
# CTCL 2023

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional
