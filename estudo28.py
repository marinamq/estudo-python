# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perder

import random

numero = random.randint(0, 5)

tentativa_usuario = int(input('Tente adivinhar o número escolhido de 0 a 5: '))

print('O numero escolhido é {} e você digitou {}'.format(numero, tentativa_usuario))

if tentativa_usuario == numero:
    print('Você venceu')
else:
    print('Você perdeu')