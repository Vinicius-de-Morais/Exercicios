
class Probabilidade:
    def __init__(self, valor_dado):
        valores = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.97, 1]
        for valor in valores:
            print(f'Para você ter {int(valor * 100)}% de chances de conseguir o item você deverá matar {round(valor * valor_dado, 2)} inimigos no jogo.')


if __name__ == '__main__':
    valor = input('Qual a probabilidade do item ser obtido?  ')
    index = valor.find('/')
    numero = int(valor[index + 1:])
    probabilidade = Probabilidade(numero)
