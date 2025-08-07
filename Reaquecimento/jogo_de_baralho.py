# Emparelhamento máximo em gráficos bipartidos

cartas, i, n = 0, 0, 13

while cartas < 52:
    while i < n:
        print(f"C{i} = ({i}, Espadas)")  #espadas
        i+=1
        cartas+=1
    i=0
    n=0
    while i < n:
        print(f"C{i} = ({i}, Copas)")  #copas
        i+=1
        cartas+=1
    i=0
    n=0
    while i < n:
        print(f"C{i} = ({i}, Ouros)")  #ouros
        i+=1
        cartas+=1
    i=0
    n=0
    while i < n:
        print(f"C{i} = ({i}, Paus)")  #paus
        i+=1
        cartas+=1