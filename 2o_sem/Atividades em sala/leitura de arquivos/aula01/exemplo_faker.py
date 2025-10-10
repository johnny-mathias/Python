#precisamos instalar a biblioteca
#pip install faker

from faker import Faker

dados_falsos = Faker('pt-BR')

with open("comandos.sql", 'w', encoding='utf8') as arquivo:
    for _ in range(100):
        #print(dados_falsos.name())
        #print(dados_falsos.address())
        #print("__________________\n")
        nome = dados_falsos.name()
        cidade = dados_falsos.city()
        cep = dados_falsos.postcode()
        sql = f"INSERT INTO pessoa(nome, cidade, cep) VALUES('{nome}', '{cidade}', '{cep}');"
        arquivo.write(sql + "\n")
print('Gerou SQL Fake')