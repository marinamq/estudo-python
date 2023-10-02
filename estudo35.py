# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triangulo

reta1 = int(input('Digite o tamanho da primeira reta: '))
reta2 = int(input('Digite o tamanho da segunda reta: '))
reta3 = int(input('Digite o tamanho da terceira reta: '))

if reta1 + reta2 > reta3:
    print('forma triangulo')
elif reta1 + reta3 > reta2:
    print('forma triangulo')
elif reta3 + reta2 > reta1:
    print('forma triangulo')
else:
    print('não forma triangulo')