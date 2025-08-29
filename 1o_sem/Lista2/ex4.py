time_a = str(input("Time A: "))
time_b = str(input("Time B: "))

gols_a = int(input(f"Gols do {time_a}: "))
gols_b = int(input(f"Gols do {time_b}: "))

if gols_a > gols_b:
    print(f"{time_a} ganhou!")
elif gols_b > gols_a:
    print(f"{time_b} ganhou!")
else:
    print(f"{time_a} e {time_b} empataram!")