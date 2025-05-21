n = int(input("Digite a quantidade de números: "))

soma = 0
menor = 0

for i in range(n):
    numero = float(input(f"Digite o {i+1}º número: "))
    
    if numero > 50:
        soma += numero
    
    if numero < 100:
        menor += 1

print(f"Soma dos números maiores que 50: {soma}")
print(f"Quantidade de números menores que 100: {menor}")
