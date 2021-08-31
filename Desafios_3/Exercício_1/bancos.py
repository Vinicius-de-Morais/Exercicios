# Implementação das classes e lógicas dos bancos

class BancodoBrasil:

    def taxa(self, valor):
        return valor + 10.45

    def exibe(self):
        return '1 - Banco do Brasil'

class CaixaEconomicaFederal:

    def taxa(self, valor):
        return valor + 10.0

    def exibe(self):
        return '2 - Caixa Econômica Federal'

class Itau:

    def taxa(self, valor):
        return valor + 10.50

    def exibe(self):
        return '3 - Itaú'

class Bradesco:

    def taxa(self, valor):
        return valor + 10.45

    def exibe(self):
        return '4 - Bradesco'
