from datetime import datetime
import json
import os

def carregar_dados():
    if os.path.exists("jogos.json") and os.path.getsize("jogos.json") > 0:
        try:
            with open("jogos.json","r",encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            return {}
    return {}

def salvar_dados():
    with open("jogos.json","w",encoding="utf-8") as arquivo:
        json.dump(jogos, arquivo, indent=4, ensure_ascii=False)

jogos = carregar_dados()

def pergunta_titulo():

    while True:
        titulo = input("Digite o Título do Jogo: ").strip()

        if not titulo:
            print("ERRO - O Título não pode estar em branco.")
            continue

        elif not all(c.isalpha() or c.isspace() for c in titulo):
            print("ERRO - O título deve conter apenas letras e espaços.")
            continue
        else:
            break

    return titulo

def pergunta_dev():

    while True:
        desenvolvedora = input("Digite o nome da Desenvolvedora: ")

        if not desenvolvedora:
            print("ERRO - O nome da Desenvolvedora não pode estar em branco.")
            continue

        elif not all(c.isalpha() or c.isspace() for c in desenvolvedora):
            print("ERRO - O nome da desenvolvedora deve conter apenas letras e espaços.")
            continue
        else:
            break
    
    return desenvolvedora

def pergunta_data():

    while True:
        entrada = input("Digite a data de seu lançamento (dd/mm/aaaa): ")

        try:
            data = datetime.strptime(entrada, "%d/%m/%Y")
            print("Data de lançamento válida: ", data.strftime("%d/%m/%Y"))
            break
        except ValueError:
            print("Data inválida! Use o formato dd/mm/aaaa")
            continue

    return entrada

def adicionar_jogo():

    titulo = pergunta_titulo()

    desenvolvedora = pergunta_dev()

    data = pergunta_data()

    while True:
        try:
            num_plataformas = int(input("Em quantas plataformas o jogo está disponível? "))
            if num_plataformas > 0:
                break
            else:
                print("ERRO - O número de plataformas deve ser maior que zero.")

        except ValueError:
            print("ERRO - Por favor, digite um número inteiro válido.")

    plataformas = []
    
    for i in range(num_plataformas):
        while True:
            plataforma = input(f" Digite o nome da Plataforma {i + 1}: ").strip()

            if not plataforma:
                print("ERRO - A plataforma não pode estar em branco.")
            elif not all(c.isalnum() or c.isspace() or c in "-" for c in plataforma):
                #permite letras, números, espaços, hífens
                print("ERRO - O nome da plataforma deve conter apenas letras, números, espaços, hífens")
            else:
                break
    
        plataformas.append(plataforma)

    #Guardar como dicionário - facilita manutenção
    jogos[titulo] = {
        "desenvolvedora" : desenvolvedora,
        "data" : data,
        "plataformas" : plataformas
    }

    print(f"\n Jogo {titulo} adicionado com sucesso.")

def mostrar_lista(jogos_para_mostrar=None):
    if jogos_para_mostrar is None:
        jogos_para_mostrar = jogos

    for titulo, dados in jogos_para_mostrar.items():
        print(f"\n  🎮 Jogo: {titulo}")
        print(f"  🖥️  Desenvolvedora: {dados['desenvolvedora']}")
        print(f"  📅 Lançamento: {dados['data']}")
        print("  🕹️  Plataformas: ")
        
        for i, plataforma in enumerate(dados["plataformas"], 1):
            print(f"        {i}. {plataforma}")


def listar_jogos():
    print("\n--- CATÁLOGO DE JOGOS ---")
    
    if not jogos:
        print("Nenhum jogo catalogado no momento.")
        return
    
    mostrar_lista()

def buscar_por_titulo():
    titulo_desejado = pergunta_titulo()

    encontrados = {}

    print(f"\n--- Jogo {titulo_desejado} ---")

    for titulo, dados in jogos.items():
        if titulo_desejado.lower() == titulo.lower():
            encontrados[titulo] = dados
    
    if encontrados:
        mostrar_lista(encontrados)

    else:
        print(f"Nenhum jogo encontrado com o título {titulo_desejado}.")

def buscar_por_dev():
    desenvolvedora_desejada = pergunta_dev()

    encontrados = {}

    print(f"\n--- Desenvolvedora {desenvolvedora_desejada} ---")

    for titulo, dados in jogos.items():
        if desenvolvedora_desejada.lower() == dados["desenvolvedora"].lower():
            encontrados[titulo] = dados

    if encontrados:
        mostrar_lista(encontrados)
    else:
        print(f"Nenhuma desenvolvedora encontrada chamada {desenvolvedora_desejada}.")


def buscar_por_ano():
    ano_desejado = input("Digite o ano que deseja buscar: ").strip()

    encontrados = {}

    print(f"\n--- Jogos no ano de {ano_desejado} ---")

    for titulo, dados in jogos.items():
        
        try:
            data = datetime.strptime(dados["data"], "%d/%m/%Y")
            ano_jogo = str(data.year)
        except ValueError:
            continue

        if ano_jogo == ano_desejado:
            encontrados[titulo] = dados

    if encontrados:
        mostrar_lista(encontrados)
    else:
        print(f"Nenhum jogo encontrado para o ano de {ano_desejado}")