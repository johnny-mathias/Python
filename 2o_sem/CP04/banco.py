import oracledb

#  Crie o modulo banco.py com as funçoes abaixo:

def inclui(venda: dict):
    conn = oracledb.connect(user="rm566516", password="210806", dsn="oracle,fiap.com.br/orcl")

    print(conn.version)

    cursor = conn.cursor()
    insert = "INSERT INTO t_vendas (id_venda, nm_comprador, nm_vendedor, dt_venda, ds_produto, vl_total, vl_impostos) "

    venda = {
        "id_venda": "sq_t_vendas.NEXTVAL", 
        "nm_comprador": "Johnny", 
        "nm_vendedor": "Luisa", 
        "dt_venda": "TO_DATE('10-10-2025', 'DD-MM-YYYY')", 
        "ds_produto": "Churros sabor chocolate",
        "vl_total": 2000,
        "vl_impostos": 300
        }

    cursor.execute(insert)

    #registrando ddaods da consulta e imprimindo na tela
    registros = cursor.fetchall()
    for venda in registros:
        print(venda)

    #fechando arquivos abertos
    cursor.close()
    conn.close()


# • (1.0) def altera(venda: dict)
# • (1.5) def recupera_vendas_data(ini, fim)-> list
# • (1.5) def recupera_vendas_comprador(vendedor: str)-> list
# • (2.0) def relatorio_vendas()




if __name__ == "__main__":
    pass