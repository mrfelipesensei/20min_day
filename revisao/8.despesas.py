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

        print(f"Total gasto: R$ {gasto_total:.2f}")

def gasto_total():
    valor_total = 0
    for nome, dados in despesas.items():
        valor = dados[0]
        valor_total += valor

    print(f"O gasto total das despesas foi de R$: {valor_total:.2f}")

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
        
def alterar_dados():
    nome = input("Digite a despesa a ser alterada: ")

    if nome in despesas:
        print("1 - Alterar o valor")
        print("2 - Alterar a categoria")
        print("3 - Voltar ao Menu Inicial")

        escolha2 = input("Digite sua opção: ")

        if escolha2 == "1":
            novo_valor = 0
            while novo_valor <= 0:
                try:
                    novo_valor = float(input(f"Digite o novo valor de {nome}: "))
                    if novo_valor <= 0:
                        print("Por favor, digite um valor maior que zero!")
                except ValueError:
                    print("Entrada inválida. Por favor digite um número!")

                #CORRIGIR ERRO DE LISTAR_DADOS()
                categoria_antiga = despesas[nome][1]
                despesas[nome] = (novo_valor, categoria_antiga)
                print(f"A despesa {nome} teve seu valor atualizado para {novo_valor:.2f}")

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
    
    elif escolha == "4":
        alterar_dados()

    elif escolha == "5":
        gasto_total()
        
    elif escolha == "6":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida, tente novamente.")
