if __name__ == "__main__":
    campeonato = {}
    campeonato ['Corinthians'] = 23
    campeonato ['Palmeiras'] = 21
    campeonato ['São Paulo'] = 30
    campeonato ['Flamengo'] = 18

    print(campeonato)

    campeonato['Santos'] = 19

    for time in campeonato.keys():
        print(f'{time} pts: {campeonato[time]}')


    #Crie um outro dicionario a partir do dicionario acima para armazenar uma lista o nome do time e os pontos ao inves de apenas os pontos
    brasileirao = {}
    brasileirao ['Corinthians'] = ['Corinthians', 23]
    brasileirao ['Palmeiras'] = ["Palmeiras", 21]
    brasileirao ['São Paulo'] = ["São Paulo", 30]
    brasileirao ['Flamengo'] = ["Flamengo", 18]

    for time in brasileirao.keys():
        print(f"{time} pts: {brasileirao[time]}")
        