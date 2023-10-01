# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo, calcule e mostre o comprimento da hipotenusa (a² = b² + c²)

import math

catetoOposto = float(input("Digite o comprimento do cateto oposto: "))
catetoAdjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = math.hypot(catetoOposto, catetoAdjacente)

print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))
