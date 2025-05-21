n = int(input("Digite o numero da sequencia desejado: "))
i = 1
a = 1
b = 1

while i < n: 
    b = b+a
    print(b)
    a = -a+b
    print(a)
    i += 1

print(f"O {n}º número da sequência é: {a}")