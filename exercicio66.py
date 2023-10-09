# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quandos úmeros foram digitados e qual foi a soma entre eles (desconsiderando a flag)

numero = cont = soma = 0

while True:
    numero = int(input("Digite um número [999 para parar]: "))
    if numero == 999:
        break
    cont += 1
    soma += numero

print(f"Foram digitados {cont} valores e a soma entre eles é {soma}.")
