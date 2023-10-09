# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc

numero = float(input("Digite um número real qualquer: "))

print(f"O número {numero} tem a parte inteira {trunc(numero)}")
