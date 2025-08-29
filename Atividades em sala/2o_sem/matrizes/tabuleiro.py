tabuleiro = []
i = 0
while i < 3:
    tabuleiro.append([''] * 3)
    i+=1

tabuleiro[0][0] = 'x'
tabuleiro[1][1] = 'o'
tabuleiro[2][2] = 'x'
for linha in tabuleiro:
    print(linha)