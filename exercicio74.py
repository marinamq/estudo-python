# crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

numero = (
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
)

print(f"eu sorteei os valores {numero}")

print(f"O maior valor sorteado foi {max(numero)}")
print(f"O menor valor sorteado foi {min(numero)}")
