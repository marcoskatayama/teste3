from datetime import datetime

from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

from ..extensions import db
from ..models.pedido import Pedido


def get_pedidos_por_mes_empresa(mes_atual: int):
    if mes_atual is None:
        mes_atual = datetime.now().month
    try:
        resultados = (
            db.session.query(
                Pedido.empresa_id,
                func.count(Pedido.id).label('total_pedidos')
            )
            .filter(func.extract('month', Pedido.data_emissao) == mes_atual)
            .filter(func.extract('year', Pedido.data_emissao) == datetime.now().year)
            .group_by(Pedido.empresa_id)
            .all()
        )

        pedidos_por_mes = [
            {'empresa_id': resultado.empresa_id, 'total_pedidos': resultado.total_pedidos} for resultado in resultados
        ]

        return pedidos_por_mes

    except SQLAlchemyError as e:
        print(str(e))
        return []


def get_todos_pedidos():
    try:
        resultados = (
            db.session.query(
                Pedido.id,
                Pedido.data_emissao,
                Pedido.total_final,
                Pedido.empresa_id
            )
            .all()
        )

        return resultados
    except SQLAlchemyError as e:
        print(str(e))
        return []
