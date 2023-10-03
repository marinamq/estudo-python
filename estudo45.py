# Crie um programa que faça o computador jogar JOKEMPO com você
import random

moveList = ['Pedra', 'Papel', 'Tesoura']

print('''Escolha o seu movimento:
Papel
Tesoura
Pedra''')

print('-' * 10)

movimento = str(input('Digite qual será o seu movimento: '))

print('-' * 10)

pcMovimento = (random.choice(moveList))


if movimento == 'Papel':
    if pcMovimento == 'Papel':
        print('{} X {} = Empate!'.format(movimento, pcMovimento))
    elif pcMovimento == 'Tesoura':
        print('{} X {} = Você perdeu!'.format(movimento, pcMovimento))
    elif pcMovimento == 'Pedra':
        print('{} X {} = Você ganhou!'.format(movimento, pcMovimento))
    else:
        print('Jogada Inválida')
if movimento == 'Tesoura':
    if pcMovimento == 'Papel':
        print('{} X {} = Você ganhou!'.format(movimento, pcMovimento))
    elif pcMovimento == 'Tesoura':
        print('{} X {} = Empate!'.format(movimento, pcMovimento))
    elif pcMovimento == 'Pedra':
        print('{} X {} = Você perdeu!'.format(movimento, pcMovimento))
    else:
        print('Jogada Inválida')
else:
    if pcMovimento == 'Papel':
        print('{} X {} = Você perdeu!'.format(movimento, pcMovimento))
    elif pcMovimento == 'Tesoura':
        print('{} X {} = Você ganhou!'.format(movimento, pcMovimento))
    elif pcMovimento == 'Pedra':
        print('{} X {} = Empate!'.format(movimento, pcMovimento))
    else:
        print('Jogada Inválida')