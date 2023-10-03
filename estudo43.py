# Desenvolva uma lógica que leia o peso e a altura de uma pessa e calcule o seu imc
# abaixo de 18.5 = abaixo do Peso
# 18.5 e 25: peso ideal
# 25 a 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade morbida


peso = float(input('Digite o seu peso em kg: '))
altura= float(input('Digite sua altura em metros: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é {:.1f} e você está abaixo do peso'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.1f} e você está com o peso ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.1f} e você está com sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.1f} e você está com obesidade'.format(imc))
else:
    print('Seu IMC é {:.1f} e você está com obesidade mórbida'.format(imc))