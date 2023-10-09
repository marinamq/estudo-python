# Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if (num1 > num2 and num1 > num3) and num2 > num3:
    print(f"O maio número é {num1} e o menor número é {num3}")
elif (num1 > num2 and num1 > num3) and num3 > num2:
    print(f"O maio número é {num1} e o menor número é {num2}")
elif (num2 > num1 and num2 > num3) and num2 > num3:
    print(f"O maio número é {num2} e o menor número é {num3}")
elif (num2 > num1 and num2 > num3) and num3 > num2:
    print(f"O maio número é {num2} e o menor número é {num2}")
elif (num3 > num1 and num3 > num2) and num2 > num1:
    print(f"O maio número é {num3} e o menor número é {num1}")
else:
    print(f"O maio número é {num3} e o menor número é {num2}")
