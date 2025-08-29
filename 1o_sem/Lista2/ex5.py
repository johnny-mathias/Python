dias_uteis = int(input("Dias úteis do mês: "))
horas_trab = int(input("Horas trabalhadas: "))
valor_h = float(input("Valor por hora: R$"))

valor_h_extra = valor_h * 1.5
jornada_minima = dias_uteis * 8

salario = valor_h * jornada_minima
print(f"Salário base: {salario}")

if horas_trab > jornada_minima:
    salario += (horas_trab - jornada_minima) * valor_h_extra
    print(f"Salário com Hora(s) Extra(s): {salario}")
else:
    print(f"Salário: {salario}")