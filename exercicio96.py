# Faça um programa que tenha uma função chamada aera()
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno

def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m².')


print('Controle de Terrenos')
print('-'*20)

larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))

area(larg, comp)
