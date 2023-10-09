# Refaça o desafio 51, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressao usando a estrutura while

# Exercicio 51 - Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 termos dessa progressão

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
decimo = termo
cont = 1

while cont <= 10:
    print(f"{termo} -> ", end="")
    termo += razao
    cont += 1
print("Fim")
