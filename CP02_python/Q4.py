frase = input("Digite uma frase a ser invertida: ")
invertida = ""

i = len(frase) - 1
while i >= 0:
    invertida += frase[i]
    i-= 1

print(f"Frase invertida: {invertida}")