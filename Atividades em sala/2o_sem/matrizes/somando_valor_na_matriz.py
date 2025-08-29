#Com While
def aumento_while(matriz, valor):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[i]):
            matriz[i][j] = matriz[i][j] + valor
            j+=1
        i+=1

#Com For/Range
def aumento_for(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = matriz[i][j] + valor

#As matrizes precisam ter a mesma dimensão para ser feita a soma

#[-3, 5, 2]  + [7,  2, 0]   = [4, 7, 2]
#[1,  6, 4]    [9, -2, 3]    [10, 4, 7]

def soma(mat_a, mat_b):
    resp = []
    lin = len(mat_a)
    col = len(mat_b[0])
    i = 0
    while i < lin:
        resp.append([0] * col)
        j = 0
        while j < col:
            resp[i][j] = mat_a[i][j] + mat_b[i][j]
            j+=1
        i+=1
        
    return resp

def soma(mat_a, mat_b):
    resp = []
    lin = len(mat_a)
    col = len(mat_b[0])
    i = 0
    for i in range(lin):
        resp.append([0] * col)
        for j in range(col):
            resp[i][j] = mat_a[i][j] + mat_b[i][j]
        
    return resp