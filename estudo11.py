# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintála,
# sabendo que cada litro de tinta pinta uma área de  2m²

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura * altura

tinta = area / 2

print('A área da parede é {} m² e será necessário {} litros para pintá-la.'.format(area, tinta))