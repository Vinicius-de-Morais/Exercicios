import random as r
import os

print('Jogo de adivinhação:')
numero_secreto = r.randrange(0, 101)
tentativa = 0
rodada = 1
pontos = 1000

print('Qual a dificuldade?')
nivel = int(input('(1) Fácil (2) Médio (3) Difícil: \n'))
if(nivel == 1):
    dificuldade = 'Fácil'
    tentativa = 20
elif(nivel == 2):
    dificuldade = 'Médio'
    tentativa = 10
else:
    dificuldade = 'Difícil'
    tentativa = 5

limpa_terminal = os.system('cls') or None
limpa_terminal

print(f'Pontuação: {pontos}')

#Jogo
for rodada in range(1, tentativa + 1):
    print(f'''Dificuldade: {dificuldade}
tentativas: {rodada} de {tentativa}''')

    chute = int(input('Digite um número entre 1 e 100 : \n'))

    print("Você chutou", chute)

    if(chute < 1 or chute > 100):
        print('Por favor, digite um número válido')
        continue

    acertou     = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto
#não sei pq tive que chamar 2 vezes, tava dando erro.
    limpa_terminal = os.system('cls') or None

    if (acertou):
        limpa_terminal
        print(f'''Parabéns, você é o GRANDE VENCEDOR!!! o número era {numero_secreto}
Pontuação: {pontos}''')
        break
    elif (chute_maior):
        limpa_terminal
        print('EEERROOOOOO!!! Seu chute foi MAIOR que o número secreto')
        pontos = pontos - abs(numero_secreto - chute)
    elif (chute_menor):
        limpa_terminal
        print('EEERROOOOOO!!! Seu chute foi MENOR que o número secreto')
        pontos = pontos - abs(numero_secreto - chute)
    if (rodada == tentativa):
        limpa_terminal
        print(f'''Perdeste amigo! o número secreto era {numero_secreto}
Pontuação: {pontos}''')

print('Fim de Jogo!')