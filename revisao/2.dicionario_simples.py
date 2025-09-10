#Dicionário simples
dados = {
    "nome" : "Felipe",
    "idade" : 28,
    "cidade" : "Ceilândia"
}

#Acessar o valor de "cidade"
print(dados["cidade"])

#Alterar a idade
dados["idade"] = 29

#Adicionar nova chave "profissão"
dados["profissão"] = "Desenvolvedor"

#Remover a chave cidade
#Remover com del
del dados["cidade"]

#Remover com pop
idade_removida = dados.pop("idade")


