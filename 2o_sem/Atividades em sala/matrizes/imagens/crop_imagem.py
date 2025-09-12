import Imagem
 
mat = Imagem.getMatrizImagemCinza("dominio.png")
 
linhas = len(mat)
colunas = len(mat[0])
print (f'{linhas} X {colunas}')
 
pedra = []
 
for i in range (40):
    pedra.append([0] * 70)
 
for i in range(40):
    for j in range(70):
        pedra[i][j] = mat [i + 10][j + 12]