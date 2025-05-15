def menu() -> int:
    print("\nSISTEMA ENQUETE")
    print("1) cadastra pergunta")
    print("2) visualiza perguntas")
    print("3) apaga perguntas")
    print("4) sair")
    return int(input("Opção: "))

#INICIO PROGRAMA (main)
lista = []
opcao = 0
while opcao != 4:
    opcao = menu()

    if opcao == 1:
        print("cadastra pergunta")
        def cadastra_pergunta(lista: list):
            num = int(input("Número: "))
            enun = input("Enunciado: ")
            tipo = input("Tipo: ")
            alternativas = None
            if tipo != 'aberta':
                #coletar as alternativas
                alternativas = []
                i = 1
                aux = input(f"alt {i}: ")
                while aux != "":
                    alternativas.append(aux)
                    i+= 1
                    aux = input(f"alt {i}: ")

                lista.append(num)
                lista.append(enun)
                lista.append(tipo)
                lista.append(alternativa)


            
    elif opcao == 2:
        print(lista)
    elif opcao == 3:
        print("apaga perguntas")
    elif opcao == 4:
        print("programa finalizado...")
    else:
        print("Entrada inválida!")
