from sqlalchemy import Sequence

from ..extensions import db


class PedidoProduto(db.Model):
    __tablename__ = 'pedido_produto'

    id_seq = Sequence('pedido_produto_id_seq', start=1)

    id = db.Column(db.BigInteger, primary_key=True,
                   server_default=id_seq.next_value())
    empresa_id = db.Column(db.BigInteger, db.ForeignKey('empresa.id'))
    ativo = db.Column(db.Integer, nullable=False, default=0)
    pedido_id = db.Column(db.BigInteger, db.ForeignKey('pedido.id'))
    produto_id = db.Column(db.BigInteger, db.ForeignKey('produto.id'))
    qtde = db.Column(db.Float(18, 4), default='0.00')
    valor_unit = db.Column(db.Float(18, 4), default='0.00')
    produto_descricao = db.Column(db.String(120))
    unidade_descricao = db.Column(db.String(6))
    desconto = db.Column(db.Float(18, 4), default='0.00')
    pedido = db.relationship('Pedido', back_populates='produtos')
