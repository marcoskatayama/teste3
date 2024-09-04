from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user

from ..models.usuario import Usuario

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))

    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')
        user = Usuario.query.filter_by(login=login).first()

        if user and user.check_password(senha):
            login_user(user)
            return redirect(url_for('home.home'))
        else:
            flash('Login inválido. Verifique suas credenciais.')

    return render_template('auth/login.html')


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
