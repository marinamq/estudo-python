# Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 termos dessa progressão

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
decimo = termo + (10 - 1) * razao

for i in range(termo, decimo + razao, razao):
    print(i, end="->")
print("Acabou")
