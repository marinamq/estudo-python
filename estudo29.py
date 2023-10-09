# Escreva um programa que leia a velocidade de umc arro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite

velocidade = float(input("Digite a velocidade do carro em km/h: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Você estava acima da velocidade permitida. Sua multa é de R${multa:.2f}")
