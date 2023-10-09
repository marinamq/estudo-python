lanche = ("hamburguer", "lanche", "suco", "pudim")

print(lanche)
print(lanche[3])
print(lanche[-3])
print(lanche[:3])

for comida in lanche:
    print(f"Eu vou comer {comida}")

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")

for comida in lanche:
    print(f"Eu vou comer {comida}")
print("Comi pra caramba!")

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")
    

# mostrar em ordem
print(sorted(lanche))

#
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a+b # junta as duas tuplas
print(c)
print(len(c)) # mostra quantos itens tem na tupla
print(c.count(2)) # mostra quantas vezes o número 2 aparece
print(c.index(2)) # mostra em qual posição está o número 2 (primeira ocorrencia)
print(c.index(2, 1)) # como o primeiro 2 está na posição 0, vai começar a procurar a partir da posição 1


