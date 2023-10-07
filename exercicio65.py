# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a media entre todos os valores e qual foi o maior e o menor valores lidos.
# o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

resposta = "S"
cont = soma = maior = menor = 0

while resposta in "Ss":
    numero = int(input("Digite um número: "))
    cont += 1
    soma += numero
    if cont == 1:
        menor = maior = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = (
        str(input("Deseja continuar a digitar valores [S/N]: ")).upper().strip()[0]
    )

media = soma / cont
print(f"A média entre todos os valores é de {media:.2f}")
print(f"O maior número é {maior} e o menor número é {menor}")
