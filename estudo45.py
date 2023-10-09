# Crie um programa que faça o computador jogar JOKEMPO com você
import random

moveList = ["Pedra", "Papel", "Tesoura"]

print(
    """Escolha o seu movimento:
Papel
Tesoura
Pedra"""
)

print("-" * 10)

movimento = str(input("Digite qual será o seu movimento: "))

print("-" * 10)

pc_movimento = random.choice(moveList)


if movimento == "Papel":
    if pc_movimento == "Papel":
        print(f"{movimento} X {pc_movimento} = Empate!")
    elif pc_movimento == "Tesoura":
        print(f"{movimento} X {pc_movimento} = Você perdeu!")
    elif pc_movimento == "Pedra":
        print(f"{movimento} X {pc_movimento} = Você ganhou!")
    else:
        print("Jogada Inválida")
if movimento == "Tesoura":
    if pc_movimento == "Papel":
        print(f"{movimento} X {pc_movimento} = Você ganhou!")
    elif pc_movimento == "Tesoura":
        print(f"{movimento} X {pc_movimento} = Empate!")
    elif pc_movimento == "Pedra":
        print(f"{movimento} X {pc_movimento} = Você perdeu!")
    else:
        print("Jogada Inválida")
else:
    if pc_movimento == "Papel":
        print(f"{movimento} X {pc_movimento} = Você perdeu!")
    elif pc_movimento == "Tesoura":
        print(f"{movimento} X {pc_movimento} = Você ganhou!")
    elif pc_movimento == "Pedra":
        print(f"{movimento} X {pc_movimento} = Empate!")
    else:
        print("Jogada Inválida")
