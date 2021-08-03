
def pintura():
    
    print('Pintura')
    largura = float(input('Qual a lagura da parede em Metros?  '))
    altura = float(input('Qual a altura em Metros?  '))
    area = round(largura * altura, 2)
    tinta = int(area / 2)

    print(f'''
A parede tem {area} m²
Para sua pintura será necessário 
aproximadamente {tinta} litros de tinta''')

pintura()

    