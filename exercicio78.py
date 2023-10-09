# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista
valores = []

for cont in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {cont}: ")))

print(f"O maior valor é {max(valores)} e está nas posições ", end="")
for i, v in enumerate(valores):
    if v == max(valores):
        print(f"{i}...", end="")

print(f"\nO menor valor é {min(valores)} e está nas posições ", end="")
for i, v in enumerate(valores):
    if v == min(valores):
        print(f"{i}...", end="")
