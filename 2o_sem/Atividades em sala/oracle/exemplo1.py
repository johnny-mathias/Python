import oracledb

#conectando ao oracle
conn = oracledb.connect(user="rm566516", password="210806", dsn="oracle,fiap.com.br/orcl")

print(conn.version)

#abrir um cursor para efetuar as operações (Statement/PreparedStatement)

cursor = conn.cursor()
sql = "SELECT * FROM T_RHSTU_PACIENTE"
#executando uma consulta
cursor.execute(sql)

#registrando ddaods da consulta e imprimindo na tela
registros = cursor.fetchall()
for info in registros:
    print(info)

#fechando arquivdos abertos
cursor.close()
conn.close()