# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre=os em uma lista única que mantenha os valores pares e impares separados.
# No final mostre os valores pares e ímpares em ordem crescente

numeros = [[], []]


for num in range(1, 8):
    num = (int(input(f"Digite o {num}º valor: ")))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print("=-" * 40)
print(f"Os valores pares digitados foram: {numeros[0]}")
print(f"Os valores ímpares digitados foram: {numeros[1]}")
