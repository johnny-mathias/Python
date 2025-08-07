ano = int(input("Ano: "))

if ano %400 == 0:
    print("Ano bissexto")
elif ano %100 == 0:
    print("Ano não é bissexto")
elif ano %4 == 0:
    print("Ano bissexto")
else:
    print("Ano não é bissexto")