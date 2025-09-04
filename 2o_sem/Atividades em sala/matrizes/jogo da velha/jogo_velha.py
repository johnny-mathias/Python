import aula0409

def trocaJogador(jogador):
    if jogador == 'x':
        return 'o'
    else:
        return 'x'

tab = []
for i in range(3):
    tab.append([' '] * 3)


player = 'x'

while aula0409.temEspaco(tab) and not aula0409.haGanhador(tab):
    aula0409.imprime(tab)    
    print(f"jogador{player}: ")
    lin = int (input("Linha: "))
    col = int (input("coluna: "))
    if aula0409.joga(tab,lin,col,player) == True:
        player = trocaJogador(player)
    else:
        print('jogada invalida, tente outra posicao')


if aula0409.haGanhador(tab):
    print(f"Parabens,{trocaJogador (player)} venceu!")        

else:
    print("deu velha ")    