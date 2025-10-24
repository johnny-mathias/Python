import oracledb

def get_conexao():
    return oracledb.connect(user="rm566516", senha="210806", dsn="oracle.fiap.com.br/orcl")

def consulta_viacep(cep):
    end = {
        "logradouro": "Av Paulista",
        "lairro": "Bela Vista",
        "cidade": "São Paulo",
        "cep": cep
    }

def insere_cliente(cliente):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "INSERT INTO cliente(nm_cliente, cpf, tel_cliente) VALUES (:nm_cliente, :tel_cliente, :cpf) RETURNING id INTO :id"

            new_var = cur.var(oracledb.NUMBER)
            cliente['id'] = new_var

            cur.execute(sql, cliente)
            cliente['id'] = new_var.getValue()[0]
        con.commit()
            
def insere_endereco(endereco, id_cliente):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "INSERT INTO cliente(logradouro, bairro, cidade, cep, pessoa_id) " \
                "VALUES (:logradouro, :bairro, :cidade, :cep, :pessoa_id)"

            endereco['pessoa_id'] = id_cliente
            cur.execute(sql, endereco)
        con.commit()

def insere_conta(cliente: dict):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "SELECT sq_numero.NEXTVAL from dual"
            cur.execute(sql)
            registro = cur.fetchone()
            id_conta = registro[0]
            print(f"Conta: {id_conta}")

            sql = "INSERT INTO conta(tipo, numero, senha, saldo, cliente_id) VALUES ('corrente', :id_conta, 'admin', 0, :cliente_id)"

            info = {
                "id_conta": id_conta, "cliente_id": cliente['id']
            }
            cur.execute(sql, info)
        con.commit()
