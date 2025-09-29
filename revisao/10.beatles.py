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
            else:
                break
           
        while True:
            vocais = input(f"\nDigite os vocais principais de {titulo}: ").strip()

            if not vocais:
                print("ERRO - Os vocais principais não podem estar em branco.")
            elif not all(c.isalpha() or c.isspace() for c in vocais):
                print("ERRO - Os vocais devem conter apenas letras e espaços.")
            else:
                break


        #Se passou nas validações anteriores -> adiciona a música
        musicas.append({
            "titulo": titulo,
            "vocais" : vocais
        })

    
    discos[nome] = entrada, gravadora, musicas
    print(f"\n Disco {nome} adicionado com sucesso.")
    

def listar_discos():
    print("\n--- DISCOGRAFIA DOS BEATLES ---")

    if not discos:
        print("Nenhum disco cadastrado no momento.")
    else:
        for nome, dados in discos.items():
            entrada = dados[0]
            gravadora = dados[1]
            musicas = dados[2]

            print(f"\n🎵 Disco: {nome}")
            print(f"  📅 Lançamento: {entrada}")
            print(f"  💿 Gravadora: {gravadora}")
            print("  🎶 Músicas:")

            for i, musica in enumerate(musicas, start=1):
                print(f"        {i}. {musica['titulo']} - (Vocais: {musica['vocais']})")


def buscar_por_ano():
    ano_desejado = input("Digite o ano que deseja buscar: ")

    print(f"\n--- Discos no ano {ano_desejado} ---")
    for nome, dados in discos.items():
        entrada = dados[0]
        gravadora = dados[1]
        musicas = dados[2]

        if entrada == ano_desejado:
            print(f"\n🎵 Disco: {nome}")
            print(f"  📅 Lançamento: {entrada}")
            print(f"  💿 Gravadora: {gravadora}")
            print("  🎶 Músicas:")

            for i, musica in enumerate(musicas, start=1):
                print(f"        {i}. {musica['titulo']} - (Vocais: {musica['vocais']})")


        #Implementar tratamento de erros para busca por ano inexistente
        #Implementar busca somente do dado 'ano' inserido em datetime





def buscar_por_musica() : print("Futura Implementação")
def buscar_por_vocal() : print("Futura Implementação")
def alterar_dados() : print("Futura Implementação")
def salvar_dados() : print("Futura Implementação")

while True:
    print("\n--- DISCOGRAFIA BEATLES ---")
    print("1 - Adicionar Disco")
    print("2 - Listar Discos")
    print("3 - Buscar por Ano")
    print("4 - Buscar por Música")
    print("5 - Buscar por Vocal")
    print("6 - Alterar Dados")
    print("7 - Salvar Dados")
    print("8 - Sair")

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
        buscar_por_vocal()
    elif escolha == "6":
        alterar_dados()
    elif escolha == "7":
        salvar_dados()
        print("Dados Salvos em beatles.json")
    elif escolha == "8":
        salvar_dados()
        print("Dados Salvos em beatles.json")
        print("\nSaindo do programa. Até mais!")
        break
    else:
        print("Opção inválida, tente novamente.")
    