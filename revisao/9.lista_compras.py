#Carregando dicionário inicial vazio
lista_compras = {}


while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1 - Adicionar Item")
    print("2 - Listar Itens")
    print("3 - Filtar por Categoria")
    print("4 - Calcular Valor Total")
    print("5 - Alterar Dados")
    print("6 - Salvar Dados")
    print("7 - ")

    escolha = input("Digite sua opção: ")

    if escolha == "1":
        adicionar_item()
    elif escolha == "2":
        listar_itens()
    elif escolha == "3":
        filtrar_itens()
    elif escolha == "4":
        valor_total()
    elif escolha == "5":
        alterar_dados()
    elif escolha == "6":
        salvar_dados()
        print("Lista de Compras salvas no arquivo lista_compras.json")
    elif escolha == "7":
        print("\nSaindo do programa. Até mais!")
        break
    else:
        print("Opção inválida, tente novamente.")
        