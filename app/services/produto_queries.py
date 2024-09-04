from datetime import datetime

from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

from ..extensions import db
from ..models.pedido import Pedido
from ..models.pedido_produto import PedidoProduto


def get_produtos_mais_vendidos(mes_atual: int):
    if mes_atual is None:
        mes_atual = datetime.now().month

    try:
        resultados = (
            db.session.query(
                PedidoProduto.produto_id,
                func.sum(PedidoProduto.qtde).label('total_vendido')
            )
            .join(Pedido, Pedido.id == PedidoProduto.pedido_id)
            .filter(func.extract('month', Pedido.data_emissao) == mes_atual)
            .filter(func.extract('year', Pedido.data_emissao) == datetime.now().year)
            .order_by(PedidoProduto.qtde)
            .all()
        )

        produtos = [
            {'produto_id': resultado.produto_id, 'total_vendido': resultado.total_vendido} for resultado in resultados
        ]

        return produtos
    except SQLAlchemyError as e:
        print(str(e))
        return []
