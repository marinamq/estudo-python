# AULA LISTAS

# metodo .append('') adiciona o elemento no final da lista
# metodo .insert(0, '') adiciona o elemento na posição 0 (início da lista)
# del lanche[3]  - deleta o item que está na posição 3
# lanche.pop(3) - se deixar vazio (lanche.pop()), vai deletar o último item
# lanche.remove('pizza') - deleta pelo nome do elemento, e não o índice
# se tentar remover um item que não existe na lista, vai dar um erro.

lanche = ["pizza", "hamburguer", "sorvete"]
print(lanche)
print('*' * 30)

if 'pizza' in lanche:
    lanche.remove("pizza")
print(lanche)
print('*' * 30)

lanche.append('pudim')
print(lanche)
print('*' * 30)

del lanche [1]
print(lanche)
print('*' * 60)


# criar lista atraves de range
valores = list(range(4, 11))
print(valores)
print('*' * 30)

valores1 = [8, 2, 5, 4, 9, 3, 0]
print(valores1)
print('*' * 30)
# colocar na ordem crescente
valores1.sort()
print(valores1)
print('*' * 30)
# colcoar na ordem reversa
valores1.sort(reverse=True)
print(valores1)
print('*' * 30)
# tamanho da lista
print(len(valores1))


print("Aula prática")

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
print(num)
num.sort(reverse=True)
num.insert(2, 0)
print(num)
print(f"a lista tem {len(num)} elementos")
num.pop()
print(num)
num.pop(2)
print(num)
num.insert(1, 5)
print(num)
num.remove(5) # varre a lista do início e elimina o primeiro número
print(num)

# mostrar a lista mais bonitinha

valores2 = []

valores2.append(5)
valores2.append(9)
valores2.append(4)
print(valores2) # senão quer mostrar dessa forma


for v in valores2:
    print(f"os valores da lista são {v}",)

# para mostrar os valores e a chave/índice

for c, v in enumerate(valores2):
    print(f"Na posição {c} encontrei o valor {v}")



# ler dados inseridos pelo teclado e colcocar dentro da lista

# valores3 = []
# for cont in range (0, 5):
#     valores3.append(int(input("Digite um valor: ")))
# print(valores3)

# peculiaridade do python na lista
a = [2, 3, 4, 7]
b = a
b[2] = 8 # quando duas listas são iguais, o python faz uma ligação entre elas, e o que modifica em uma, modifica na outra
print(f"Lista A: {a}")
print(f"Lista B: {b}")

c = [2, 3, 4, 7]
d = c[:]
d[2] = 8
print(f"Lista C: {c}")
print(f"Lista D: {d}")

