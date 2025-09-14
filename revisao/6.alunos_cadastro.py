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
        
    elif escolha == "2":
        #Pedir nome do aluno
        nome = input("Digite o nome do aluno que deseja remover: ")

        if nome in alunos_cadastrados:
            #Remover do dicionário, se ele existir
            del alunos_cadastrados[nome]
            print(f"{nome} foi removido dos alunos cadastrados.")

    elif escolha == "3":
        #Pedir nome do aluno
        nome = input("Digite o nome do aluno a ser atualizado: ")

        if nome in alunos_cadastrados:
            print("1 - Para alterar o curso: ")
            print("2 - Para alterar a idade: ")
            print("3 - Voltar ao Menu Inicial.")

            escolha2 = input("Digite sua opção: ")
            if escolha2 == "1":
                #Lógica de novo curso
                curso_valido = None
                while True: 
                    #1. Pedir novo curso, informa como sair
                    novo_curso = input(f"Digite o novo curso para o aluno {nome}: ")
                    print("Ou digite 'sair' para cancelar.")

                    #2. Verifica se o usuário quer sair
                    if novo_curso.strip().lower() == 'sair':
                        print("Operação cancelada pelo usuário.")
                        break

                    #3. Verifica se a entrada é válida (não está em branco)
                    if novo_curso.strip():
                        curso_valido = novo_curso.strip() #Armazena o valor
                        break #Quebra o loop dada a entrada válida

                    else:
                        print("Entrada inválida. Por favor, digite um nome de curso válido!")

                    
                #Adicionar ao dicionário somente se um curso válido for inserido
                if curso_valido:
                    idade_antiga = alunos_cadastrados[nome][1] #Pega a idade, que está no ínice 1 para não perder/alterar o dado
                    alunos_cadastrados[nome] = (curso_valido, idade_antiga)
                    print(f"O curso de {nome} foi atualizada para {curso_valido}")
                
            elif escolha2 == "2":
                nova_idade = 0
                while nova_idade <= 0:
                    try:
                        #Pedir nova idade
                        nova_idade = int(input(f"Digite a nova idade de {nome}: "))
                        if nova_idade <= 0:
                            print("Por favor, digite um valor maior que zero!")
                        elif nova_idade < 18:
                            print("O aluno não pode ser menor de idade!")
                    except ValueError:
                        print("Entrada inválida. Por favor, digie um número inteiro!")

                    curso_antigo = alunos_cadastrados[nome][0] #Pega o curso, que está no índice 0 para não perder/alterar o dado
                    alunos_cadastrados[nome] = (curso_antigo, nova_idade)
                    print(f"A idade de {nome} foi atualizada para {nova_idade}.")

            elif escolha2 == "3":
                break
            else:
                print("Opção inválida, tente novamente.")
                

        else:
            print(f"{nome} não cadastrado dentre os alunos.")


    elif escolha == "4":
        print("\n--- ALUNOS CADASTRADOS ---")
        #Melhoria - exibição mais legível
        if not alunos_cadastrados:
            print("Nenhum aluno cadastrado no momento.")
        else:
            for nome, dados in alunos_cadastrados.items():
                curso = dados[0]
                idade = dados[1]
                print(f"Nome: {nome} | Curso: {curso} | Idade: {idade}")
        
    elif escolha == "5":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida, tente novamente.")


