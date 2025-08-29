idade = int(input("Idade: "))

if idade < 5:
    print("Idade insuficiente")
elif idade >= 5 and idade <= 7:
    print("Infantil")
elif idade < 11:
    print("Juvenil")
elif idade < 16:
    print("Adolescente")
elif idade < 31:
    print("Adulto")
else:
    print("Senior")