# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impars digitados, respectivamente
# No final mostre o conteúdo das três listas digitadas
numero = []
option = "S"

while option == "S":
    numero.append(int(input("Digite um valor: ")))
    option = str(input("Deseja continuar [S/N]: ")).upper().strip()[0]
while option not in ("S", "N"):
    option = str(input("Deseja continuar [S/N]: ")).upper().strip()[0]

pares = []
impares = []

for n in numero:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

numero.sort()
print(f"A lista completa é {numero}")
pares.sort()
print(f"A lista de pares é {pares}")
impares.sort()
print(f"A lista de ímpares é {impares}")
