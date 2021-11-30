
# Imprimir os 100 primeiros números
#for x in range(101):
#    print(x)

#-----------------------------------
# Pedir um número e informar se é um número primo 
#a = int(input('Digite um número: '))

#div = 0
#for x in range(1, a + 1):
#    resto = a % x
#    print(x, resto)
#    if resto == 0:
#        div += 1

#if div == 2:
#    print('Número {} é primo '.format(a))
#else:
#    print('Número {} não é primo '.format(a))
#-----------------------------------

# Números primos de 0 a 100
#for num in range(101):
#    div = 0
#    for x in range(1, num + 1):
#        resto = num % x
#        if resto == 0:
#            div += 1
#    if div == 2:
#        print(num)
   
#-----------------------------------
# Números primos até onde o usuário escolher
#a = int(input('Digite um valor: '))
#for num in range(a + 1):
#    div = 0
#    for x in range(1, num + 1):
#        resto = num % x
#        if resto == 0:
#            div += 1
#    if div == 2:
#        print(num)

#-----------------------------------
# Laço de repetição ate um número especifico (10)
#a = 0
#while a <= 10:
#    print(a)
#    a += 1 

#-----------------------------------
# Digitar uma nota menor ou igual a 10
#nota = int(input('Digite sua nota '))
#while nota > 10:
#    nota = int(input('Nota inválida. Digite sua nota '))
#print('Sua nota foi {}'.format(nota))

#-----------------------------------
# Verificar a média
a = int(input('Primeira nota: '))
while a > 10:
    a = int(input('Você digitou errado. Primeira nota: '))
b = int(input('Segunda nota: '))
while b > 10:
    b = int(input('Você digitou errado. Segunda nota: '))
c = int(input('Terceira nota: '))
while c > 10:
    c = int(input('Você digitou errado. Terceira nota: '))
d = int(input('Quarta nota: '))
while d > 10:
    d = int(input('Você digitou errado. Quarta nota: '))

media = (a + b + c + d) / 4
print('Média: {}'.format(media))