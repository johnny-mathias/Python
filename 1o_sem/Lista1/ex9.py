preco = float(input("Preço: R$"))
percentual = float(input("Desconto (%): "))

desconto = preco * (100-percentual)/100
desconto_a = round(desconto, 2)

print(f"O novo preço é: R${desconto_a}")