# Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if (num1 > num2 and num1 > num3) and num2 > num3:
    print('O maio número é {} e o menor número é {}'.format(num1, num3))
elif (num1 > num2 and num1 > num3) and num3 > num2:
    print('O maio número é {} e o menor número é {}'.format(num1, num2))
elif (num2 > num1 and num2 > num3) and num2 > num3:
    print('O maio número é {} e o menor número é {}'.format(num2, num3))
elif (num2 > num1 and num2 > num3) and num3 > num2:
    print('O maio número é {} e o menor número é {}'.format(num2, num2))
elif (num3 > num1 and num3 > num2) and num2 > num1:
    print('O maio número é {} e o menor número é {}'.format(num3, num1))
else:
    print('O maio número é {} e o menor número é {}'.format(num3, num2))
    