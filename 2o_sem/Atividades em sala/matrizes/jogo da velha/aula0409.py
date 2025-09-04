matriz = []

def haGanhador(matriz: list) -> bool:
    for t in range(len(matriz)):

        if matriz [t][0] != ' ' and matriz [t][0] == matriz[t][1] and matriz[t][1] == matriz[t][2]:
            return True 
        
    if matriz[0][t] != ' ' and matriz[0][t] == matriz[1][t] and matriz[1][t] == matriz[2][t]:
        return True 
    
    if matriz[0] [0] != ' ' and matriz[0][0] == matriz[1] [1] and matriz[1] [1] == matriz[2] [2]:
        return True 
    
    if matriz[0][2] != ' ' and matriz[0][2] == matriz[1][1] and matriz[1][1] == mat[2][0]:
        return True

def temEspaco(matriz: list) -> bool:
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == ' ':
                return True 
    return False        

def joga(matriz: list, lin: int, col: int, jogador: str) -> bool:
    if matriz [lin][col] != 'x' and matriz [lin][col] != 'o':
        matriz[lin] [col] = jogador
        return True 
    else:
        return False

def imprime(matriz: list):
    for linha in matriz:
        print(linha)

imprime(matriz)        