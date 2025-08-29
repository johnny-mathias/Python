dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

bissexto = bool

if dia < 1 or dia > 31:
    print("Coloque um dia entre 1 e 31!")
if mes < 1 or mes > 12:
    print("Coloque um mês entre 1 e 12!")
elif mes == 2 and bissexto == False:
    if dia > 28:
        print("Fevereiro tem 28 dias! Insira um dia válido!")
    else:
        print("O dia é válido.")
elif mes == 2 and bissexto == True:
    if dia > 29:
        print("Fevereiro tem 29 dias! Insira um dia válido!")
    else:
        print("O dia é válido.")

elif mes != 1 or 3 or 5 or 6 or 8 or 10 or 12:
    if dia == 31:
        print("Esse mês tem 30 dias! Insira um dia válido!")
    else:
        print("O dia é válido.")
else:
    print("O dia é válido.")

if ano %400 == 0:
    bissexto = True
elif ano %100 == 0:
    bissexto = False
elif ano %4 == 0:
    bissexto = True
else:
    bissexto = False