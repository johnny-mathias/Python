def organiza(lista: list):
    pos = len(lista)
    aux = lista[pos]

    while lista[pos-1] > aux:
        lista[pos] = lista[pos-1]
        pos -= 1

    lista[pos] = aux

if __name__ == "__main__":


    lst = [3, 5, 9, 17, 55, 78, 0]
    