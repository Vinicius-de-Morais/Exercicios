class ImcValido:

    def valida(self):
        quantidade = int(input('Quantas vezes você treina por semana?  '))
        tempo = int(input('Aproximadamente quantos minutos por sessão de treino?  '))
        resultado = quantidade * tempo

        if resultado >= 300:
            print('''Parabéns, você passou em todos os nossos testes, agora você fará um teste pessoal em nossa sede,
favor comparecer ao endereço: Rua dos Atletas, 43, Bairro do Futebol. Nos vemos lá!''')
        else:
            print('Muito obrigado, agradecemos a sua participação!')

class Validador:

    def __init__(self, prossimo_passo):
        self.prossimo_passo = prossimo_passo

    def valida(self, imc):
        if imc < 24.9:
            return self.prossimo_passo.valida()
        else:
            print('''Seu imc é maior que 24,9. Primeiramente normalize sua forma física, e só depois
volte a se inscrever''')

