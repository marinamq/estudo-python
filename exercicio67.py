# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usário.
# O programa será interrompido quando o número solicitado for negativo


while True:
    num = int(input("Quer ver a tabuada de qual valor: "))
    print("-" * 30)
    if num < 0:
        break
    for c in range(1, 11):
        resultado = c * num
        print(f"{c:2} x {num} = {resultado:2}")
    print("-" * 30)
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")
