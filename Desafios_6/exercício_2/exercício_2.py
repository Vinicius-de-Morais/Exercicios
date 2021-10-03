import random as r
import os
import winsound
from time import sleep

class PalavraSecreta:
    def __init__ (self):
        self.palavra = None
        self.anagrama = None

    def escolhe_palavra(self):
        
        palavras = []
        # abre o arquivo txt
        with open('Desafios_6\exercício_2\palavras.txt', 'r', encoding='UTF-8') as arquivo:
            for linha in arquivo:
                palavras.append(linha.strip())

        # sorteia um indice aleatório
        numero = r.randrange(0, len(palavras))
        palavra = palavras[numero].upper()
        anagrama = []

        # embaralha a palavra
        for letra in palavra:
            numero = r.randrange(0, len(palavra))
            anagrama.insert(numero, letra)
            
        self.palavra = palavra
        self.anagrama = anagrama 

    def joga(self):

        rodadas = 0
        pontuação = 0

        while (rodadas != 5):
            self.escolhe_palavra()

            # coisas para personalizar o funcionamento
            os.system('cls')
            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION) #faz som de perggunta
            
            # mensagem de inicio
            print(f'Rodada: {rodadas}  Pontuação: {pontuação}')
            print('Analise o anagrama:')
            print(*self.anagrama, sep=' ')
            resposta = input('Qual a palavra?\n').upper()

            if resposta == self.palavra:
                winsound.MessageBeep(winsound.MB_OK) #faz som de acerto
                print('Acertou!')
                sleep(0.7) # para dar tempo de exibir a mensagem
                pontuação += 1
            else:
                winsound.MessageBeep(winsound.MB_ICONHAND) #faz som de erro
                print('Errou!!')
                sleep(0.7) 
                pontuação -= 1
            
            rodadas += 1                              
        
        os.system('cls')
        winsound.MessageBeep(winsound.MB_ICONASTERISK) #faz som final
        print('**FIM DE JOGO**')
        print(f'Pontuação final: {pontuação}')
        
                
            

            
        
if __name__ == "__main__":

    jogo = PalavraSecreta()
    jogo.joga()

