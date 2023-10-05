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

pc_movimento = (random.choice(moveList))


if movimento == 'Papel':
    if pc_movimento == 'Papel':
        print('{} X {} = Empate!'.format(movimento, pc_movimento))
    elif pc_movimento == 'Tesoura':
        print('{} X {} = Você perdeu!'.format(movimento, pc_movimento))
    elif pc_movimento == 'Pedra':
        print('{} X {} = Você ganhou!'.format(movimento, pc_movimento))
    else:
        print('Jogada Inválida')
if movimento == 'Tesoura':
    if pc_movimento == 'Papel':
        print('{} X {} = Você ganhou!'.format(movimento, pc_movimento))
    elif pc_movimento == 'Tesoura':
        print('{} X {} = Empate!'.format(movimento, pc_movimento))
    elif pc_movimento == 'Pedra':
        print('{} X {} = Você perdeu!'.format(movimento, pc_movimento))
    else:
        print('Jogada Inválida')
else:
    if pc_movimento == 'Papel':
        print('{} X {} = Você perdeu!'.format(movimento, pc_movimento))
    elif pc_movimento == 'Tesoura':
        print('{} X {} = Você ganhou!'.format(movimento, pc_movimento))
    elif pc_movimento == 'Pedra':
        print('{} X {} = Empate!'.format(movimento, pc_movimento))
    else:
        print('Jogada Inválida')