def adicionar_despesa():
    nome = input("Digite o nome da despesa: ").strip()

    valor = float(input(f"Digite o valor de {nome} R$: "))

    categoria = input(f"Digite a categoria de {nome}: ")

    #Adicionar ao dicionário
    despesas[nome] = valor, categoria
    print(f"{nome} adicionada com sucesso.")

def listar_despesas():
    print("\n--- LISTA DE DESPESAS ---")
    gasto_total = 0

    if not despesas:
        print("Nenhuma despesa cadastrada no momento.")
    else:
        for nome, dados in despesas.items():
            valor = dados[0]
            categoria = dados[1]
            print(f"Nome: {nome} | Valor R$: {valor:.2f} | Categoria: {categoria}")
            gasto_total += valor

        print(f"Total gsto: R$ {gasto_total:.2f}")

def filtrar_despesas():
    categoria_desejada = input("Digite o nome da categoria que deseja filtrar: ")
    gasto_categoria = 0

    print(f"\n---Despesas na categoria {categoria_desejada} ---")
    for nome, dados in despesas.items():
        valor = dados[0]
        categoria = dados[1]
        if categoria.lower() == categoria_desejada.lower():
            print(f"Categoria: {categoria} | Valor R$: {valor:.2f} | Nome: {nome}")
            gasto_categoria += valor
        
    print(f"Gasto total da categoria {categoria_desejada} R$: {gasto_categoria:.2f} ")
        

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

    elif escolha == "3":
        filtrar_despesas()

    elif escolha == "6":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida, tente novamente.")
