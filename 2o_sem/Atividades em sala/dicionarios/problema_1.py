frase = "Socorram-me subi no  onibus em Marrocos"
frase = frase.lower()

dic = {}
for letra in frase:
    if letra != ' ':
        if letra in dic.keys():
            dic[letra] = dic[letra] + 1
        else:
            dic[letra] = 1

print(dic)