x = 60
lista = [100, 80, 10, 30, 40, 50, 70, 60, 20, 90]

def busca(lista: list, x: float) -> int:
    i = 0
    while i < len(lista) or lista[i] != x:
        i+= 1

    if i == len(lista):
        return -1
    else:
        return i

def busca_for(lista, x) -> int:
    for i in range(len(lista)):
        if lista [i] == x:
            return i
    return -1

def busca_binaria(lista: list, x: float) -> int:
    i = 0   #i de inicio
    lista_ordenada =sorted(lista)
    fim = (len(lista_ordenada)-1)
    while i <= fim:
        meio = (i + fim)//2
        print(meio)
        if lista_ordenada[meio] > x:
            fim = meio -1
        elif lista_ordenada[meio] > x:
            fim = meio +1
        else:
            return meio
    return -1

def saida():
    print()

busca_binaria(lista, x)