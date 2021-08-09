import random as r

alunos = ['Batman', 'Tony', 'Zeca Pagodinho', 'Bruce']

def seleciona_aluno(lista):
   print(f'O aluno escolhido é {r.choice(lista)}') 

seleciona_aluno(alunos)