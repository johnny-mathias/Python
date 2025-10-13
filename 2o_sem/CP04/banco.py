import oracledb
import datetime

def inclui(venda: dict):
    try:
        campos_obrigatorios = [
            "nm_comprador", "nm_vendedor", "dt_venda",
            "ds_produto", "vl_total", "vl_impostos"
        ]

        for campo in campos_obrigatorios:
            if campo not in venda or venda[campo] in (None, "", []):
                print(f"Erro: o campo '{campo}' é obrigatório e não pode estar vazio.")
                return 

        conn = oracledb.connect(
            user="rm566516", 
            password="210806", 
            dsn="oracle.fiap.com.br/orcl"
        )
        print("Conectado na versão: ", conn.version)
        
        cursor = conn.cursor()
        
        insert = '''
        INSERT INTO t_vendas 
            (nm_comprador, nm_vendedor, dt_venda, ds_produto, vl_total, vl_impostos)
        VALUES 
            (:nm_comprador, :nm_vendedor, :dt_venda, :ds_produto, :vl_total, :vl_impostos)
        '''
        
        cursor.execute(insert, venda)
        conn.commit()
        
        print("Venda inserida com sucesso!")

    except oracledb.Error as e:
        print("Erro ao inserir venda:", e)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
        print("Conexão finalizada.")


if __name__ == "__main__":
    inclui({
        "nm_comprador": "Johnny",
        "nm_vendedor": "Luisa",
        "dt_venda": datetime.date.today(),
        "ds_produto": "Mouse Gamer",
        "vl_total": 150.00,
        "vl_impostos": 22.50
    })
