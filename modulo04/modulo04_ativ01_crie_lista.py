def atividade_1():
    print("\n" + "="*40)
    print("      ATIVIDADE 1: LISTA DE COMPRAS")
    print("="*40)
    lista_compras = []

    while True:
        print("\n--- MENU LISTA DE COMPRAS ---")
        print("1 - Adicionar item")
        print("2 - Remover item")
        print("3 - Visualizar lista")
        print("0 - Voltar/Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            item = input("Digite o nome do item a adicionar: ").strip()
            if item:
                lista_compras.append(item)
                print(f"'{item}' foi adicionado à lista!")
        elif opcao == '2':
            item = input("Digite o nome do item a remover: ").strip()
            if item in lista_compras:
                lista_compras.remove(item)
                print(f"'{item}' foi removido da lista!")
            else:
                print("Item não encontrado na lista.")
        elif opcao == '3':
            print("\nSua lista atual:")
            if not lista_compras:
                print("A lista está vazia.")
            else:
                for idx, item in enumerate(lista_compras, start=1):
                    print(f"{idx}. {item}")
        elif opcao == '0':
            break
        else:
            print("Opção inválida! Tente novamente.")

def atividade_2():
    print("\n" + "="*40)
    print("      ATIVIDADE 2: DADOS DO ALUNO")
    print("="*40)
    
    aluno = {
        "nome": "Lucas Silva",
        "idade": 17,
        "notas": [8.5, 9.0, 7.5]
    }

    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']} anos")
    print(f"Notas: {aluno['notas']}")

    media = sum(aluno['notas']) / len(aluno['notas'])
    print(f"Média do Aluno: {media:.2f}")

def atividade_3():
    print("\n" + "="*40)
    print("      ATIVIDADE 3: PARES E ÍMPARES")
    print("="*40)
    
    numeros = [12, 7, 3, 18, 25, 40, 9, 2, 15]
    pares = []
    impares = []

    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    print(f"Lista completa: {numeros}")
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")

def desafio_extra():
    print("\n" + "="*40)
    print("     DESAFIO EXTRA: AGENDA DE CONTATOS")
    print("="*40)
    agenda = {}

    while True:
        print("\n--- MENU AGENDA ---")
        print("1 - Adicionar contato")
        print("2 - Remover contato")
        print("3 - Buscar contato")
        print("4 - Listar todos os contatos")
        print("0 - Voltar/Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do contato: ").strip()
            telefone = input("Número de telefone: ").strip()
            agenda[nome] = telefone
            print(f"Contato '{nome}' adicionado com sucesso!")
        elif opcao == '2':
            nome = input("Nome do contato a remover: ").strip()
            if nome in agenda:
                del agenda[nome]
                print(f"Contato '{nome}' removido!")
            else:
                print("Contato não encontrado.")
        elif opcao == '3':
            nome = input("Nome do contato a buscar: ").strip()
            if nome in agenda:
                print(f"Telefone de {nome}: {agenda[nome]}")
            else:
                print("Contato não encontrado.")
        elif opcao == '4':
            print("\n--- CONTATOS CADASTRADOS ---")
            if not agenda:
                print("Agenda vazia.")
            else:
                for nome, telefone in agenda.items():
                    print(f"Nome: {nome} | Telefone: {telefone}")
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")

def menu_principal():
    while True:
        print("\n" + "="*40)
        print("        PAINEL DE ATIVIDADES")
        print("="*40)
        print("1 - Executar Atividade 1 (Lista de Compras)")
        print("2 - Executar Atividade 2 (Dados do Aluno)")
        print("3 - Executar Atividade 3 (Pares e Ímpares)")
        print("4 - Executar Desafio Extra (Agenda de Contatos)")
        print("0 - Sair do Programa")
        
        escolha = input("\nEscolha qual atividade deseja rodar: ")

        if escolha == '1':
            atividade_1()
        elif escolha == '2':
            atividade_2()
        elif escolha == '3':
            atividade_3()
        elif escolha == '4':
            desafio_extra()
        elif escolha == '0':
            print("\nSaindo do programa... Até mais!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu_principal()