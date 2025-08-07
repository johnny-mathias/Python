n = int(input("Digite o valor de N: "))
i, negativo, positivo = 0, 0, 0
while i < n:
    sequencia = float(input(f"Valor {i+1}: "))
    if sequencia < 0:
        negativo += 1
    else:
        positivo += 1
    i+= 1
print(f"Positivos: {positivo}")
print(f"Negativos: {negativo}")