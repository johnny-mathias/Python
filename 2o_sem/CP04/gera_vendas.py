from faker import Faker
import random

#Usei só 'f' pra facilitar a leitura do código
f = Faker('pt-BR')

with open("comandos.sql", 'w', encoding='utf8') as arquivo:
    for _ in range(20):
        nm_comprador = f.name()
        nm_vendedor = f.name()
        dt_venda = f.date_between(start_date='-5y')
        ds_produto = f"Produto {f.color_name()}"
        vl_total = random.randint(1000, 5000)
        vl_impostos = random.randint(200, 800)
        sql = f" INSERT INTO t_vendas (nm_comprador, nm_vendedor, dt_venda, ds_produto, vl_total, vl_impostos) " \
        f"VALUES ('{nm_comprador}', '{nm_vendedor}', TO_DATE('{dt_venda}', 'YYYY-MM-DD'), '{ds_produto}', {vl_total}, {vl_impostos});"
        
        arquivo.write(sql + "\n")
print('Gerou SQL Fake')