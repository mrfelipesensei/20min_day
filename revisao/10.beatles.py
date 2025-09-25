discos = {}

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
    