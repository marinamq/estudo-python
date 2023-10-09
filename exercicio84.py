# faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# Quantas pessoas foram cadastradas
# Uma listagem com as pessoas mais pesadas
# Uma listagem com as pessoas mais leves

pessoas = []
princ = []

peso_maior = peso_menor = 0

while True:
    pessoas.append(str(input("Digite seu nome: ")))
    pessoas.append(float(input(("Digite o seu pes em kg: "))))
    if len(princ) == 0:
        peso_maior = peso_menor = pessoas[1]
    else:
        if pessoas[1] > peso_maior:
            peso_maior = pessoas[1]
        if pessoas[1] < peso_menor:
            peso_menor = pessoas[1]
    princ.append(pessoas[:])
    pessoas.clear()
    opcao = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if opcao in "N":
        break

print(f"Foram cadastradas {len(princ)} pessoas.")
print(f"O maior peso foi de {peso_maior}kg. Peso de ", end="")
for p in princ:
    if p[1] == peso_maior:
        print(f"[{p[0]}] ", end="")
print(f"\nO menor peso foi de {peso_menor} kg. Peso de ", end="")
for p in princ:
    if p[1] == peso_menor:
        print(f"[{p[0]}] ", end="")
