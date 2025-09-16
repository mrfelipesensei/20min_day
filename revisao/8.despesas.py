def adicionar_despesa():
    nome = input("Digite o nome da despesa: ").strip()

    valor = float(input(f"Digite o valor de {nome} R$: "))

    categoria = input(f"Digite a categoria de {nome}: ")

    #Adicionar ao dicionário
    despesas[nome] = valor, categoria
    print(f"{nome} adicionada com sucesso.")

def listar_despesas():
    print("\n--- LISTA DE DESPESAS ---")

    if not despesas:
        print("Nenhuma despesa cadastrada no momento.")
    else:
        for nome, dados in despesas.items():
            valor = dados[0]
            categoria = dados[1]
            print(f"Nome: {nome} | Valor: {valor:.2f} | Categoria {categoria}")


despesas = {}

while True:
    print("\n1 - Adicionar despesa")
    print("2 - Listar despesas")
    print("3 - Filtrar por categoria")
    print("4 - Alterar dados") #Colocar lógica de remover despesa dentro de alterar dados
    print("5 - Calcular total gasto")
    print("6 - Sair")

    escolha = input()

    if escolha == "1":
        adicionar_despesa()

    elif escolha == "2":
        listar_despesas()

    elif escolha == "6":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida, tente novamente.")
