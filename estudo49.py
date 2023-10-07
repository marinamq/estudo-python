# Refaça o desafo 09: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada. Mostrando a tabuada de um número que o usuário escolher, só que agora
# utilizando o laço FOR

n = int(input('Digite um número: '))

for c in range(1, 11):
    r = c * n
    print(f'{c:2} x {n} = {r:2}')

# print('{} x 1 = {}'.format(n, n*1))
# print('{} x 2 = {}'.format(n, n*2))
# print('{} x 3 = {}'.format(n, n*3))
# print('{} x 4 = {}'.format(n, n*4))
# print('{} x 5 = {}'.format(n, n*5))
# print('{} x 6 = {}'.format(n, n*6))
# print('{} x 7 = {}'.format(n, n*7))
# print('{} x 8 = {}'.format(n, n*8))
# print('{} x 9 = {}'.format(n, n*9))
# print('{} x 10 = {}'.format(n, n*10))
