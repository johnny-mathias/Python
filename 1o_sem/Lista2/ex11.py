preco = float(input("Preço: R$"))
pagamento = str(input('''Escolha uma condição de pagamento:
                      
                      Código  | Condição de pagamento
                      1       | A vista (dinheiro), 10%% de desconto
                      2       | A vista no cartão de crédito, 5%% de desconto
                      3       | Em 2x, sem juros
                      4       | Em 4x, 7%% de juros
                      '''))

match pagamento:
    case "1":
        subtotal = preco * 0.9
        print(f"Valor a pagar: R${subtotal}")
    case "2":
        subtotal = preco * 0.95
        print(f"Valor a pagar: R${subtotal}")
    case "3":
        print(f"Parcelas de R${preco/2}, Total: R${preco}")
    case "4":
        subtotal = preco * 1.07
        print(f"Parcelas de R${preco/2}, Total: R${subtotal}")
    case _:
        print("Código inválido!")