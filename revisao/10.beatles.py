from datetime import datetime


discos = {}

def adicionar_disco():

    while True:
        nome = input("Digite o Nome do Disco: ").strip()

        if not nome:
            print("ERRO - O nome não pode estar em branco.")
            continue

        elif not all(c.isalpha() or c.isspace() for c in nome):
            print("ERRO - O nome deve conter apenas letras e espaços.")
            continue
        else:
            break

    while True:

        entrada = input("Digite uma data (dd/mm/aaaa): ")

        try:
            data = datetime.strptime(entrada, "%d/%m/%Y")
            print("Data válida: ", data.strftime("%d/%m/%Y"))
            break
        except ValueError:
            print("Data inválida! Use o formato dd/mm/aaaa.")
            continue
    
    while True:

        gravadora = input("Digite o nome da Gravadora: ")

        if not gravadora:
            print("ERRO - A Gravadora não pode estar em branco.")
            continue

        elif not all(c.isalpha() or c.isspace() for c in gravadora):
            print("ERRO - A Gravadora deve conter apenas letras e espaços.")
            continue
        
        else:
            break

    while True:
        try:
            num_mus = int(input("Quantas músicas o disco possui? "))
            if num_mus > 0:
                break
            else:
                print("ERRO - O número de músicas deve ser maior que zero.")

        except ValueError:
            print("ERRO - Por favor, digite um número válido.")

    musicas = []
    print("\n--- Digite o título das músicas ---")

    for i in range(num_mus):
        while True:
            titulo = input(f"Digite o título da Música {i + 1}: ").strip()

            if not titulo:
                print("ERRO - O título não pode estar em branco.")
            elif not all(c.isalpha() or c.isspace() for c in titulo): #Corrigir essa validação
                print("ERRO - O título deve conter apenas letras, números e espaços.")
            else:
                musicas.append({"titulo":titulo})
                break #Próxima música

    
    discos[nome] = entrada, gravadora, musicas
    print(f"\n Disco {nome} adicionado com sucesso.")
    

while True:
    print("\n--- DISCOGRAFIA BEATLES ---")
    print("1 - Adicionar Disco")
    print("2 - Listar Discos")
    print("3 - Buscar por Ano")
    print("4 - Buscar por Música")
    print("5 - Alterar Dados")
    print("6 - Salvar Dados")
    print("7 - Sair")

    escolha = input("Digite sua opção: ")

    if escolha == "1":
        adicionar_disco()
    elif escolha == "2":
        listar_discos()
    elif escolha == "3":
        buscar_por_ano()
    elif escolha == "4":
        buscar_por_musica()
    elif escolha == "5":
        alterar_dados()
    elif escolha == "6":
        salvar_dados()
        print("Dados Salvos em beatles.json")
    elif escolha == "7":
        salvar_dados()
        print("Dados Salvos em beatles.json")
        print("\nSaindo do programa. Até mais!")
        break
    else:
        print("Opção inválida, tente novamente.")
    