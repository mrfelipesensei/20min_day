#Criando dicionário inicial vazio
lista_compras ={}

#Enquanto o programa não for encerrado
while True:

    #Menu de opções
    print("1 - Adiciona item")
    print("2 - Remover item")
    print("3 - Alterar quantidade")
    print("4 - Ver lista")
    print("5 - Sair")

    #Ler escolha do usuário
    escolha = input("Digite sua opção: ")

    if escolha == "1":
        #Pedir nome
        item = input("Digite o nome do item: ").strip().lower()
        
        #Pedir quantidade
        quantidade = int(input("Digite a quantidade: "))

        #Tratamento de erros
        if quantidade > 0:
            #Adicionar ao dicionário
            lista_compras[item] = quantidade
            print(f"{item} adicionado à lista de compras com a quantidade {quantidade}.")
        else:
            print(f"Digite um valor maior que zero!")

    elif escolha == "2":
        #Pedir nome do item
        item = input("Digite o nome do item a ser removido: ").strip().lower()

        #Tratamento de erros
        if item in lista_compras:
            #Remover do dicionário (se existir)
            del lista_compras[item]
            print(f"{item} removido da lista de compras")
        else:
            print(f"{item} não está cadastrado na lista de compras.")

    elif escolha == "3":
        #Pedir nome do item
        item = input("Digite o nome do item a ser atualizado: ").strip().lower()

        #Tratamento de erros
        if item in lista_compras:
            #Pedir nova quantidade
            nova_quantidade = int(input(f"Digite a nova quantidade do item {item}: "))
            #Tratamento de erros
            if nova_quantidade > 0:
            
                #Atualizar no dicionário (se existir)
                lista_compras[item] = nova_quantidade
                print(f"{item} atualizado com a nova quantidade: {nova_quantidade}")

            else:
                print(f"Digite um valor maior que zero!")  
        else:
            print(f"{item} não cadastrado na lista de compras.")

                    
    elif escolha == "4":
        print(lista_compras)

    elif escolha == "5":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida, tente novamente")