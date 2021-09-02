from cond_signos import Define
from cond_cabelo import Escolhe
import os

class Pessoa:
    def __init__(self, nome, idade, data_de_nascimento):
        self._nome = nome.title()
        self.idade = idade
        self._data_de_nascimento = data_de_nascimento
        self.cavaleiro = self.define_cavaleiro()

    @property
    def data_de_nascimento(self):
        return self._data_de_nascimento

    @property
    def ano(self):
        #                         dd/mm/aaaa
        ano = self.data_de_nascimento[6:]
        return ano

    @property
    def dia(self):
        dia = self._data_de_nascimento[0:2]
        return int(dia)

    @property
    def mes(self):
        mes = self._data_de_nascimento[3:5]
        return int(mes)

    def define_cavaleiro(self):
        if self.idade > 18:
            cavaleiro = Define.define(self.dia, self.mes)
        else:
            print('Não tema, você não tem idade para ser um cavaleiro de ouro, porém você pode ser um de Bronze')
            print('Se você pudesse escolher a cor do seu cabelo qual seria?')
            cor = input('Castanho - Preto - Loiro - Verde - Azul\n').title().strip()
            cavaleiro = Escolhe().escolhe(cor)
        return cavaleiro

    def __str__(self):
        return f'''Nome: {self._nome}
Idade: {self.idade}
Cavaleiro: {self.cavaleiro}
'''

if __name__ == '__main__':

    nome = input('Nome: ')
    idade = int(input('Idade: '))
    nascimento = input('Data de Nascimento: ')

    pessoa = Pessoa(nome, idade, nascimento)
    os.system('cls')
    print(pessoa)
