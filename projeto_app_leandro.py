'''

CRUD



'''

while True:

    print("\n== GESTÃO DO SALÃO ===")
    print("1. Agendar Cliente")
    print("2. Ver Agenda")
    print("3. Mudar Serviço")
    print("4. Cancelar Agendamento")
    print("5. Relatorio de Serviços")
    print("7. Tabela de Preços")
    print("8. Simulador de Desconto")
    print("0. Sair")

    escolha = input("\nEscolha uma opção: ")

    if escolha == '1':
        print("\n--- Cadastrar cliente ---")
        
        nome_cliente = input("Digite o nome do Cliente: ")
        cliente_telefone = input("Digite o telefone do cliente: ")
        email_cliente = input("Digite o e-mail do cliente: ")
        data_agendamento = input("Digite a data (ex: 25/10): ")
        observacao = input("Alguma observação especial? ")

        print("Salvando dados...")
        print("Cadastro concluido com sucesso\n")

    elif escolha == '2':
        print("\n--- Ver Agenda ---")
        print("Mostrar os horarios cadastrados...")
        
        horario_cliente = input("Escolha um horario: ")
        periodo_cliente = input("Escolha o periodo: ")

        print("Horario Cadastrado com sucesso\n")

    elif escolha == '3':
        print("\n--- Alterar serviço do cliente ---")
        
        nome_busca = input("Digite o nome do cliente: ")
        servico_cliente = input("Digite o novo serviço (corte / barba / Corte + Barba): ")
        
        print("Alterando registro de", nome_busca, "...")
        print("Serviço alterado com sucesso!")

    elif escolha == '4':
        print("\n--- Cancelar Agendamento ---")
        
        cliente = input("Digite o nome do cliente que deseja cancelar: ")
        horario = input("Digite o horário do agendamento: ")
        
        print("Removendo do sistema...")
        print("Cancelamento com sucesso!")

    elif escolha == '5':
        print("\n--- Relatorio de Serviços ---")
        print("Calculando faturamento do dia...")
        print("Serviços realizados: 0")
        print("Total em caixa: R$ 0,00")
        print("--------------------------")

    elif escolha == '7':
        print("\n--- TABELA DE VALORES ---")
        print("1. Corte Social .......... R$ 35,00")
        print("2. Degradê Moderno ....... R$ 45,00")
        print("3. Barba Simples ......... R$ 25,00")
        print("4. Combo (Corte+Barba) ... R$ 60,00")
        print("5. Sobrancelha ........... R$ 15,00")
        print("--------------------------")
        input("Pressione ENTER para voltar ao menu...")

    elif escolha == '8':
        print("\n--- SIMULADOR DE DESCONTO (FIDELIDADE) ---")
        valor_total = input("Digite o valor total do serviço: R$ ")
        
        valor_numero = float(valor_total)
        
        print("Calculando 10% de desconto para cliente fiel...")
        desconto = valor_numero * 0.10
        valor_final = valor_numero - desconto
        
        print("--------------------------")
        print("Desconto: R$", desconto)
        print("Valor com Desconto: R$", valor_final)
        print("--------------------------")

    elif escolha == '0':
        print("\nSaindo do sistema...")
        print("Até logo!")
        break

    else:
        print("\n[AVISO] Opção inválida! Tente novamente.")