# Desenvolva uma lógica que leia o peso e a altura de uma pessa e calcule o seu imc
# abaixo de 18.5 = abaixo do Peso
# 18.5 e 25: peso ideal
# 25 a 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade morbida


peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura**2)

if imc < 18.5:
    print(f"Seu IMC é {imc:.1f} e você está abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print(f"Seu IMC é {imc:.1f} e você está com o peso ideal")
elif imc >= 25 and imc < 30:
    print(f"Seu IMC é {imc:.1f} e você está com sobrepeso")
elif imc >= 30 and imc < 40:
    print(f"Seu IMC é {imc:.1f} e você está com obesidade")
else:
    print(f"Seu IMC é {imc:.1f} e você está com obesidade mórbida")
