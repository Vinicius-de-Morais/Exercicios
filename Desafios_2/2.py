from validate_email import validate_email
import json


class Cadastro:
    def __init__(self, email, nome, telefone, idade):
        if self.valida(email):
            self.email = email
            self.nome = nome
            self.telefone = self.formata_telefone(telefone)
            self.idade = idade
        else:
            raise ValueError('E-mail inválido')

    # Valida se o email é valido e retorna True or False
    @staticmethod
    def valida(email):
        validador = validate_email(email)
        return validador

    def formata_telefone(self, telefone):
        mascara = f'{telefone[0]} {telefone[1:6]}-{telefone[5:]}'
        return mascara

    # Regista os usuarios em um arquivo
    def registra(self, modo='json'):
        if modo == 'json':
            usuario = self.__dict__
            caminho = 'usuarios.json'
            with open(caminho, 'a') as arquivo:
                json.dump(usuario, arquivo, indent="\t")
        elif modo == 'csv':
            caminho = 'usuarios.csv'
            email = self.email
            nome = self.nome
            telefone = self.telefone
            idade = self.idade
            formatacao = f'{email},{nome},{telefone},{idade}\n'
            with open(caminho, 'a', encoding='latin_1') as arquivo:
                arquivo.write(formatacao)


def main():
    email = input('E-mail:  ')
    nome = input('Nome:  ')
    telefone = input('Telefone:  ')
    idade = input('Idade:  ')
    pessoa = Cadastro(email, nome, telefone, idade)
    pessoa.registra('csv')
    pessoa.registra()


if __name__ == '__main__':
    main()
