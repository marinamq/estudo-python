# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex. Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = str(input('Digite o seu nome completo: '))

nome1 = nome.split()

print('primeiro = ', nome1[0])
print('último = ', nome1[-1])
