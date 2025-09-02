import bisect

caixa_de_mensagens: list[dict[str, str]] = []

#1. a)
def mail_to_dictionary(assunto, destinatario, remetente, conteudo):
    mensagem = {
    'assunto': assunto,
    'destinatario': destinatario,
    'remetente': remetente,
    'conteudo': conteudo
    }

    caixa_de_mensagens.append(mensagem)


#b) 20 Emails/Mensagens
mail_to_dictionary("Reunião", "Maria", "João", "Confirmação da reunião amanhã.")
mail_to_dictionary("Lembrete", "Equipe", "RH", "Entregar documentos até sexta.")
mail_to_dictionary("Aviso", "Carlos", "Diretoria", "Reunião de alinhamento às 14h.")
mail_to_dictionary("Convite", "Ana", "Pedro", "Você está convidada para a festa de sábado.")
mail_to_dictionary("Cobranca", "Empresa X", "Financeiro", "Fatura em aberto com vencimento hoje.")
mail_to_dictionary("Confirmação", "Lucas", "Eventos", "Confirmação de presença registrada.")
mail_to_dictionary("Parabéns", "Fernanda", "Equipe de RH", "Feliz aniversário, muitas felicidades!")
mail_to_dictionary("Atualização", "Tiago", "Suporte", "Sistema ficará fora do ar às 22h.")
mail_to_dictionary("Resultado", "Alunos", "Professor", "Notas da prova já estão disponíveis.")
mail_to_dictionary("Entrega", "Cliente A", "Logística", "O pedido foi entregue com sucesso.")
mail_to_dictionary("Boletim", "Pais", "Escola", "Segue o boletim do 2º bimestre.")
mail_to_dictionary("Notificação", "Juliana", "Banco XYZ", "Compra suspeita detectada no cartão.")
mail_to_dictionary("Oferta", "Marcos", "Loja Online", "Desconto especial válido até amanhã.")
mail_to_dictionary("Relatório", "Gerente", "Equipe de Vendas", "Relatório mensal anexado.")
mail_to_dictionary("Feedback", "Fornecedor", "Compras", "O material entregue está em conformidade.")
mail_to_dictionary("Chamado", "Suporte", "Funcionário José", "Computador não liga desde ontem.")
mail_to_dictionary("Orientação", "Estagiário", "Supervisor", "Favor revisar os documentos antes de enviar.")
mail_to_dictionary("Agradecimento", "Cliente B", "Atendimento", "Obrigado pela rápida resolução do problema.")
mail_to_dictionary("Suspensão", "Aluno Pedro", "Coordenação", "Você está suspenso por 2 dias.")
mail_to_dictionary("Alerta", "Segurança", "Administração", "Movimentação suspeita detectada no prédio.")



#2. Ordenando mensagens por destinatário, em ordem alfabética
def sorting_by_destinatary():
    caixa_de_mensagens_ordenada = sorted(caixa_de_mensagens, key=lambda msg: msg['destinatario'])
    return caixa_de_mensagens_ordenada

#3. Busca binaria sobre a lista
def binary_search(destinatario: str):
    lista_ordenada = sorting_by_destinatary()
    destinatarios = [msg['destinatario'] for msg in lista_ordenada]
    
    index = bisect.bisect_left(destinatarios, destinatario)
    resultados = []

    while index < len(destinatarios) and destinatarios[index] == destinatario:
        resultados.append(lista_ordenada[index])
        index += 1

    if resultados:
        return resultados
    else:
        return None

    
#4. Menu
def menu():
    while True:
        opcao = input('''
=== MENU DE MENSAGENS ===

1 - Cadastrar nova mensagem
2 - Exibir Caixa de Mensagens
3 - Exibir Caixa de Mensagens por destinatário
4 - Buscar mensagem por destinatário
0 - Sair

Escolha uma opção: ''')


        # Cadastrar nova mensagem
        if opcao == "1":
            assunto = input("Assunto: ")
            destinatario = input("Destinatário: ")
            remetente = input("Remetente: ")
            conteudo = input("Conteúdo: ")
            mail_to_dictionary(assunto, destinatario, remetente, conteudo)
            print("Mensagem cadastrada com sucesso!")

        # Exibir Caixa de Mensagens
        elif opcao == "2":
            exibir_mensagens()
        # Ordenar Caixa de Mensagens
        elif opcao == "3":
            exibir_mensagens_ordenadas()

        # Buscar mensagem por destinatário
        elif opcao == "4":
            destinatario_busca = input("Digite o destinatário que deseja buscar: ")
            mensagens = binary_search(destinatario_busca)  # ou binary_search_all
            
            if mensagens:  # se não for None
                print("\nMensagens encontradas:")
                for i, msg in enumerate(mensagens, start=1):
                    print(f"\nMENSAGEM ({i}):")
                    for chave, valor in msg.items():
                        print(f"{chave}: {valor}")
            else:
                print("Destinatário não encontrado.")

        elif opcao == "0":
            print("Saindo do menu...")
            break

        else:
            print("Opção inválida. Tente novamente.")


#Coisas a mais porque sou teimoso/curioso:
def exibir_mensagens():
    print("\n=== Caixa de Mensagens ===")
    for i, msg in enumerate(caixa_de_mensagens, start=1):
        print(f"\nMENSAGEM ({i}):")
        for chave, valor in msg.items():
            print(f"  {chave}: {valor}")

def exibir_mensagens_ordenadas():
    caixa_de_mensagens_ordenada = sorting_by_destinatary()

    print("\n=== Caixa de Mensagens ===")
    for i, msg in enumerate(caixa_de_mensagens_ordenada, start=1):
        print(f"\nMENSAGEM ({i}):")
        for chave, valor in msg.items():
            print(f"  {chave}: {valor}")

# Executa o menu
menu()