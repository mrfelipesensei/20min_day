def cadastrar_tarefa():
    nome = input("Digite o nome da Tarefa: ").strip()
    print(f"\nDefina a Prioridade de {nome}:")
    print("1 - Alta")
    print("2 - Média")
    print("3 - Baixa")

    prioridade = input("Digite sua opção: ")

    if prioridade == "1":
        prioridade = "Alta"
        tarefas_dia[nome] = prioridade
    elif prioridade == "2":
        prioridade = "Média"
        tarefas_dia[nome] = prioridade
    elif prioridade == "3":
        prioridade = "Baixa"
        tarefas_dia[nome] = prioridade
    else:
        print("Opção inválida, tente novamente.")

def remover_tarefa():
    nome = input("Digite o nome da Tarefa a ser removida: ")

    if nome in tarefas_dia:
        del tarefas_dia[nome]
        print(f"A Tarefa {nome} foi removida com sucesso.")
    else:
        print(f"Tarefa {nome} ainda não foi cadastrada.")

def alterar_prioridade():
    nome = input("Digite o nome da Tarefa que deseja alterar sua Prioridade: ")

    if nome in tarefas_dia:
        print(f"\nDefina a Nova Prioridade de {nome}:")
        print("1 - Alta")
        print("2 - Média")
        print("3 - Baixa")

        nova_prioridade = input("Digite sua opção: ")
        
        if nova_prioridade == "1":
            nova_prioridade = "Alta"
            tarefas_dia[nome] = nova_prioridade
        elif nova_prioridade == "2":
            nova_prioridade = "Média"
            tarefas_dia[nome] = nova_prioridade
        elif nova_prioridade == "3":
            tarefas_dia[nome] = "Baixa"

def mostrar_tarefas():
    print("\n--- TAREFAS CADASTRADAS ---")
    if not tarefas_dia:
        print("Nenhuma tarefa cadastrada no momento.")
    else:
        for nome, dados, in tarefas_dia.items():
            prioridade = dados[0]
            print(f"Tarefa: {nome} | Prioridade: {prioridade}")

#Criando o dicionário de tarefas vazio
tarefas_dia = {}

#Enquanto o programa não for encerrado
while True:
    print("\n1 - Cadastrar Tarefa")
    print("2 - Alterar Prioridade")
    print("3 - Remover Tarefa")
    print("4 - Visualizar tarefas")
    print("5 - Sair do programa.")

    escolha = input("Digite sua opção: ")

    if escolha == "1":
        cadastrar_tarefa()
        
    elif escolha == "2":
        alterar_prioridade()
        
    elif escolha == "3":
        remover_tarefa()

    elif escolha == "4":
        mostrar_tarefas()
        
    elif escolha == "5":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida, tente novamente.")
