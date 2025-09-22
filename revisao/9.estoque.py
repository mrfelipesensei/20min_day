#Carregando dicionário inicial vazio
estoque = {}

def adicionar_item():
    nome = input("Digite o nome do item: ").strip()

    valor = float(input(f"Digite o valor de {nome} R$: "))

    quantidade = int(input(f"Digite a quantidade: "))

    categoria = input(f"Digite a categoria de {nome}: ")

    #Adicionar ao dicionário
    estoque[nome] = valor, quantidade, categoria
    print(f"{nome} adicionado com sucesso.")



while True:
    print("\n--- CONTROLE DE ESTOQUE ---")
    print("1 - Adicionar Item")
    print("2 - Listar Itens")
    print("3 - Filtar por Categoria")
    print("4 - Calcular Valor Total")
    print("5 - Alterar Dados")
    print("6 - Salvar Dados")
    print("7 - Sair")

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
        print("Controle de Estoque salvo no arquivo lista_compras.json")
    elif escolha == "7":
        print("\nSaindo do programa. Até mais!")
        break
    else:
        print("Opção inválida, tente novamente.")
        