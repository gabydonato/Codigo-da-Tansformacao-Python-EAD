# Sistema de Agenda de Contatos usando dicionários

agenda = {}

while True:
    print("\n=== AGENDA DE CONTATOS ===")
    print("1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Remover contato")
    print("4 - Mostrar todos os contatos")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do contato: ")
        telefone = input("Telefone: ")
        agenda[nome] = telefone
        print("Contato adicionado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome para buscar: ")
        if nome in agenda:
            print(f"Telefone de {nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")

    elif opcao == "3":
        nome = input("Digite o nome para remover: ")
        if nome in agenda:
            del agenda[nome]
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado.")

    elif opcao == "4":
        if agenda:
            print("\nLista de contatos:")
            for nome, telefone in agenda.items():
                print(f"{nome}: {telefone}")
        else:
            print("A agenda está vazia.")

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")