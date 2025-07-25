distancia = int(input("Distância (m): "))
tempo = float(input("Tempo (s): "))

ms = distancia/tempo
km = ms * 3.6

msa = round(ms, 2)
kma = round(km, 2)

print(f"Velocidade:\n{msa}m/s     {kma}Km/h")