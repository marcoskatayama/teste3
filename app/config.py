import os

from dotenv import load_dotenv

# Determine o ambiente atual
# AMBIENTE = os.getenv('FLASK_ENV', 'testing')

# # Mapeia o ambiente para o arquivo .env correspondente
# env_files = {
#     'development': '.env.development',
#     'testing': '.env.testing',
#     'production': '.env.production'
# }

# Carrega o arquivo .env correto
# load_dotenv(env_files[AMBIENTE])
load_dotenv()

# Configurações BD
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('POSTGRES_PORT')
DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DATABASE_URI = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

SECRET_KEY = os.getenv('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Diretório de Logs
LOG_DIR = 'logs'
