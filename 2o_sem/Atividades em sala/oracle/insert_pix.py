import oracledb

#conectando ao oracle
conn = oracledb.connect(user="rm566516", password="210806", dsn="oracle,fiap.com.br/orcl")

print(conn.version)

#abrir um cursor para efetuar as operações (Statement/PreparedStatement)

cursor = conn.cursor()

ins = "INSERT INTO t_pix(chave, nome, banco, agencia, conta)" \
"VALUES (:chave, :nome, :banco, :agencia, :conta)"

info = {"chave": "(11) 42994242", "nome": "Frederico Tavares", "banco": "NuBank", "agencia": "2439", "conta": "634289-8"}

#registrando ddaods da consulta e imprimindo na tela
cursor.execute(ins, info)
conn.commit()

#fechando arquivdos abertos
cursor.close()
conn.close()