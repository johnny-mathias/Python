import oracledb
import datetime

def criar_conexao():
    """Cria conexão e cursor e retorna ambos."""
    try:
        conn = oracledb.connect(
            user="rm566516",
            password="210806",
            dsn="oracle.fiap.com.br/orcl"
        )
        cur = conn.cursor()
        print("Conectado na versão:", conn.version)
        return conn, cur
    except oracledb.Error as e:
        print("Erro ao conectar ao banco:", e)
        return None, None


def fechar_conexao(conn, cur):
    """Fecha cursor e conexão, se existirem."""
    try:
        if cur:
            cur.close()
        if conn:
            conn.close()
        print("Conexão finalizada.")
    except oracledb.Error as e:
        print("Erro ao fechar a conexão:", e)


def inclui(venda: dict):
    conn, cur = criar_conexao()
    if not conn or not cur:
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

        sql = '''
        INSERT INTO t_vendas 
            (nm_comprador, nm_vendedor, dt_venda, ds_produto, vl_total, vl_impostos)
        VALUES 
            (:nm_comprador, :nm_vendedor, :dt_venda, :ds_produto, :vl_total, :vl_impostos)
        '''
        cur.execute(sql, venda)
        conn.commit()
        print("Venda inserida com sucesso!")

    except oracledb.Error as e:
        print("Erro ao inserir venda:", e)
    finally:
        fechar_conexao(conn, cur)


def altera(venda: dict):
    conn, cur = criar_conexao()
    if not conn or not cur:
        return

    try:
        if "id_venda" not in venda or not venda["id_venda"]:
            print("Erro: é necessário informar o 'id_venda' para alterar um registro.")
            return

        campos_validos = {k: v for k, v in venda.items() if v not in (None, "", []) and k != "id_venda"}
        if not campos_validos:
            print("Nenhum campo válido para atualização.")
            return

        set_clause = ", ".join([f"{campo} = :{campo}" for campo in campos_validos.keys()])
        sql = f"UPDATE t_vendas SET {set_clause} WHERE id_venda = :id_venda"
        campos_validos["id_venda"] = venda["id_venda"]

        cur.execute(sql, campos_validos)
        conn.commit()

        if cur.rowcount > 0:
            print(f"Venda {venda['id_venda']} atualizada com sucesso!")
        else:
            print(f"❌ Nenhuma venda encontrada com id {venda['id_venda']}.")

    except oracledb.Error as e:
        print("Erro ao alterar venda:", e)
    finally:
        fechar_conexao(conn, cur)


def recupera_vendas_data(ini: str, fim: str) -> list:
    conn, cur = criar_conexao()
    if not conn or not cur:
        return []

    try:
        sql = """
            SELECT 
                id_venda, 
                nm_comprador, 
                nm_vendedor, 
                TO_CHAR(dt_venda, 'DD-MM-YYYY') AS dt_venda, 
                ds_produto, 
                vl_total, 
                vl_impostos
            FROM t_vendas
            WHERE dt_venda BETWEEN TO_DATE(:ini, 'DD-MM-YYYY') AND TO_DATE(:fim, 'DD-MM-YYYY')
            ORDER BY dt_venda
        """

        cur.execute(sql, {"ini": ini, "fim": fim})
        linhas = cur.fetchall()

        vendas = []
        for linha in linhas:
            venda = {
                "id_venda": linha[0],
                "nm_comprador": linha[1],
                "nm_vendedor": linha[2],
                "dt_venda": linha[3],
                "ds_produto": linha[4],
                "vl_total": linha[5],
                "vl_impostos": linha[6]
            }
            vendas.append(venda)

        return vendas

    except oracledb.Error as e:
        print("Erro ao recuperar vendas:", e)
        return []
    finally:
        fechar_conexao(conn, cur)


def recupera_vendas_comprador(comprador: str) -> list:
    conn, cur = criar_conexao()
    if not conn or not cur:
        return []

    try:
        sql = """
            SELECT 
                id_venda, 
                nm_comprador, 
                nm_vendedor, 
                TO_CHAR(dt_venda, 'DD-MM-YYYY') AS dt_venda, 
                ds_produto, 
                vl_total, 
                vl_impostos
            FROM t_vendas
            WHERE nm_comprador = :comprador
            ORDER BY dt_venda
        """
        cur.execute(sql, {"comprador": comprador})
        linhas = cur.fetchall()

        vendas = []
        for linha in linhas:
            venda = {
                "id_venda": linha[0],
                "nm_comprador": linha[1],
                "nm_vendedor": linha[2],
                "dt_venda": linha[3],
                "ds_produto": linha[4],
                "vl_total": linha[5],
                "vl_impostos": linha[6]
            }
            vendas.append(venda)

        return vendas

    except oracledb.Error as e:
        print("Erro ao recuperar vendas do comprador:", e)
        return []
    finally:
        fechar_conexao(conn, cur)


def recupera_vendas_vendedor(vendedor: str) -> list:
    conn, cur = criar_conexao()
    if not conn or not cur:
        return []

    try:
        sql = """
            SELECT 
                id_venda, 
                nm_comprador, 
                nm_vendedor, 
                TO_CHAR(dt_venda, 'DD-MM-YYYY') AS dt_venda, 
                ds_produto, 
                vl_total, 
                vl_impostos
            FROM t_vendas
            WHERE nm_vendedor = :vendedor
            ORDER BY dt_venda
        """
        cur.execute(sql, {"vendedor": vendedor})
        linhas = cur.fetchall()

        vendas = []
        for linha in linhas:
            venda = {
                "id_venda": linha[0],
                "nm_comprador": linha[1],
                "nm_vendedor": linha[2],
                "dt_venda": linha[3],
                "ds_produto": linha[4],
                "vl_total": linha[5],
                "vl_impostos": linha[6]
            }
            vendas.append(venda)

        return vendas

    except oracledb.Error as e:
        print("Erro ao recuperar vendas do vendedor:", e)
        return []
    finally:
        fechar_conexao(conn, cur)


def relatorio_vendas():
    """Gera um relatório resumido de vendas com totais e estatísticas."""
    conn, cur = criar_conexao()
    if not conn or not cur:
        return

    try:
        print("\n=== RELATÓRIO GERAL DE VENDAS ===")

        # Totais gerais
        sql_totais = """
            SELECT 
                COUNT(*) AS qtd_vendas,
                NVL(SUM(vl_total), 0) AS soma_total,
                NVL(SUM(vl_impostos), 0) AS soma_impostos,
                NVL(AVG(vl_total), 0) AS media_venda
            FROM t_vendas
        """
        cur.execute(sql_totais)
        qtd, total, impostos, media = cur.fetchone()

        print(f"\nTotal de vendas registradas: {qtd}")
        print(f"Soma total de vendas: R$ {total:,.2f}")
        print(f"Total de impostos: R$ {impostos:,.2f}")
        print(f"Média por venda: R$ {media:,.2f}")

        # Vendedor com mais vendas
        sql_vendedor_qtd = """
            SELECT nm_vendedor, COUNT(*) AS total_vendas
            FROM t_vendas
            GROUP BY nm_vendedor
            ORDER BY total_vendas DESC
        """
        cur.execute(sql_vendedor_qtd)
        vendedor_mais_vendas = cur.fetchone()

        if vendedor_mais_vendas:
            print(f"\nVendedor com mais vendas: {vendedor_mais_vendas[0]} "
                  f"({vendedor_mais_vendas[1]} vendas)")
        else:
            print("\nNenhum vendedor encontrado.")

        # Vendedor com maior faturamento
        sql_vendedor_faturamento = """
            SELECT nm_vendedor, SUM(vl_total) AS total_faturado
            FROM t_vendas
            GROUP BY nm_vendedor
            ORDER BY total_faturado DESC
        """
        cur.execute(sql_vendedor_faturamento)
        vendedor_mais_faturou = cur.fetchone()

        if vendedor_mais_faturou:
            print(f"Vendedor que mais faturou: {vendedor_mais_faturou[0]} "
                  f"(R$ {vendedor_mais_faturou[1]:,.2f})")
        else:
            print("Nenhum faturamento encontrado.")

        print("\n=== Fim do Relatório ===\n")

    except oracledb.Error as e:
        print("Erro ao gerar relatório de vendas:", e)
    finally:
        fechar_conexao(conn, cur)


def menu():
    while True:
        print("""
=== MENU DE OPERAÇÕES ===
1 - Cadastrar nova venda
2 - Alterar venda existente
3 - Recuperar vendas por data
4 - Recuperar vendas por comprador          
5 - Recuperar vendas por vendedor
6 - Relatório geral de vendas

0 | Sair
              """)

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
        
        elif opcao == "3":
            print("\n--- Recuperar vendas por intervalo de datas ---")
            ini = input("Data inicial (DD-MM-YYYY): ")
            fim = input("Data final (DD-MM-YYYY): ")

            vendas = recupera_vendas_data(ini, fim)
            if vendas:
                for v in vendas:
                    print(f"ID: {v['id_venda']}, Comprador: {v['nm_comprador']}, "
                          f"Vendedor: {v['nm_vendedor']}, Data: {v['dt_venda']}, "
                          f"Produto: {v['ds_produto']}, Total: {v['vl_total']}, "
                          f"Impostos: {v['vl_impostos']}")
            else:
                print("Nenhuma venda encontrada nesse intervalo.")

        elif opcao == "4":
            print("\n--- Recuperar vendas por comprador ---")
            comprador = input("Nome do comprador: ")

            vendas = recupera_vendas_comprador(comprador)
            if vendas:
                for v in vendas:
                    print(f"ID: {v['id_venda']}, Comprador: {v['nm_comprador']}, "
                        f"Vendedor: {v['nm_vendedor']}, Data: {v['dt_venda']}, "
                        f"Produto: {v['ds_produto']}, Total: {v['vl_total']}, "
                        f"Impostos: {v['vl_impostos']}")
            else:
                print(f"Nenhuma venda encontrada para o comprador {comprador}.")

        elif opcao == "5":
            print("\n--- Recuperar vendas por vendedor ---")
            vendedor = input("Nome do vendedor: ")

            vendas = recupera_vendas_vendedor(vendedor)
            if vendas:
                for v in vendas:
                    print(f"ID: {v['id_venda']}, Comprador: {v['nm_comprador']}, "
                          f"Vendedor: {v['nm_vendedor']}, Data: {v['dt_venda']}, "
                          f"Produto: {v['ds_produto']}, Total: {v['vl_total']}, "
                          f"Impostos: {v['vl_impostos']}")
            else:
                print(f"Nenhuma venda encontrada para o vendedor {vendedor}.")

        elif opcao == "6":
            relatorio_vendas()

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")
        

def verifica_id(id_venda: int) -> bool:
    conn, cur = criar_conexao()
    if not conn:
        return False

    try:
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