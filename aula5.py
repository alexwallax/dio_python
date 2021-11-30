# aula 5 - lista e tupla

# -------------------------------lista-------------------------------------
# lista coloca entre cochetes [] 

lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
nova_lista = lista_animal * 3 
#print(lista)
#print(type(lista))
#print(lista_animal[1])
#-------------------------------------
print('----------------------------------------\n\n\n')
#-------------------------------------
# trocar o valor de uma lista
#lista_animal[0] = 'macaco'

#-------------------------------------
#imprime todos da lista_animal
for x in lista_animal: 
    print(x)
#-------------------------------------
# Soma todos os valores da lista
soma = 0
for x in lista:
    print('Valor da lista {}'.format(x))
    soma += x
print('O total somado da lista é {} '.format(soma))
#-------------------------------------
# Soma todos os valores da lista
print(sum(lista))
# mostra qual o maior valor da lista
print(max(lista))
# mostra o menor valor da lista
print(min(lista))
# menor valor referente a primeira letra
print(min(lista_animal)) 
#-------------------------------------

# verifica se existe na lista
if 'gato' in lista_animal:
    print('existe um gato na lista')
else:
    print('não existe um gato na lista')
#-------------------------------------
# imprime os valores de lista_animal 3 vezes
#print(nova_lista) 
#-------------------------------------

#incluir um valor na lista (se não existir)
#if 'lobo' in lista_animal:
#    print('existe um lobo na lista')
#else:
#    print('não existe um lobo na lista')
#    lista_animal.append('lobo')
#    print(lista_animal)

#-------------------------------------
#animal = str(input('Digite o nome de um animal'))
#if animal in lista_animal:
#    print('animal ja existe {}'.format(animal))
#else:
#    print('animal ainda não existe {}'.format(animal))
#    lista_animal.append(animal)
#    print(lista_animal)

#-------------------------------------
# retirar um item da lista (o que estiver na ultima posição)
#lista_animal.pop()
#print(lista_animal)

# retirar um item da lista (escolhendo a posição)
#lista_animal.pop(1)

# remover item da lista pelo nome
#lista_animal.remove('elefante') 
#print(lista_animal)
#-------------------------------------

# ordenar lista
print('\n\n\n')
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)

# ordenar por ordem reversa
lista_animal.reverse()
print(lista_animal)

print('----------------------------------------\n\n\n')
# -------------------------------tupla-------------------------------------

# tupla coloca entre parenteses () 

# não consegue alterar um objeto da tupla

tupla = (1, 10, 12, 14)
print(tupla[2])

# contar quantos elementos tem 
print(len(tupla))
print(len(lista_animal))

#-------------------------------------
# converter lista em tupla
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

# converter tupla em lista
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)