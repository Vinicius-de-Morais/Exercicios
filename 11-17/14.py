funcionarios = []
 
def adiciona_funcionario(funcionario, salario):
    combo = [funcionario,salario]
    funcionarios.append(combo)

def aumento(funcionario):
    funcionario_index = 0
    for i in range (len(funcionarios)):
            if funcionario in funcionarios[i]:
                funcionario_index = i
    
    salario = funcionarios[funcionario_index][1]
    salario += (salario * 0.15)

    funcionarios[funcionario_index].insert(1, salario)
    funcionarios[funcionario_index].pop(2)

    nome = funcionarios[funcionario_index][0]

    print(f'O salario de {nome} agora é de {salario} Reais')   


adiciona_funcionario('Sofia', 15)
adiciona_funcionario('Flavio', 100)
adiciona_funcionario('marcio', 10)
print(funcionarios)
aumento('Flavio')
aumento('marcio')

print(funcionarios)
