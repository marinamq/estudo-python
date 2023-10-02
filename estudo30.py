# Crie um programa que leia um númro inteiro e mostre na tela se ele é PAR ou impar

numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print('{} é par'.format(numero))
else:
    print('{} é ímpar'.format(numero))