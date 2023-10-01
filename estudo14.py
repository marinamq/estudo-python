# Escreva um programa que converta uma temperatura digitada em °C e converta para °F. Sendo formula: (°C * 9)/ 5) + 32
temperaturaCelsius = float(input('Digite a temperatura em celsius: '))

temperaturaFahrenheit = ((temperaturaCelsius * 9) / 5) + 32

print('A temperatura de {}°C é {}°F'.format(temperaturaCelsius, temperaturaFahrenheit))