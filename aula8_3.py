
# lambda - função anomina
contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))


soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplicacao = lambda a, b: a * b
divisao = lambda a, b: a / b

print(soma(5, 10))
print(subtracao(55, 5))
print(multiplicacao(2, 16))
print(divisao(50, 10))

# tipo dict (dicionario)
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
multiplicacao = calculadora['multplicacao']

print('A soma é: {}'.format(soma(10, 5)))
print('A multiplicação é: {}'.format(multiplicacao(2, 8)))