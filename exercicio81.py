# crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# quantos números foram digitados
# a lista de valores ordenada de forma decrescente
# Se o valor 5 foi digitado e está ou não na lista

numero = []
cont = 0
option = "S"

while option == "S":
    numero.append(int(input("Digite um valor: ")))
    cont += 1
    option = str(input("Deseja continuar [S/N]: ")).upper().strip()[0]
while option not in ("S", "N"):
    option = str(input("Deseja continuar [S/N]: ")).upper().strip()[0]

print(f"Foram digitados {cont} números.")

numero.sort(reverse=True)
print(numero)

if numero.count(5) > 0:
    print(f"o número 5 está na lista e foi digitado {numero.count(5)} vezes.")
else:
    print("O número 5 não foi digitado")
