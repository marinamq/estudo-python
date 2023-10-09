# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# Quantas vezes apareceu o valor 9
# Em que posição foi digitado o primeiro valor 3
# Quais foram os números pares


numeros = (
    int(input("Digite o primeiro número: ")),
    int(input("Digite o segundo número: ")),
    int(input("Digite o terceiro número: ")),
    int(input("Digite o quarto número: ")),
)

print(f"Você digitou os números {numeros}")

if 9 in numeros:
    print(f"O valor 9  apareceu {numeros.count(9)} vezes")
else:
    print("O valor 9 não foi digitado")

if 3 in numeros:
    print(f"O valor 3 apareceu pela primeira vez na posição {numeros.index(3)+1}")
else:
    print("O valor 3 não foi digitado")

print("Os valores pares digitados foram: ", end="")

for n in numeros:
    if n % 2 == 0:
        print(n, end=" ")
