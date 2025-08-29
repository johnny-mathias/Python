matriz = []

linha = 0
for linha in range(4):
    matriz.append([0] * 5)
    
x = 1   
coluna = 0
linha = 0
while linha < 4:
    while coluna < 5:
        matriz[linha][coluna] = x
        x+=1
        coluna+=1
    coluna = 0
    linha+=1
    
#imprimindo a matriz
for linha in matriz:
    print(linha)