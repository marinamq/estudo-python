import math

# para importar um método específico, é feito dessa forma:
# from math import sqrt // e para chamar a função faz assim: raiz = sqrt(num) // Não precisa escrever o "math."sqrt
# caso queira importar mais de um método, é assim que faz:
# from math import sqrt, ceil

num = int(input('Digite um número: '))

raiz = math.sqrt(num)

print('A raiz de {} é igual a {}'.format(num, raiz))

#sqrt -> calcula a raíz
#ceil -> arredonda para cima
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
#floor -> arredonda para baixo
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))

#==========================================================================================
frase = 'Curso em Video Python'
frase1 = '   Aprenda Python  '

# fatiamento
print(frase[::2])
print(frase[9])
print(frase[9:13]) #vai pegar do 9 até o 12. Não pega o último número. No range o último valor não entra na contagem.
print(frase[9:21])
print(frase[9:21:2]) # vai de 9 até 21, pulando de 2 em 2
print(frase[:5]) # é a mesma coisa que [0:5]
print(frase[15:]) # inicia no 15 e vai até o último caractere
print(frase[9::3]) # inicia no 9 e vai até o final, pulando de 3 em 3

# Análise

print(len(frase)) # função len (vem de lengh) vai mostrar o comprimento da frase
print(frase.count('o')) # vai contar quantas vezes aparece a letra o
print(frase.count('o', 0, 13)) # vai fazer uma contagem com fatiamento. Vai contar quantas vezes aparece a letra o, mas no trecho do 5 até o 13 (lembrando q vai considerar do 5 ao 12).
print(frase.find('deo')) # vai dizer onde inicia deo
print(frase.find('Android')) # se receber o valor -1, significa que a string não foi encontrada
print('Curso' in frase) # vai responder True ou False

#Transformação 

print(frase.replace('Python', 'Android')) # vai substituir a primeira palavra, e substituir pela segunda
print(frase.upper()) # deixa tudo maiúsculo
print(frase.lower()) # deixa tudo em minúsculo
print(frase.capitalize()) # Vai deixar só o primeiro caractere maiúsculo e o restante minúsculo
print(frase.title()) #Vai deixar a primeira letra de cada palavra maiúsculo

print(frase1)
print(frase1.strip()) # remove os espaços inúteis no início e no final da string
print(frase1.rstrip()) # remove somente os espaços no final (a direita)
print(frase1.lstrip()) # remove somente os espaços no início (a esquerda)

# Divisão

print(frase.split()) # divisão na string onde tem espaços e gera uma lista com as palavras isoladas

# Junção
frase2 = frase.split()
print('-'.join(frase2)) # Junta as palavras divididas pelo split usando o -

# ======================================================================================================

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

#=========================================================================================================================
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

#================================================================================================================================
# LISTAS DENTROS DE LISTAS

# dados = []
# dados.append("Pedro")
# dados.append(25)
# dados.append("Maria")
# dados.append(22)
# dados.append("Joao")
# dados.append(32)
# print(dados[0])
# print(dados[1])

# pessoas = []
# pessoas.append(dados[:])
# print(pessoas)
# pessoas = [["PEDRO", 25], ["MARIA", 22], ["JOAO", 32]]
# print(pessoas[0])
# print(pessoas[0][0])
# print(pessoas[1][1])
# print(pessoas[2][0])
# print(pessoas[1])
# pessoas.clear() #vai deletar os valores das duas listas, dados e pessoas
print("=-" * 60)

galera = []
dado = []
totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade")
        totmen += 1
print(f"Temos {totmai} maiores e {totmen} menores de idade.")

# ===============================================================================================================================
# DICIONÁRIOS

dados = {}

dados = {"nome": "Pedro", "idade": 25}

print(dados["nome"])
print("=-" * 30)

# para criar novo elemento
dados["sexo"] = "M"
print(dados)
print("=-" * 30)

print(
    f"O {dados['nome']} tem {dados['idade']} anos."
)  # assim que vai tratar o dicionario no print formatado
print(dados.keys())
print(dados.values())
print(dados.items())
print("=-" * 30)

# para remover elemento
del dados["idade"]
print(dados)
print("=-" * 30)
# criar outro dicionário

filme = {"titulo": "Star wars", "ano": 1997, "diretor": "George Lucas"}

print(filme)

# valor, chave e item
print(filme.values())  # retorna todos os valores do dicionário
print(filme.keys())  # retorna as chaves
print(
    filme.items()
)  # pega todos os dados ( valores e keys ). No dicionário usa o items, não tem enumerate

for k, v in filme.items():
    print(f"O {k} é {v}")

for k in filme.keys():
    print(k)
for k in filme.values():
    print(k)

# como criar um dicionário dentro de uma lista
# brasil = []

# estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
# estado2 = {"uf": "São Paulo", "sigla": "SP"}

# brasil.append(estado1)
# brasil.append(estado2)

# print(estado1) # vai mostrar o dicionário estado 1
# print(estado2) # vai mostrar o dicionário estado 2
# print(brasil) # mostra a lista com os 2 dicionários dentro
# print(brasil[0])
# print(brasil[0]["uf"])

print("=-" * 60)

estado = {}
pais = []

for c in range(0, 3):
    estado["uf"] = str(input("Undade Federativa: "))
    estado["sigla"] = str(input("Sigla: "))
    pais.append(estado.copy()) # assim que faz para copiar um conteúdo
print(pais)
print("=-" * 30)
for e in pais:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")
# ou
print("=-" * 30)
for e in pais:
    for v in e.values():
        print(v, end=" ")
    print() # pula de linha
# ============================================================================================================================

