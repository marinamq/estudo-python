# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 - binário / 2 - octal / 3 - hexadecimal

numero = int(input('Digite um número inteiro: '))

print('''Escolha o método de conversão: 
1 - binário
2 - octal
3 - hexadecimal''')

metodo = int(input('Digite o método escolhido: '))

if metodo == 1:
    print(bin(numero)[2:])
elif metodo == 2:
    print(oct(numero)[2:])
elif metodo == 3:
    print(hex(numero)[2:])
else:
    print('Opção incorreta')
