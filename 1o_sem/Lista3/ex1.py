soma = 0
num = None

while num != 0:
    print("Digite um valor para adicionar\nPressione 0 para finalizar")
    num = int(input("n: "))
    if (num % 2) == 0:
        soma+= num
print(f"\na soma dos pares é: {soma}")   