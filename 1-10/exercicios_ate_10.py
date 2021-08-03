
def soma():
    try:
        print('Vamos somar, por-favor digite os valores:')
        numero_1 = int(input('Qual o primeiro numero?  '))
        numero_2 = int(input('Qual o segundo numero?  '))

        operacao = numero_1 + numero_2
        antecessor = operacao - 1
        sucessor = operacao + 1
        print(f'''
O resultado é da soma é: {operacao}
Seu antecessor é: {antecessor}
Seu sucessor é: {sucessor}''')
    except:
        print('Não foi possivel realizar a operação, digite outros valores')

def informacoes():
    print('Informações:')
    numero = int(input('Qual o numero?  '))

    if numero%2 == 0:
        info = 'par'
    else:
        info = 'ímpar'
# eu não fiz relacionado a alfanumericos pq não sabia nada a respeito
    dobro = numero * 2
    triplo = numero * 3
    raiz = round(float(numero) ** 0.5, 2)
    quadrado = numero ** 2
    cubo = numero ** 3
    print(f'''
As informações sobre o numero {numero} são:
Ele é: {info};
Seu dobro é:    {dobro};
Seu triplo é:   {triplo};
Sua raiz é:     {raiz};
Seu quadrado é: {quadrado};
Seu cubo é:     {cubo}.''')

def calcula_media():
    print('Calcula Média')
    media_1 = float(input('Digite a primeira média: \n'))
    media_2 = float(input('Digite a segunda média: \n'))

    media_final = media_1 + media_2 % 2

    print(f'A média final é: {media_final}')

def conversor():
    print('Conversor:')
    valor_m = float(input('Qual o valor em metros?\n'))
    valor_cm =  valor_m * 100
    valor_mm = valor_m * 1000

    print(f'''
{valor_m} m em:
centimetros: {valor_cm}
milimetros: {valor_mm}''')

def tabuada():
    print('Tabuada:')
    numero_desejado = int(input('Qual número deseja ver a tabuada?\n'))
    tabuada = [1,2,3,4,5,6,7,8,9,10]

    for numero in tabuada:
        resultado = numero_desejado * numero
        print(f'{numero} x {numero_desejado} = {resultado}')

