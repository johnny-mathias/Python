from faker import Faker
import random
import banco

f = Faker('pt-BR')

# Número total de vendas
total_vendas = random.randint(20, 50)

# Criar vendedores
vendedores = [f.name() for _ in range(10)]

vendas = []

# Primeiro, distribuir 2 a 5 vendas por vendedor
for vendedor in vendedores:
    num_vendas = random.randint(2, 5)
    for _ in range(num_vendas):
        comprador = f.name()
        venda = {
            "nm_comprador": comprador,
            "nm_vendedor": vendedor,
            "dt_venda": f.date_between(start_date='-5y', end_date='today'),
            "ds_produto": f"Tinta {f.color_name()}",
            "vl_total": random.randint(1000, 5000),
            "vl_impostos": random.randint(200, 800)
        }
        vendas.append(venda)

# Se ultrapassou total_vendas, corta a lista
if len(vendas) > total_vendas:
    vendas = random.sample(vendas, total_vendas)

# Se ficou abaixo, adiciona vendas aleatórias até atingir o total
while len(vendas) < total_vendas:
    vendedor = random.choice(vendedores)
    comprador = f.name()
    venda = {
        "nm_comprador": comprador,
        "nm_vendedor": vendedor,
        "dt_venda": f.date_between(start_date='-5y', end_date='today'),
        "ds_produto": f"Tinta {f.color_name()}",
        "vl_total": random.randint(1000, 5000),
        "vl_impostos": random.randint(200, 800)
    }
    vendas.append(venda)

# Enviar para o banco
for venda in vendas:
    banco.inclui(venda)

print(f"\n{len(vendas)} vendas geradas!")
