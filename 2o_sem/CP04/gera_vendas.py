from faker import Faker
import random
import banco

f = Faker('pt-BR')

numero_de_inserts = 20

for _ in range(numero_de_inserts):
    venda = {
        "nm_comprador": f.name(),
        "nm_vendedor": f.name(),
        "dt_venda": f.date_between(start_date='-5y', end_date='today'),
        "ds_produto": f"Tinta {f.color_name()}",
        "vl_total": random.randint(1000, 5000),
        "vl_impostos": random.randint(200, 800)
    }

    banco.inclui(venda)

print(f"{numero_de_inserts} Inserts enviados!")
