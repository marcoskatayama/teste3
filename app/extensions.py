# extensions.py
# Contém as instâncias globais do Flask (db, login_manager, etc.)
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
