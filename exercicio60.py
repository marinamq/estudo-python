# Faça um programa que leia um número qualquer e mostre o seu fatorial

# --------------usando módulo --------------

# from math import factorial

# numero = int(input('Digite um número: '))
# fator = factorial(numero)

# print('O fatorial de {} é {}'.format(numero, fator))


# -------------- sem usar o módulo ------------------------

numero = int(input("Digite um número: "))
cont = numero
fator = 1

while cont > 0:
    print(f"{cont}", end="")
    print(" x " if cont > 1 else " = ", end="")
    fator *= cont
    cont -= 1
print(f"{fator}")
