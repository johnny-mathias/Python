n = int(input("Digite um numero inteiro: "))
i = 0
ast = "*"

while n <= 0:
    print("Digite um número inteiro positivo!")
    n = int(input("n = "))

while i < n:
    i+= 1
    print(ast * i)