def cadastrar_tarefa():
    nome = input("Digite o nome da Tarefa: ").strip()
    print(f"\n Defina a Prioridade de {nome}:")
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
        prioridade == "Baixa"
        tarefas_dia[nome] = prioridade
    else:
        print("Opção inválida, tente novamente.")

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
    print("1 - Cadastrar Tarefa")
    print("2 - Alterar Prioridade")
    print("3 - Remover Tarefa")
    print("4 - Visualizar tarefas")

    escolha = input("Digite sua opção: ")

    if escolha == "1":
        cadastrar_tarefa()
        
    #elif escolha == "2":
        #Lógica de alterar prioridade da tarefa
        
    #elif escolha == "3":
        

    elif escolha == "4":
        mostrar_tarefas()
        
    elif escolha == "5":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida, tente novamente.")
