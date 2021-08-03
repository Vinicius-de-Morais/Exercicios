import exercicios_ate_10 as exe
print('Seja bem vindo!')

seleciona = int(input('''O que deseja fazer?
1 - Somar, 2 - Informações sobre o numero,
3 - Média, 4 - Conversor de metros
5 - Tabuada \n'''))

if seleciona == 1:
    exe.soma()
elif seleciona == 2:
    exe.informacoes()
elif seleciona == 3:
    exe.calcula_media()
elif seleciona == 4:
    exe.conversor()
elif seleciona == 5:
    exe.tabuada()
else:
    print('Opção invalida!')
