from funcoes import adicionar_jogo
from funcoes import listar_jogos

while True:
    print("\n--- CATÁLOGO DE GAMES ---")
    print("1 - Adicionar Jogo")
    print("2 - Listar Jogos")
    print("3 - Buscar por Título")
    print("4 - Buscar por Desenvolvedora")
    print("5 - Buscar por Ano")
    print("6 - Alterar Dados")
    print("7 - Salvar Dados")
    print("8 - Sair")

    escolha = input("Digite sua opção: ")

    if escolha == "1":
        adicionar_jogo()
    elif escolha == "2":
        listar_jogos()
    elif escolha == "3":
        print("Chama a função buscar_por_titulo()")
    elif escolha == "4":
        print("Chama a função buscar_por_dev()")
    elif escolha == "5":
        print("Chama a função buscar_por_ano()")
    elif escolha == "6":
        print("Chama a função alterar_dados()")
    elif escolha == "7":
        print("Chama a função salvar_dados()")
    elif escolha == "8":
        print("Salva os dados")
        print("\nSaindo do programa. Até mais!")
        break
    else:
        print("Opção inválida, tente novamente.")