#USANDO READ

with open('index.html', mode='r') as arquivo:
    tudo = arquivo.read()

print(tudo.replace("<p>", "<h1>"))

with open('index.html', mode='r') as arq:
    lista = arq.readlines()

print(lista)

with open('index.html', mode='r') as file:
    info = file.readline()
    info