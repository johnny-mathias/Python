a_vista = float(input("Valor à vista: R$"))
parcela = float(input("Valor de cada parcela: R$"))

desconto = a_vista/parcela*10 - 100
print("Desconto: ", desconto, "%")