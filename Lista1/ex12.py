rm = int(input("RM: "))
if rm < 99999:
    print("RM inválido!")
else:
    n = rm//100000
    soma = n
    rm -= n * 100000
    print(soma)

    n = rm//10000
    soma += n
    rm -= n * 10000
    print(soma)

    n = rm//1000
    soma += n
    rm -= n * 1000
    print(soma)

    n = rm//100
    soma += n
    rm -= n * 100
    print(soma)

    n = rm//10
    soma += n
    rm -= n * 10
    print(soma)

    n = rm
    soma += n
    rm -= n
    print(soma)