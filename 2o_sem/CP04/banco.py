import oracledb
import datetime

def criar_conexao():
    try:
        conn = oracledb.connect(
            user="rm566516",
            password="210806",
            dsn="oracle.fiap.com.br/orcl"
        )
        print("Conectado na versão:", conn.version)
        return conn
    except oracledb.Error as e:
        print("Erro ao conectar ao banco:", e)
        return None


def inclui(venda: dict):
    conn = criar_conexao()
    if not conn:
        return

    try:
        campos_obrigatorios = [
            "nm_comprador", "nm_vendedor", "dt_venda",
            "ds_produto", "vl_total", "vl_impostos"
        ]

        for campo in campos_obrigatorios:
            if campo not in venda or venda[campo] in (None, "", []):
                print(f"Erro: o campo '{campo}' é obrigatório e não pode estar vazio.")
                return

        cur = conn.cursor()
        insert = '''
        INSERT INTO t_vendas 
            (nm_comprador, nm_vendedor, dt_venda, ds_produto, vl_total, vl_impostos)
        VALUES 
            (:nm_comprador, :nm_vendedor, :dt_venda, :ds_produto, :vl_total, :vl_impostos)
        '''

        cur.execute(insert, venda)
        conn.commit()
        print("Venda inserida com sucesso!")

    except oracledb.Error as e:
        print("Erro ao inserir venda:", e)
    finally:
        if 'cur' in locals():
            cur.close()
        conn.close()
        print("Conexão finalizada.")


def altera(venda: dict):
    conn = criar_conexao()
    if not conn:
        return

    try:
        if "id_venda" not in venda or not venda["id_venda"]:
            print("Erro: é necessário informar o 'id_venda' para alterar um registro.")
            return

        cur = conn.cursor()

        #Validação dos campos de entrada
        campos_validos = {
            k: v for k, v in venda.items()
            #Caso o valor seja nulo ou vazio, ele ignora e mantém o valor antigo (não atualiza o campo)
            if v not in (None, "", []) and k != "id_venda"
        }

        if not campos_validos:
            print("Nenhum campo válido para atualização.")
            return

        set_clause = ", ".join([f"{campo} = :{campo}" for campo in campos_validos.keys()])
        sql = f"""
        UPDATE t_vendas
        SET {set_clause}
        WHERE id_venda = :id_venda
        """

        campos_validos["id_venda"] = venda["id_venda"]

        cur.execute(sql, campos_validos)
        conn.commit()

        if cur.rowcount > 0:
            print(f"Venda {venda['id_venda']} atualizada com sucesso!")
        else:
            print(f"❌ Nenhuma venda encontrada com id {venda['id_venda']}.")

    except oracledb.Error as e:
        print("Erro ao alterar venda: ", e)
    finally:
        if 'cur' in locals():
            cur.close()
        conn.close()
        print("Conexão finalizada.")

def menu():
    while True:
        print("\n === MENU DE OPERAÇÕES ===")
        print("1 - Cadastrar nova venda")
        print("2 - Alterar venda existente")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- Cadastro de nova venda ---")
            nm_comprador = input("Nome do comprador: ")
            nm_vendedor = input("Nome do vendedor: ")
            ds_produto = input("Descrição do produto: ")
            vl_total = float(input("Valor total: "))
            vl_impostos = float(input("Valor dos impostos: "))

            venda = {
                "nm_comprador": nm_comprador,
                "nm_vendedor": nm_vendedor,
                "dt_venda": datetime.date.today(),
                "ds_produto": ds_produto,
                "vl_total": vl_total,
                "vl_impostos": vl_impostos
            }

            inclui(venda)

        elif opcao == "2":
            print("\n--- Alterar venda existente ---")
            id_venda = int(input("ID da venda a alterar: "))

            # Valida se o ID existe
            if not verifica_id(id_venda):
                print(f"\n❌ Venda com ID {id_venda} não existe.")
                continue


            print("Preencha apenas os campos que deseja alterar (deixe vazio para ignorar).")

            nm_comprador = input("Nome do comprador: ")
            nm_vendedor = input("Nome do vendedor: ")
            ds_produto = input("Descrição do produto: ")
            vl_total = input("Valor total: ")
            vl_impostos = input("Valor dos impostos: ")

            venda = {
                "id_venda": id_venda,
                "nm_comprador": nm_comprador if nm_comprador else None,
                "nm_vendedor": nm_vendedor if nm_vendedor else None,
                "ds_produto": ds_produto if ds_produto else None,
                "vl_total": float(vl_total) if vl_total else None,
                "vl_impostos": float(vl_impostos) if vl_impostos else None
            }

            altera(venda)

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")
        
def verifica_id(id_venda: int) -> bool:
    conn = criar_conexao()
    if not conn:
        return False

    try:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM t_vendas WHERE id_venda = :id_venda", {"id_venda": id_venda})
        count = cur.fetchone()[0]
        return count > 0
    except oracledb.Error as e:
        print("Erro ao verificar o ID:", e)
        return False
    finally:
        if 'cur' in locals():
            cur.close()
        conn.close()



if __name__ == "__main__":
    menu()