import string
import os

class SenhaUser:

    def __init__(self, senha):

        if self.verifica(senha):
            self._senha = senha
    
    @property
    def senha(self):
        return self._senha

    def verifica(self, senha):

        if len(senha) == 9:
            return True
        else:
            raise ValueError('A senha deve conter 9 caracteres')


class Decodificador:

    def decodifica(lista):
        palavra = []
        tentativas = 0
        #criando uma lista com todos os caracteres possíveis
        caracteres = [letra for letra in string.printable]
        #criando um loop
        while True:

            for item in lista.senha:
                # verificando os itens da senha para apendar os certos
                if item in caracteres:
                    tentativas += 1 + caracteres.index(item) # adiciona-se 1 para corrigir o index
                    palavra.append(item)

            if len(palavra) == 9:
                os.system('cls')
                print(f'''Essa foi fácil.
A senha era: {lista.senha}
Tentativas: {tentativas}''')
                return False


if __name__ == '__main__':
    
    input_senha = input('Qual a senha? (ela deve conter 9 caractéres)')

    senha = SenhaUser(input_senha)
    
    Decodificador.decodifica(senha)
    