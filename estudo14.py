# Escreva um programa que converta uma temperatura digitada em °C e converta para °F. Sendo formula: (°C * 9)/ 5) + 32
temperatura_celsius = float(input('Digite a temperatura em celsius: '))

temperatura_fahrenheit = ((temperatura_celsius * 9) / 5) + 32

print('A temperatura de {}°C é {}°F'.format(temperatura_celsius, temperatura_fahrenheit))