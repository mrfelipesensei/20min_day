from datetime import datetime
import json
import os

def carregar_dados():
    if os.path.exists("beatles.json") and os.path.getsize("beatles.json") > 0:
        try:
            with open("beatles.json","r",encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            return {}
    return {}

def salvar_dados():
    with open("beatles.json","w",encoding="utf-8") as arquivo:
        json.dump(discos, arquivo, indent=4, ensure_ascii=False)

discos = carregar_dados()

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

        #Aqui eu quero colocar uma lógica que verifica se o usuário tem certeza de que deseja cadastrar as informações
        #Além de poder editar aqui mesmo uma possível informação errada chamando portanto as futuras funções:
        #alterar_nome_disco()
        #alterar_gravadora()
        #alterar_data()
        #alterar_nome_musica()
        #alterar_vocais()

        #Se passou nas validações anteriores -> adiciona a música
        musicas.append({
            "titulo": titulo,
            "vocais" : vocais
        })

    
    discos[nome] = entrada, gravadora, musicas
    salvar_dados() #Salva os dados em 'beatles.json'
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
    ano_desejado = input("Digite o ano que deseja buscar: ").strip()

    #Verifica se o usuário digitou apenas números
    if not ano_desejado.isdigit():
        print("ERRO - Digite apenas números para o ano (ex: 1963).")
        return


    encontrado = False #Flag para verificar se algum disco foi encontrado

    print(f"\n--- Discos no ano {ano_desejado} ---")
    for nome, dados in discos.items():
        entrada = dados[0]
        gravadora = dados[1]
        musicas = dados[2]

        try:
            data = datetime.strptime(entrada, "%d/%m/%Y")
            ano_disco = str(data.year)
        except ValueError:
            #Caso algum disco tenha sido salvo com a data inválida
            continue


        #Compara apenas o ano
        if ano_disco == ano_desejado:
            encontrado = True  #Flag dizendo que foi encontrado
            print(f"\n🎵 Disco: {nome}")
            print(f"  📅 Lançamento: {entrada}")
            print(f"  💿 Gravadora: {gravadora}")
            print("  🎶 Músicas:")

            for i, musica in enumerate(musicas, start=1):
                print(f"        {i}. {musica['titulo']} - (Vocais: {musica['vocais']})")

    if not encontrado:
        print(f"Nenhum disco encontrado no ano {ano_desejado}.")


def buscar_por_musica():
    musica_desejada = input("Digite o título da música que deseja buscar: ").strip()

    if not musica_desejada:
        print("ERRO - O titulo da música não pode estar em branco.")
        return
    
    encontrado = False

    print(f"\n--- Discos com a música {musica_desejada} ---")
    for nome, dados, in discos.items():
        entrada = dados[0]
        gravadora = dados[1]
        musicas = dados[2]

        for i, musica in enumerate(musicas,start=1):
            #Busca parcial (case-sensitive)
            if musica_desejada.lower() in musica["titulo"].lower():
                if not encontrado:
                    encontrado = True
                print(f"\n🎵 Disco: {nome}")
                print(f"  📅 Lançamento: {entrada}")
                print(f"  💿 Gravadora: {gravadora}")
                print(f"  🎶 Música encontrada: {musica['titulo']} - (Vocais: {musica['vocais']})")
    
    if not encontrado:
        print(f"Nenhuma música encontrada com o título {musica_desejada}.")


def buscar_por_gravadora():
    gravadora_desejada = input("Digite a Gravadora que deseja buscar: ")

    if not gravadora_desejada:
        print("ERRO - O nome da gravadora não pode estar em branco.")
        return

    encontrado = False

    print(f"\n--- Discos da Gravadora {gravadora_desejada} ---")
    for nome, dados in discos.items():
        entrada = dados[0]
        gravadora = dados[1]
        musicas = dados[2]

        if gravadora_desejada.lower() == gravadora.lower():
            encontrado = True
            print(f"\n🎵 Disco: {nome}")
            print(f"  📅 Lançamento: {entrada}")
            print(f"  💿 Gravadora: {gravadora}")
            print("  🎶 Músicas:")

            for i, musica in enumerate(musicas, start=1):
                print(f"        {i}. {musica['titulo']} - (Vocais: {musica['vocais']})")

    if not encontrado:
        print(f"Nenhum disco encontrado com a Gravadora {gravadora_desejada}.")

def alterar_data(nome):
    while True:
        nova_data = input("Digite a nova data (dd/mm/aaaa): ").strip()

        try:
            data = datetime.strptime(nova_data, "%d/%m/%Y")
            discos[nome] = (nova_data, discos[nome][1], discos[nome][2])
            salvar_dados()
            print(f"Data do disco {nome} foi alterada para {nova_data}")
            break
        except ValueError:
            print("Data inválida! Use o formato dd/mm/aaaa.")

def alterar_gravadora(nome):
    while True:
        nova_gravadora = input("Digite o nome da nova Gravadora: ")

        if not nova_gravadora:
            print("ERRO - A nova Gravadora não pode estar em branco.")
            continue

        elif not all(c.isalpha() or c.isspace() for c in nova_gravadora):
            print("ERRO - A nova Gravadora deve conter apenas letras e espaços.")
            continue

        else:
            discos[nome] = (discos[nome][0], nova_gravadora, discos[nome][2])
            salvar_dados()
            print(f"A gravadora do disco {nome} foi alterada para {nova_gravadora}")
            break

def alterar_musica(nome):
    musicas = discos[nome][2]

    print(f"\n🎶 Músicas do disco {nome}:")
    for i, musica in enumerate(musicas, start=1):
        print(f"{i}. {musica['titulo']} - (Vocais: {musica['vocais']})")
    
    while True:
        try:
            escolha = int(input("\nDigite o número da música que deseja alterar: "))
            if 1 <= escolha <= len(musicas):
                break
            else:
                print("Número inválido. Escolha um número da lista.")
        except ValueError:
            print("ERRO - Digite um número válido.")
    
    #Lógica de acesso correto do número da música de acordo com o índice - se o usuário escolheu 3, o índice será 2
    indice = escolha - 1 
    musica_antiga = musicas[indice]['titulo']

    while True:
        novo_titulo = input(f"Digite o novo título para a música {musica_antiga}: ").strip()

        if not novo_titulo:
            print("ERRO - O título não pode estar em branco.")
        else:
            break

    musicas[indice]['titulo'] = novo_titulo
    discos[nome] = (discos[nome][0], discos[nome][1], musicas)
    salvar_dados()
    print(f"Título da música alterada com sucesso para {novo_titulo}.")

def alterar_vocais(nome):
    musicas = discos[nome][2]

    print(f"\n🎶 Músicas do disco {nome}:")
    for i, musica in enumerate(musicas,start=1):
        print(f"{i}. {musica['titulo']} - (Vocais: {musica['vocais']})")
    
    while True:
        try:
            escolha = int(input("\nDigite o número da música que deseja alterar os vocais: "))
            if 1 <= escolha <= len(musicas):
                break
            else:
                print("Número inválido. Escolha um número da lista.")
        except ValueError:
            print("ERRO - Digite um número válido.")

    indice = escolha - 1
    musica_escolhida = musicas[indice]['titulo']

    while True:
        novos_vocais = input(f"Digite os novos vocais para a música {musica_escolhida}: ")

        if not novos_vocais:
            print("ERRO - O título não pode estar em branco.")
        else:
            break
    
    musicas[indice]['vocais'] = novos_vocais
    discos[nome] = (discos[nome][0], discos[nome][1], musicas)
    salvar_dados()
    print(f"Vocais da música {musica_escolhida} alterados para {novos_vocais}.")

def deletar_disco(nome):
    questao = input(f"\nVocê tem certeza que deseja deletar o Disco {nome}? (s/n): ")

    if questao == "s":
        del discos[nome]
        print(f"{nome} foi deletado da Discografia com sucesso.")
    elif questao == "n":
        return
    else:
        print("Opção inválida, digite 's' para deletar e 'n' para voltar.")


def alterar_dados():
    while True:
        nome = input("Digite o Nome do Disco a ser Alterado: ")

        if not nome:
            print("ERRO - O nome não pode estar em branco.")
            continue

        elif not all(c.isalpha() or c.isspace() for c in nome):
            print("ERRO - O nome deve conter apenas letras e espaços.")
            continue
        else:
            break


    if nome in discos:
        print("\n --- MENU DE ALTERAÇÕES ---")
        print("1 - Alterar Data")
        print("2 - Alterar Gravadora")
        print("3 - Alterar Título de Música")
        print("4 - Alterar Vocais Principais")
        print("5 - Deletar Disco")
        print("6 - Voltar ao Menu Inicial")

        escolha2 = input("Digite sua opção: ")

        if escolha2 == "1":
            alterar_data(nome)
        elif escolha2 == "2":
            alterar_gravadora(nome)
        elif escolha2 == "3":
            alterar_musica(nome)
        elif escolha2 == "4":
            alterar_vocais(nome)
        elif escolha2 == "5":
            deletar_disco(nome)
        elif escolha2 == "6":
            print("Voltando ao Menu Inicial...")
            return
        
        else:
            print("Opção inválida. Tente novamente.")

    elif nome not in discos:
        print(f"Disco {nome} não encontrado na Discografia")




while True:
    print("\n--- DISCOGRAFIA BEATLES ---")
    print("1 - Adicionar Disco")
    print("2 - Listar Discos")
    print("3 - Buscar por Ano")
    print("4 - Buscar por Música")
    print("5 - Buscar por Gravadora")
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
        buscar_por_gravadora()
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
    