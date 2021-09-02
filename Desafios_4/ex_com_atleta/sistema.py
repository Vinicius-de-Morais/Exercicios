from condicionais import Validador, ImcValido


class Atleta:
    def __init__(self, altura, peso, idade):
        self.altura = altura
        self.peso = peso
        self.idade = idade
        self._imc = self.calcula_imc()

    def calcula_imc(self):
        calculo = self.peso / (self.altura ** 2)
        return round(calculo, 2)

    @property
    def imc(self):
        return self._imc

    def aptidao(self):
        resultado = Validador(ImcValido()).valida(self.imc)
        return resultado


if __name__ == '__main__':

    altura = float(input('Altura: '))
    peso = int(input('Peso: '))
    idade = input('Idade')

    atleta = Atleta(altura, peso, idade)
    atleta.aptidao()
