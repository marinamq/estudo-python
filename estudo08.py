# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = float(input('Digite o valor em metros: '))

centimetro = n * 100
milimetro = n * 1000

print('O valor digitado em centímetros é {} cm.'.format(centimetro))
print('O valor digitado em milímetros é {} mm.'.format(milimetro))