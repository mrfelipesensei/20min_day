def adicionar_despesa():
    nome = input("Digite o nome da despesa: ").strip()

    valor = float(input(f"Digite o valor de {nome}: "))

    categoria = input(f"Digite a categoria de {nome}: ")

    #Adicionar ao dicionário
    despesas[nome] = valor, categoria
    print(f"{nome} adicionada com sucesso.")

despesas = {}

while True:
    print("\n1 - Adicionar despesa")
    print("2 - Listar despesas")
    print("3 - Filtrar por categoria")
    print("4 - Alterar dados") #Colocar lógica de remover despesa dentro de alterar dados
    print("6 - Calcular total gasto")
    print("7 - Sair")

    escolha = input()

    if escolha == "1":
        adicionar_despesa()
    elif escolha == "5":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida, tente novamente.")
