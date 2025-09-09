#Lista de dicionários
boletim = [
    {"nome" : "Felipe", "nota" : 9},
    {"nome" : "Maria", "nota": 10}
]

#Acessar nota do segundo aluno
print(boletim[1]["nota"])

#Adicionar um novo aluno
boletim.append({"nome" : "Josias", "nota" : 0})

#Remover um aluno
boletim.remove(boletim[2])

