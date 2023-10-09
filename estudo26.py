# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantes vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input("Digite uma frase: ")).strip()
repeticao = frase.count("A")
primeira_posicao = frase.find("A")
ultima_posicao = frase.rfind("A")

print(f"A letra A aparece {repeticao} vezes")
print(f"A letra A aparece pela primeira vez na posição {primeira_posicao + 1}")
print(f"A letra A aparece pela última vez na posição {ultima_posicao + 1}")
