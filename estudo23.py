# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
# Ex.: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

numero = input("Digite um número de 0 a 9999: ")

comprimento = len(numero)

if comprimento == 4:
    unidade = numero[3]
    dezena = numero[2]
    centena = numero[1]
    milhar = numero[0]
    print(f"unidade: {unidade}")
    print(f"dezena: {dezena}")
    print(f"centena: {centena}")
    print(f"milhar: {milhar}")
elif comprimento == 3:
    unidade = numero[2]
    dezena = numero[1]
    centena = numero[0]
    print(f"unidade: {unidade}")
    print(f"dezena: {dezena}")
    print(f"centena: {centena}")
elif comprimento == 2:
    unidade = numero[1]
    dezena = numero[0]
    print(f"unidade: {unidade}")
    print(f"dezena: {dezena}")
else:
    unidade = numero
    print(f"unidade: {unidade}")
