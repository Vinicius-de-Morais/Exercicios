def saudar():
    boas_vindas = int(input('''
1 - Boas vindas em Português
2 - Welcome in English
3 - Boas vindas zica
'''))

    if boas_vindas == 1:
        print('Seja Bem Vindo!')
    elif boas_vindas == 2:
        print('Be Welcome')
    elif boas_vindas == 3:
        print('Que isso lek TMJ!')
saudar()