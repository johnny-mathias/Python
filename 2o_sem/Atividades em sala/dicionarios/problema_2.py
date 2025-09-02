# maneira mais simplificada

# def inverter_dicionario(dicionario):
#     return {valor: chave for chave, valor in dicionario.items()}

#valor: chave                   // Substitui o valor para chave e chave para valor
#for chave, valor in <condição> // Faz um loop com a quantidade da condição
#dicionario.items()             // Condição que o for recebe, com a quantidade de itens

#maneira tradicional
def inverter_dicionario(dicionario):
    invertido = {}                 # cria um dicionário vazio
    for chave, valor in dicionario.items():   # percorre cada par (chave, valor)
        invertido[valor] = chave   # no novo dicionário, o valor vira chave
    return invertido          #devolve o valor invertido

ingles_portugues = {
    "apple": "maçã",
    "dog": "cachorro",
    "house": "casa",
    "car": "carro"
}

portugues_ingles = inverter_dicionario(ingles_portugues)

print(portugues_ingles)