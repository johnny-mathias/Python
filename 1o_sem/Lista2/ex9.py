a = float(input("A: "))
b = float(input("B: "))
op = input(f"Operação: ")

if a == 0 or b == 0:
    print("Não é possível dividir por zero!")
else:
    print("deu")
    match op:
        case "+":
            print(f"{a} + {b} = {a+b}")
        case "-":
            print(f"{a} - {b} = {a-b}")
        case "/":
            print(f"{a} / {b} = {a/b}")
        case "*":
            print(f"{a} * {b} = {a*b}")
        case _:
            "Operação inválida!"