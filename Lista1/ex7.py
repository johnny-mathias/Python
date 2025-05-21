num = int(input("Digite um numero de 0 a 99: "))

dezena = (num // 10) * 10
unidade = num % 10

print(f"dezena: {dezena}\nunidade: {unidade}")