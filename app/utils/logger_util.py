import codecs
import logging
import os
import time
from datetime import datetime
from enum import Enum
from logging.handlers import TimedRotatingFileHandler

import psutil

from config import LOG_DIR


class LogLevel(Enum):
    INFO = 'info'
    WARNING = 'warning'
    ERROR = 'error'
    EXCEPTION = 'exception'


# INFO: Para relatar eventos gerais no sistema, como o início ou término de
# uma operação, ou outros eventos significativos que não indicam problemas.

# WARNING: Para indicar que algo inesperado aconteceu ou que há uma situação
# que pode se tornar um problema no futuro, mas que não impede a execução do
# programa.

# ERROR: Para relatar erros que ocorrem durante a execução do programa, mas
# que não causam a parada do sistema. Geralmente, são problemas que precisam
# ser corrigidos.

# EXCEPTION: Para registrar exceções não tratadas que ocorrem no programa.
# Isso geralmente inclui o rastreamento completo da pilha para ajudar na
# depuração.

def setup_logging(log_file):
    logger = logging.getLogger()

    # Verifica se o logger já tem handlers configurados
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        file_handler = codecs.open(log_file, 'a', 'utf-8')
        file_handler = TimedRotatingFileHandler(
            log_file, when="midnight", interval=1, backupCount=30)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)


def get_log_file_path():
    current_date = datetime.now().strftime('%Y-%m-%d')

    log_dir = os.path.join("logs")

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, f"{current_date}.log")

    if not os.path.exists(log_file):
        with open(log_file, 'w', encoding='utf-8'):
            pass
    return log_file


def log_message(level, msg):
    log_file = get_log_file_path()
    setup_logging(log_file)
    logger = logging.getLogger()

    if level == LogLevel.INFO:
        logger.info(msg)
    elif level == LogLevel.WARNING:
        logger.warning(msg)
    elif level == LogLevel.ERROR:
        logger.error(msg)
    elif level == LogLevel.EXCEPTION:
        logger.exception(msg)
    else:
        logger.info(msg)


def clean_old_logs():
    logs_dir = LOG_DIR
    for root, dirs, files in os.walk(logs_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                if is_file_in_use(file_path):
                    print(
                        f"O arquivo {file_path} está sendo utilizado por "
                        "outro processo. Pulando para o próximo arquivo."
                    )
                    continue
                file_creation_time = os.path.getctime(file_path)
                if (time.time() - file_creation_time) // (24 * 3600) >= 30:
                    try:
                        os.remove(file_path)
                    except PermissionError as e:
                        print(
                            "Não foi possível remover o arquivo "
                            f"{file_path}: {e}"
                        )


def is_file_in_use(file_path):
    for proc in psutil.process_iter(['open_files']):
        try:
            open_files = proc.info['open_files']
            if open_files:
                for open_file in open_files:
                    if open_file.path == file_path:
                        return True
        except psutil.NoSuchProcess:
            pass
    return False
