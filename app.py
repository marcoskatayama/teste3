import os
import sys

from flask import Flask
from flask_migrate import Migrate

from app.config import DATABASE_URI, SECRET_KEY, SQLALCHEMY_TRACK_MODIFICATIONS
from app.extensions import db, login_manager
from app.routes import register_routes

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# from app.utils.logger_util import (LogLevel, get_log_file_path, log_message,
#                                    setup_logging)


# Log
# def setup_log():
#     log_file = get_log_file_path()
#     setup_logging(log_file)

#     log_message(
#         level=LogLevel.INFO,
#         msg=(
#             "Iniciando serviço no ambiente "
#             f"{AMBIENTE} usando o banco de dados {DB_NAME}..."
#         )
#     )


def create_app():
    app = Flask(__name__)

    # Configurações do aplicativo Flask
    app.config['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = \
        SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_size': 20,
        'max_overflow': 10,
        'pool_recycle': 1800  # Recicla conexões a cada 30 minutos
    }
    app.config['SECRET_KEY'] = SECRET_KEY

    # Inicializando o banco de dados e o gerenciador de login
    db.init_app(app)
    login_manager.init_app(app)

    Migrate(app, db)

    # Importar e configurar o carregador de usuários após a configuração das extensões
    from app.auth_loader import load_user
    login_manager.user_loader(load_user)

    # Registra as rotas
    register_routes(app)

    # Configurando o log
    # setup_log()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=8000, debug=False)
