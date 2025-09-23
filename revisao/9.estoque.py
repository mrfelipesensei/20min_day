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

def listar_itens():
    print("\n--- CONTROLE DE ESTOQUE ---")
    valor_total_estoque = 0

    if not estoque:
        print("Nenhum item cadastrado no momento.")
    else:
        for nome, dados in estoque.items():
            valor = dados[0]
            quantidade = dados[1]
            categoria = dados[2]

            #Cálculo do valor indexado pela quantidade
            valor_calc_item = valor * quantidade

            print(f"Nome: {nome} | Valor Unitário: R$ {valor:.2f} | Quantidade: {quantidade} | Valor Total:  R$ {valor_calc_item:.2f} | Categoria: {categoria}")
            
            valor_total_estoque += valor * quantidade

        #Valor total de TODOS os itens do estoque
        print(f"Valor Total do Estoque: R$ {valor_total_estoque:.2f}")


def filtrar_itens():
    categoria_desejada = input("Digite a Categoria desejada: ")
    valor_categoria = 0

    print(f"\n--- Itens na Categoria de {categoria_desejada}")
    for nome, dados in estoque.items():
        valor = dados[0]
        quantidade = dados[1]
        categoria = dados[2]

        #Cálculo do valor indexado pela quantidade
        valor_calc_item = valor * quantidade

        if categoria.lower() == categoria_desejada.lower():
            print(f"Nome: {nome} | Valor Uniário: R$ {valor} | Quantidade {quantidade} | Valor Total: R$ {valor_calc_item:.2f}")
            valor_categoria += valor * quantidade

    print(f"Valor Total da Categoria {categoria_desejada}: R$ {valor_categoria:.2f}")

def valor_total():
    print("\n--- VALOR TOTAL DO ESTOQUE ---")
    valor_total_estoque = 0

    if not estoque:
        print("Nenhum item cadastrado no momento.")
    else:
        for nome, dados in estoque.items():
            valor = dados[0]
            quantidade = dados[1]

            valor_total_estoque += valor * quantidade

        print(f"Valor total do Estoque: R$ {valor_total_estoque:.2f}")

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
        