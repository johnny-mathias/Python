x = int(input("Digite o valor da cédula: "))
a = int(input("Digite o valor de uma moeda: "))
b = int(input("Digite o valor da outra moeda: "))

possivel = False

for qtd_a in range(x // a + 1):
    resto = x - (qtd_a * a)
    
    if resto % b == 0:
        qtd_b = resto // b
        print(f"Possível: {qtd_a} moeda(s) de {a} e {qtd_b} moeda(s) de {b}")
        possivel = True
        break

if not possivel:
    print("Não é possível fazer a troca")