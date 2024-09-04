# auth_loader.py
from .models.usuario import Usuario


def load_user(user_id):
    return Usuario.query.get(int(user_id))
