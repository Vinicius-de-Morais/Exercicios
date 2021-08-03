input_nome = input('Qual o seu nome?\n').title()
input_data = input("Qual sua data de nascimento? (dd/mm/aa)\n")

def formata_data(data):
    d = input_data.replace('/', '')
    
    if len(d) == 6:
        data = f'{d[:2]}/{d[2:4]}/{d[4:]}'
    else:
        raise ValueError('Ensira uma data no formado dd/mm/aa')
    return data

def exibe():
    data_formatada = formata_data(input_data)
    print(f'{input_nome}\n{data_formatada}')    

exibe()