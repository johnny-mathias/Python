import banco
import datetime

venda = {
    "nm_comprador": "Johnny",
    "nm_vendedor": "Luisa",
    "dt_venda": datetime.date.today(),
    "ds_produto": "Churros sabor chocolate",
    "vl_total": 2000,
    "vl_impostos": 300
}

banco.inclui(venda)