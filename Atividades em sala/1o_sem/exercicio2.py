num_a = int(input("Digite um numero: "))
num_b = int(input("Digite outro numero: "))

if num_a > num_b:
    print(f"\n{num_a} é maior que {num_b}")
elif num_b > num_a:
    print(f"\n{num_b} é maior que {num_a}")
else:
    print(f"{num_a} e {num_b} possuem mesmo valor")