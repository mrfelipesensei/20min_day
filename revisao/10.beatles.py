from datetime import datetime


discos = {}

def adicionar_disco():

    while True:
        nome = input("Digite o Nome do Disco: ").strip()

        if not nome:
            print("ERRO - O nome não pode estar em branco.")
            continue

        if not all(c.isalpha() or c.isspace() for c in nome):
            print("ERRO - O nome deve conter apenas letras e espaços.")
            continue

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

        if not all(c.isalpha() or c.isspace() for c in gravadora):
            print("ERRO - A Gravadora deve conter apenas letras e espaços.")
            continue

        break

    musicas = []

    while True:
        titulo = input("Digite o título da música: ").strip()

        if not titulo:
            print("ERRO - O título não pode estar em branco.")
            continue

        if not all(c.isalpha() or c.isspace() for c in titulo):
            print("ERRO - O título deve conter apenas letras e espaços.")
            continue

        musicas.append({"titulo":titulo})

        continuar = input("Deseja adicionar outra música? (s/n): ").strip().lower()
        if continuar == "n":
            break
        else:
            continue

    
    discos[nome] = entrada, gravadora, musicas
    print(f"{nome} adicionado com sucesso.")
    

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
    