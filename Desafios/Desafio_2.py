import random as r
import datetime

def gera_boleto():
    numero_banco = input('Qual o numero do banco?\n')
    valor_boleto = input('Qual o valor do boleto?\n')

    data = datetime.datetime.now()
    dia = data.strftime("%d")
    mes = data.strftime("%m")
    ano = data.strftime("%Y")
    zeros = 00000000

    numero_aleatorio = r.randrange(1000, 10001)

    boleto_gerado = f'{numero_banco} | {numero_aleatorio}{dia}{mes}{ano}{zeros}{valor_boleto}'
    print(boleto_gerado)

gera_boleto()
