time_a = input("Digite o nome do primeiro time: ")
gols_a = int(input(f"Gols do time {time_a} "))
time_b = input("Digite o nome do segundo time: ")
gols_b = int(input(f"Gols do time {time_b} "))

if gols_a > gols_b:
    print(f"\n{time_a} é o vencedor!")
elif gols_b > gols_a:
    print(f"\n{time_b} é o vencedor!")
else:
    print(f"{time_a} e {time_b} empataram!")