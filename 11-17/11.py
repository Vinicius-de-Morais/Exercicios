
def conversor():
    print('''Conversor de Reais em Dólares:
Valor do Dólar: $ 5.30''')
    valor = float(input('Quanto deseja converter?  ').replace(',','.'))

    valor_convertido = round(valor * 5.30, 2)

    print(f'R$ {valor} Reais em Dólares é: $ {valor_convertido}')

conversor()
