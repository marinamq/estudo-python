# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
num = int(input('Digite um número: '))
total_divisiveis = 0
for c in range(1, num + 1):
    if num % c == 0:            
        print('\033[33m', end='')
        total_divisiveis += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\nO número {} foi divísivel {} vezes'.format(num, total_divisiveis))
if total_divisiveis == 2:
    print('O número {} é primo'.format(num))
else:
    print('O número {} não é primo'.format(num))