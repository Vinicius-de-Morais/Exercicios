import random as r
funcionarios = []

def adiciona_funcionario():
    contador = 0
    while len(funcionarios) <= 9:
        funcionario = input('Qual o nome do Funcionario?\n')
        salario = float(input('Qual o salario?\n'))
        combo = [funcionario,salario]
        funcionarios.append(combo)
        contador += 1
        if contador == 3:
            for x in range(len(funcionarios)):
                salario = funcionarios[x][1]
                salario += round((salario * 0.05), 2)
                funcionarios[x].insert(1, salario)
                funcionarios[x].pop(2)
            contador = 0
    for x,y in funcionarios:
        print(f'Nome: {x} Salario: {y}')

    sorteado = r.choice(funcionarios)
    sorteado[1] += round(sorteado[1] * 0.10, 2)
    print(f'''Parabens ao funcionario {sorteado[0]} ele foi sorteado e gratificado com 10% de aumento
Agora seu salário é de {sorteado[1]}''')
    


adiciona_funcionario()
