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

def alterar_dados():
    nome = input("Digite o Item a ser Alterado: ")

    if nome in estoque:
        print("1 - Alterar Valor")
        print("2 - Alterar Quantidade")
        print("3 - Alterar Categoria")
        print("4 - Deletar Item")
        print("5 - Voltar ao Menu Inicial")

        escolha2 = input("Digite sua opção: ")

        if escolha2 == "1":
            novo_valor = 0
            while novo_valor <= 0:
                try:
                    novo_valor = float(input(f"Digite o novo valor de {nome} R$: "))
                    if novo_valor <= 0:
                        print("Por favor, digite um valor maior que zero!")
                except ValueError:
                    print("Entrada inválida. Por favor digite um número!")

                quantidade_antiga = estoque[nome][1]
                categoria_antiga = estoque[nome][2]
                estoque[nome] = (novo_valor, quantidade_antiga, categoria_antiga)
                print(f"O Item {nome} teve seu valor unitário atualizado para: R$ {novo_valor:.2f}")

        elif escolha2 == "2":
            nova_quantidade = 0
            while nova_quantidade <= 0:
                try:
                    nova_quantidade = int(input(f"Digite a nova quantidade de {nome}: "))
                    if nova_quantidade <= 0:
                        print("Por favor, digite um valor maior que zero!")
                except ValueError:
                    print("Entrada inválida. Por favor digite um número inteiro!")
            
                valor_antigo = estoque[nome][0]
                categoria_antiga = estoque[nome][2]
                estoque[nome] = (valor_antigo, nova_quantidade, categoria_antiga)
                print(f"O Item {nome} teve sua quantidade alterada para {nova_quantidade}")
        
        elif escolha2 == "3":
            categoria_valida = None
            while True:
                nova_categoria = input(f"Digite a nova categoria de {nome}: ")

                if nova_categoria.strip():
                    categoria_valida = nova_categoria.strip()
                    break

                else:
                    print(f"Entrada inválida. Por favor, digite a nova categoria de {nome}!")

                
            if categoria_valida:
                valor_antigo = estoque[nome][0]
                quantidade_antiga = estoque[nome][1]
                estoque[nome] = (valor_antigo, quantidade_antiga, nova_categoria)
                print(f"O Item {nome} teve sua categoria alterada para {nova_categoria}")
            
        elif escolha2 == "4":
            del estoque[nome]
            print(f"{nome} foi Deletado do Estoque. ")
        
        elif escolha2 == "5":
            print("Voltando ao Menu Inicial...")
            return
        
        else:
            print("Opção inválida. Tente novamente.")
    
    elif nome not in estoque:
        print(f"Item {nome} não cadastrado no Estoque. ")


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
        