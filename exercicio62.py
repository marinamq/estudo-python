# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disse que quer mostrar 0 termos

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
decimo = termo
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo} -> ", end="")
        termo += razao
        cont += 1
    print("Pausa")
    mais = int((input("Quantos termos você quer mostrar a mais? ")))

print("FIM")
