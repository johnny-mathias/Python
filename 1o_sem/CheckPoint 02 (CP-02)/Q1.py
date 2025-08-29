n = int(input("Digite o número de produtos que terão o preço aumentado: "))
i = 0

if n > 0:

    while i < n:
        i+= 1
        atual = float(input(f"{i}º Produto |   Preço atual: "))
        novo = float(input(f"            Preço ajustado: "))

        por = ((novo - atual) / (atual))*100

        if i == 1:
            maior_p = por
            maior_v = novo
            maior_pn = i
            maior_vn = i
        else:
            if por > maior_p:
                maior_p = por
                maior_pn = i
            if novo > maior_v:
                maior_v = novo
                maior_vn = i

    print(f"O {maior_vn}º produto é o mais caro: R${maior_v}")
    print(f"O {maior_pn}º produto é o que sofreu maior aumento: {maior_p}%")          
else:
    print("Insira um número inteiro positivo!")