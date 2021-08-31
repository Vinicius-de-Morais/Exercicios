from datetime import datetime
from bancos import BancodoBrasil, CaixaEconomicaFederal, Itau, Bradesco
import os

# Lista implementada fora da classe para ser acessada pelo if
bancos = [BancodoBrasil(), CaixaEconomicaFederal(), Itau(), Bradesco()]

class RealizaPagamento:
    def __init__(self, banco, valor):
        banco_escolhido = bancos[int(banco) - 1]
        self._banco = banco_escolhido
        self._valor = banco_escolhido.taxa(valor)
        self.momento_cadastro = datetime.today()
        self.registra()

    def data_formatada(self):
        return self.momento_cadastro.strftime('%d/%m/%Y  %H:%M')

# Salva a transação em um .csv
    def registra(self):
        caminho = 'Exercício_1/pagamentos.csv'
        banco = self._banco.exibe()
        valor = self._valor
        momento = self.data_formatada()
        formatacao = f'Banco: {banco}, Valor: {valor}, Registro: {momento}\n'
        with open(caminho, 'a', encoding = 'UTF-8') as arquivo:
            arquivo.write(formatacao)

    def __str__(self):
        return f'''Pagamento realizado
Banco: {self._banco.exibe()}
Valor (com taxa): {self._valor}
Data do registro: {self.data_formatada()}'''

# Código para rodas
if __name__ == '__main__':

    print('Qual o banco para a tranzação?')
    for x in bancos:
        print(x.exibe())

    banco_user = int(input('Digite o código:  '))
    valor_user = float(input('Digite o valor da transação: '))
    os.system('cls') #limpa o terminal

    transacao = RealizaPagamento(banco_user, valor_user)
    print(transacao)
