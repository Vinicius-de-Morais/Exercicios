# Mascara para as classes
class Mascara:
    def __init__(self, proximo):
        self.proximo = proximo

class Define:
    # As classes definem os signos, e essa classe classe fornece acesso a elas
    @staticmethod
    def define(dia, mes):
        signo = Capricornio(
            Aquario(
                Peixes(
                    Aries(
                        Touro(
                            Gemeos(
                                Cancer(
                                    Leao(
                                        Virgem(
                                            Libra(
                                                Escorpiao(
                                                    Saritario(
                                                        Nada
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        ).signo(dia, mes)
        return signo

class Nada:
    @staticmethod
    def signo(dia, mes):
        return f' O dia {dia} ou o mes {mes} são invalidos'

class Capricornio(Mascara):

    def signo(self, dia, mes):
        if mes == 12 and 22 <= dia <= 31 or mes == 1 and 1 <= dia <= 20:
            return 'Shura de Capricórnio'
        else:
            return self.proximo.signo(dia, mes)

class Aquario(Mascara):

    def signo(self, dia, mes):
        if mes == 1 and 21 <= dia <= 31 or mes == 2 and 1 <= dia <= 18:
            return 'Camus de Aquário'
        else:
            return self.proximo.signo(dia, mes)

class Peixes(Mascara):

    def signo(self, dia, mes):
        if mes == 2 and 19 <= dia <= 29 or mes == 3 and 1 <= dia <= 19:
            return 'Afrodite de Peixes'
        else:
            return self.proximo.signo(dia, mes)

class Aries(Mascara):

    def signo(self, dia, mes):
        if mes == 3 and 20 <= dia <= 31 or mes == 4 and 1 <= dia <= 20:
            return 'Mu de Áries'
        else:
            return self.proximo.signo(dia, mes)

class Touro(Mascara):

    def signo(self, dia, mes):
        if mes == 4 and 21 <= dia <= 30 or mes == 5 and 1 <= dia <= 20:
            return 'Aldebaran de Touro'
        else:
            return self.proximo.signo(dia, mes)

class Gemeos(Mascara):

    def signo(self, dia, mes):
        if mes == 5 and 21 <= dia <= 31 or mes == 6 and 1 <= dia <= 20:
            return 'Saga de Gêmeos'
        else:
            return self.proximo.signo(dia, mes)

class Cancer(Mascara):

    def signo(self, dia, mes):
        if mes == 6 and 21 <= dia <= 30 or mes == 7 and 1 <= dia <= 21:
            return 'Máscara da Morte de Câncer'
        else:
            return self.proximo.signo(dia, mes)

class Leao(Mascara):

    def signo(self, dia, mes):
        if mes == 7 and 22 <= dia <= 31 or mes == 8 and 1 <= dia <= 22:
            return 'Aiolia de Leão'
        else:
            return self.proximo.signo(dia, mes)

class Virgem(Mascara):

    def signo(self, dia, mes):
        if mes == 8 and 23 <= dia <= 31 or mes == 9 and 1 <= dia <= 22:
            return 'Shaka de Virgem'
        else:
            return self.proximo.signo(dia, mes)

class Libra(Mascara):

    def signo(self, dia, mes):
        if mes == 9 and 23 <= dia <= 30 or mes == 10 and 1 <= dia <= 22:
            return 'Dohko de Libra'
        else:
            return self.proximo.signo(dia, mes)

class Escorpiao(Mascara):

    def signo(self, dia, mes):
        if mes == 10 and 23 <= dia <= 31 or mes == 11 and 1 <= dia <= 21:
            return 'Milo de Escorpião'
        else:
            return self.proximo.signo(dia, mes)

class Saritario(Mascara):

    def signo(self, dia, mes):
        if mes == 11 and 22 <= dia <= 30 or mes == 12 and 1 <= dia <= 21:
            return 'Aiolos de Sagitário'
        else:
            return self.proximo.signo(dia, mes)
