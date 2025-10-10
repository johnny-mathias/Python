import oracledb

def get_conexao():
    return oracledb.connect(user='rm566516', password='210806', dsn='oracle.fiap.com.br/orcl')

def recupera_pelo_nome(nome: str) -> dict:
    pass

def insere_time(time: dict):
    