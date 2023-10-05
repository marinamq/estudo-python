# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. So o valor digitado for ímpar, desconsidere-o

for c in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        num += num
        print(num)