# Dados uma lista de números inteiros e um inteiro x, escreva um algoritmo que verifica se
# existem 2 elementos do conjunto cuja soma seja igual a x. Por exemplo: dado x = 11 e a
# lista abaixo:

lista = [2, 5, -7, 9, 3, 10, 15, 6]
x = 11

def repetido(x, lista) -> int:
    for i in range(len(lista)):
        if lista[i] == x:
            soma += 1
        