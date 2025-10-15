from funcoes import adicionar_jogo, listar_jogos, buscar_por_titulo, buscar_por_dev, buscar_por_ano, salvar_dados, alterar_dados

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
        buscar_por_titulo()
    elif escolha == "4":
        buscar_por_dev()
    elif escolha == "5":
        buscar_por_ano()
    elif escolha == "6":
        alterar_dados()
    elif escolha == "7":
        salvar_dados()
        print("Dados salvos em jogos.json")
    elif escolha == "8":
        salvar_dados()
        print("Dados salvos em jogos.json")
        print("\nSaindo do programa. Até mais!")
        break
    else:
        print("Opção inválida, tente novamente.")