# conjunto = {1, 2, 3, 4} # não permite duplicidade
# conjunto.add(5) # adicionando um elemento no conjunto
# conjunto.discard(2) # remover um elemento
# print(type(conjunto)) # verificando o tipo
# print(conjunto)


conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
# união dos conjuntos (tudo do conjunto + tudo do conjunto2)
conjunto_uniao = conjunto.union(conjunto2)
print('União {}'.format(conjunto_uniao))

# interseccao dos conjuntos (o que tem no conjunto, e também no conjunto2)
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção {}'.format(conjunto_interseccao))

# diferença (o que tem de diferente do conjunto para o conjunto2)
conjunto_diferenca1 = conjunto.difference(conjunto2)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))

conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))

# diferença simétrica (não mostra o que tem nos dois ao mesmo tempo)
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

# pertinéncia - retorna true se conjunto_a estiver dentro de conjunto_b 
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('a é subconjunto de B: {}'.format(conjunto_subset))

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é superconjunto de a: {}'.format(conjunto_superset))

# converter lista para conjunto
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)
print(conjunto_animais)

# converter conjunto para lista
lista_animais = list(conjunto_animais)
print(lista_animais)

