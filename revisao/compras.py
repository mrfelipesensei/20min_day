#Crie uma lista de compras usando dicionário
lista_compras = {
    "banana" : 5,
    "maçã" : 8,
    "frango" : 1,
    "ovos" : 12,
    "mussarela" : 2
}

#Adicionar novo item
lista_compras["cenoura"] = 5

#Remover item
del lista_compras["ovos"]

#Alterar quantidade de item
lista_compras["cenoura"] = 2

print(lista_compras)