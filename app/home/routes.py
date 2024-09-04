from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
@login_required
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return render_template('home.html')
