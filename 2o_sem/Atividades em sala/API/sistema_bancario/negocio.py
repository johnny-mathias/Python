from banco import *

def abrir_conta(cliente: dict, cep: str):
    try:
        #pego o cep do cliente e faço uma consulta no viacep
        endereco = consulta_viacep(cep)

        insere_cliente(cliente)
        insere_endereco(endereco, cliente['id'])
        insere_conta(cliente)
    except Exception as e:
        msg = f'Erro na abertura de conta do cliente {cliente["nome"]}'
        raise Exception(msg)