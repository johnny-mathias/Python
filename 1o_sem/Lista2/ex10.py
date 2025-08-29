from math import sqrt

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b**2 - 4*a*c

if a == 0:
    print("\"a\" não pode ser igual a zero!")
else:
    if delta < 0:
        print("A equação não possui raízes reais")
    elif delta == 0:
        x = -b/2*a
        print(f"Raíz única: {x}")
    else:
        x1 = (-b + sqrt(delta))/(2*a)
        x2 = (-b - sqrt(delta))/(2*a)

        print(f"x1 = {x1}, x2 = {x2}")