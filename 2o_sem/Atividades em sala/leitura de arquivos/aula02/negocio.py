import banco

def importa_partidas(lista: list) -> void:
    for registro in 

def insere_partida(partida: dict):
    tc = partida.get('time_casa')
    tv = partida.get('time_visitante')
    time_casa = banco.recupera_pelo_nome(tc)
    if time_casa == None:
        time_casa = banco.insere_time(tc)
    time_visitante = banco.recupera_pelo_nome(tv)

    if time_visitante == None:
        time_visitante = banco.insere_time(tv)

    if partida['gols_casa'] > partida['gols_visitante']:
        time_visitante['derrota'] = time_visitante['derrota'] + 1
        time_casa['vitoria'] = time_casa['vitoria'] + 1
    elif partida['gols_casa'] < partida['gols_visitante']:
        time_visitante['vitoria'] = time_visitante['vitoria'] + 1
        time_casa['derrota'] = time_casa['derrota'] + 1
    else:
        time_casa['empate'] = time_casa['empate'] + 1
        time_visitante['empate'] = time_visitante['empate'] + 1

    time_visitante['gol_pro'] += partida['gols_visitante']
    time_casa['gol_pro'] += partida['gols_casa']

    time_visitante['gol_sof'] += partida['gols_casa']
    time_casa['gol_sof'] += partida['gols_visitante']


