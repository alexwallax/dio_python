# Verificar a média
a = int(input('Primeira nota: '))
if a > 10:
    a = int(input('Você digitou errado. Primeira nota: '))
b = int(input('Segunda nota: '))
if b > 10:
    b = int(input('Você digitou errado. Segunda nota: '))
c = int(input('Terceira nota: '))
if c > 10:
    c = int(input('Você digitou errado. Terceira nota: '))
d = int(input('Quarta nota: '))
if d > 10:
    d = int(input('Você digitou errado. Quarta nota: '))

media = (a + b + c + d) / 4
print('Média: {}'.format(media))

#------------------------------------------
# Verificar a média outra forma
#a = int(input('Primeira nota: '))
#b = int(input('Segunda nota: '))
#c = int(input('Terceira nota: '))
#d = int(input('Quarta nota: '))

#media = (a + b + c + d) / 4
#if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#    print('Média: {}'.format(media))
#else:
#    print('Foi informado alguma nota invalida')

#------------------------------------------
# Verifica se foi digitado um número par alguma vez
#a = int(input('Digite um valor: '))
#b = int(input('Digite outro valor: '))
#resto_a = a % 2
#resto_b = b % 2
#if resto_a == 0 or resto_b == 0:
#    print('Foi digitado número par')
#else:
#    print('Não foi digitado número par')

#------------------------------------------
# Verifica se o número é par
#a = int(input('Digite um valor: '))
#resto = a % 2
#if resto == 0:
#    print('Número é par')
#else:
#    print('Número é impar')

#------------------------------------------
# Verificar qual o maior número

#a = int(input('Primeiro valor: '))
#b = int(input('Segundo valor: '))
#c = int(input('Treceiro valor: '))

#if a > b and a > c:
#    print('O maior número é {}'.format(a))
#elif b > a and b > c:
#    print('O maior número é {}'.format(b))
#else:
#    print('O maior número é {}'.format(c))
#print('Final do programa')
#------------------------------------------
