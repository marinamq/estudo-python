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

