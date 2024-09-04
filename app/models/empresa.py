from sqlalchemy import Sequence

from ..extensions import db


class Empresa(db.Model):
    __tablename__ = 'empresa'

    id_seq = Sequence('empresa_id_seq', start=1)

    id = db.Column(db.BigInteger, primary_key=True,
                   server_default=id_seq.next_value())
    ativo = db.Column(db.Integer, nullable=False, default=0)
    razao = db.Column(db.String(255))
    nome = db.Column(db.String(255))
    cnpj = db.Column(db.String(20))
