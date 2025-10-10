import random

times = [
    'Atlético-MG', 'Bahia', 'Botafogo', 'Bragantino', 'Ceará',
    'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Fortaleza',
    'Grêmio', 'Internacional', 'Juventude', 'Mirassol', 'Palmeiras',
    'Santos', 'São Paulo', 'Sport', 'Vasco', 'Vitória'
]

with open("partidas.txt", mode="w", encoding='utf8') as archive:
    for j in range(len(times)):
        for i in range(j + 1, len(times)):
            gol_visitante = random.randint(0, 6)
            gol_casa = random.randint(0, 6)
            partida = (f"{times[i]}: {gol_casa} X {times[j]}: {gol_visitante}\n")
            archive.write(partida)