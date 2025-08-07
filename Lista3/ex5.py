n = int(input("n: "))

if n <= 0:
    print("Digite um valor positivo!")
else:
    i = 1
    while i <= n:
        if n%i == 0:
            print(i)
        i+= 1