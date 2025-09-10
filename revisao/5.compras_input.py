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
        #Pedir quantidade
        #Adicionar ao dicionário
    elif escolha == "2":
        #Pedir nome do item
        #Remover do dicionário (se existir)
    elif escolha == "3":
        #Pedir nome do item
        #Pedir nova quantidade
        #Atualizar no dicionário (se existir)
    elif escolha == "4":
        print(lista_compras)
    elif escolha == "5":
        print("Saindo do programa. Até mais!")
        break

else:
    print("Opção inválida, tente novamente")