# app/routes.py
from flask import Flask

from .auth.routes import auth_bp
from .dashboard.routes import dashboard_bp
from .home.routes import home_bp


def register_routes(app: Flask):

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(home_bp)
