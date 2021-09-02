
class Mascara:
    def __init__(self, proximo):
        self.proximo = proximo

class Escolhe:
    @staticmethod
    def escolhe(cor):
        cavaleiro = Castanho(
            Preto(
                Loiro(
                    Verde(
                        Azul
                    )
                )
            )
        ).cabelo(cor)
        return cavaleiro

class Castanho(Mascara):
    def cabelo(self, cor):
        if cor == 'Castanho':
            return 'Seya de Pégasu'
        else:
            return self.proximo.cabelo(cor)

class Preto(Mascara):
    def cabelo(self, cor):
        if cor == 'Preto':
            return 'Shiryu de Dragão'
        else:
            return self.proximo.cabelo(cor)

class Loiro(Mascara):
    def cabelo(self, cor):
        if cor == 'Loiro':
            return 'Hyoga de Cisne'
        else:
            return self.proximo.cabelo(cor)

class Verde(Mascara):
    def cabelo(self, cor):
        if cor == 'Verde':
            return 'Shun de Andrômeda'
        else:
            return self.proximo.cabelo(cor)

class Azul:
    @staticmethod
    def cabelo(cor):
        if cor == 'Azul':
            return 'Ikki de Fênix'
        else:
            return f'A cor {cor} não é valida'
