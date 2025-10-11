import oracledb
import datetime

def inclui(venda: dict):
    conn = oracledb.connect(
        user="rm566516", 
        password="210806", 
        dsn="oracle.fiap.com.br/orcl"
    )
    print("Conectado na versão:", conn.version)
    
    cursor = conn.cursor()
    
    insert = """
    INSERT INTO t_vendas 
        (id_venda, nm_comprador, nm_vendedor, dt_venda, ds_produto, vl_total, vl_impostos)
    VALUES 
        (sq_t_vendas.NEXTVAL, :nm_comprador, :nm_vendedor, :dt_venda, :ds_produto, :vl_total, :vl_impostos)
    """
    
    # Se não for passado, você pode definir aqui
    if not venda:
        venda = {
            "nm_comprador": "Johnny",
            "nm_vendedor": "Luisa",
            "dt_venda": datetime.date.today(),
            "ds_produto": "Churros sabor chocolate",
            "vl_total": 2000,
            "vl_impostos": 300
        }
    
    cursor.execute(insert, venda)
    conn.commit()
    
    print("Venda inserida com sucesso!")
    
    cursor.close()
    conn.close()


if __name__ == "__main__":
    inclui({})
