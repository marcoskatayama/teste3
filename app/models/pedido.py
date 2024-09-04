from datetime import datetime

from sqlalchemy import Sequence

from ..extensions import db


class Pedido(db.Model):
    __tablename__ = 'pedido'

    id_seq = Sequence('pedido_id_seq', start=1)

    id = db.Column(db.BigInteger, primary_key=True,
                   server_default=id_seq.next_value())
    empresa_id = db.Column(db.BigInteger, db.ForeignKey('empresa.id'))
    ativo = db.Column(db.Integer, nullable=False, default=0)
    local_atualizar = db.Column(db.Integer, nullable=False, default=0)
    local_codigo = db.Column(db.Integer, nullable=False, default=0)
    cliente_id = db.Column(db.BigInteger, db.ForeignKey('cliente.id'))
    data_emissao = db.Column(db.DateTime, default=datetime.utcnow)
    total_produto = db.Column(db.Float(18, 4), default='0.00')
    total_final = db.Column(db.Float(18, 4), default='0.00')
    despesas = db.Column(db.Float(18, 4), default='0.00')
    observacoes = db.Column(db.String(300))
    produtos = db.relationship('PedidoProduto', back_populates='pedido')
