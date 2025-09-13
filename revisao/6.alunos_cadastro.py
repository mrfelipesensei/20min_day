#Criando dicionário inicial vazio
alunos_cadastrados = {}

#Enquanto o programa não for encerrado
while True:

    #Menu de opções
    print("1 - Cadastrar aluno")
    print("2 - Remover aluno")
    print("3 - Alterar dados")
    print("4 - Ver alunos cadastrados")
    print("5 - Sair")

    #Ler a escolha do usuário
    escolha = input("Digite sua opção: ")

    if escolha == "1":
        #Pedir nome do aluno
        nome = input("Digite o nome do aluno: ").strip()

        curso = input(f"Digite o curso do aluno {nome}: ")

        #Loop para garantir idade válida
        idade = 0
        while idade <= 0:
            try:
                #Pedir idade
                idade = int(input(f"Digite a idade de {nome}: "))
                if idade <= 0:
                    print("Por favor, digite um valor maior que zero!")
                elif idade < 18:    
                    print("O aluno não pode ser menor de idade!")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro!")

            #Adicionar ao dicionário
            alunos_cadastrados[nome] = curso, idade
            print(f"{nome} adicionado com sucesso aos alunos cadastrados.")
        
    elif escolha == "5":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida, tente novamente.")


