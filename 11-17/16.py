
def aluguel():
    dias = int(input('Quantos dias você ficou com o carro?\n'))
    km = int(input('Quantos quilômetros foram rodados?\n'))

    calculo_final = round((60 * dias) + (km * 0.15), 2)

    print(f'O Aluguel total foi de: {calculo_final}')

aluguel()

