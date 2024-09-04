from datetime import datetime

from flask import Blueprint, render_template
from flask_login import login_required

from ..services.pedido_queries import (get_pedidos_por_mes_empresa,
                                       get_todos_pedidos)
from ..services.produto_queries import get_produtos_mais_vendidos

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    data_atual = datetime.now()
    mes_atual = data_atual.month

    pedidos_por_mes = get_pedidos_por_mes_empresa(mes_atual)
    pedidos_por_mes_labels = [f"Empresa {pedido['empresa_id']}" for pedido in pedidos_por_mes]
    pedidos_por_mes_data = [pedido['total_pedidos'] for pedido in pedidos_por_mes]

    produtos_mais_vendidos = get_produtos_mais_vendidos(mes_atual)
    produtos_mais_vendidos_labels = [produto['produto_id'] for produto in produtos_mais_vendidos]
    produtos_mais_vendidos_data = [produto['total_vendido'] for produto in produtos_mais_vendidos]

    todos_pedidos = get_todos_pedidos()

    return render_template(
        'dashboard/dashboard.html',
        pedidos_por_mes_labels=pedidos_por_mes_labels,
        pedidos_por_mes_data=pedidos_por_mes_data,
        produtos_mais_vendidos_labels=produtos_mais_vendidos_labels,
        produtos_mais_vendidos_data=produtos_mais_vendidos_data,
        todos_pedidos=todos_pedidos
    )
