n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}")
elif n1 < n2:
    print(f"{n2} é maior que {n1}")
else:
    print(f"{n1} e {n2} são iguais")