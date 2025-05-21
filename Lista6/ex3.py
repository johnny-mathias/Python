tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

def maior_valor(entrada):
    maior = entrada[0]
    for num in entrada:
        if num > maior:
            maior = num
    return maior

print(f"Maior valor: {maior_valor(tuple)}")