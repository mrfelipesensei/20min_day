from datetime import datetime

jogos = {}

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

    jogos[titulo] = desenvolvedora, data, plataformas
    print(f"\n Jogo {titulo} adicionado com sucesso.")
