# Crie um programa que leia uma frase qualquer e diga se ela é palindromo, desconsiderando os espaços. palindromo: lê de frente pra tras e tras pra frente e é a mesma palavra. 
# Ex apos a sopa / a sacada da casa / a torre da derrota

frase = str(input('Digite uma frase: '))
frase2 = frase.replace(' ', '').lower()

frase_invertida = frase2[::-1]

print(frase2, frase_invertida)

if frase2 == frase_invertida:
    print('A frase: {} é um palíndromo'.format(frase))
else:
    print('A frase: {} não é um palíndromo'.format(frase))


