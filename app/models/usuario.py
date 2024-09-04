from flask_login import UserMixin
from sqlalchemy import Sequence
from werkzeug.security import check_password_hash

from ..extensions import db


class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'

    id_seq = Sequence('usuario_id_seq', start=1)

    id = db.Column(db.BigInteger, primary_key=True,
                   server_default=db.text("nextval('usuario_id_seq')"))
    empresa_id = db.Column(db.BigInteger, db.ForeignKey('empresa.id'))
    ativo = db.Column(db.Integer, nullable=False, default=0)
    local_atualizar = db.Column(db.Integer, nullable=False, default=0)
    login = db.Column(db.String(100))
    senha = db.Column(db.String(255))
    nivel = db.Column(db.String(50))

    def check_password(self, password):
        return check_password_hash(self.senha, password)
