salario_anterior = float(input("Salário antes do aumento: R$"))
salario_depois = float(input("Salário depois do aumento: R$"))

percentual = salario_depois/salario_anterior * 100 - 100
percentual_a = round(percentual, 2)

print(f"Acréscimo: {percentual_a}%")