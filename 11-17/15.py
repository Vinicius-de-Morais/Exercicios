
def converte_temperatura():
    tempertura = int(input('Qual temperatura em Celsius deseja converter em Fahrenheit?\n'))

    convertido = round(((9*tempertura)/5) + 32, 1)

    print(f'{tempertura}C° em Fahrenheit é: {convertido}F°')

converte_temperatura()
