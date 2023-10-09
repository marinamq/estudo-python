# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angulo = float(input("Digite o valor do ângulo: "))

cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(
    f"O valor do cosseno é {cosseno:.2f}, de seno é {seno:.2f} e da tangente é {tangente:.2f}."
)
