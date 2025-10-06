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


def adicionar_jogo():

    titulo = pergunta_titulo()




