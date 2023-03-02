from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required, logout_user

# Main Flask blueprint
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@main_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")
