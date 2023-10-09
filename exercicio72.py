# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.

contagem = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)

numero = int(input("Digite um número entre 0 e 20: "))
while 0 > numero > 20:
    numero = int(input("Tente novamente. Digite um número entre 0 e 20: "))
print(f"Você digitou o número {contagem[numero]}.")
