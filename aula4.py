
# Imprimir os 100 primeiros números
#for x in range(101):
#    print(x)

#-----------------------------------
# Pedir um número e informar se é um número primo 
a = int(input('Digite um número: '))

div = 0
for x in range(1, a + 1):
    resto = a % x
    print(x, resto)
    if resto == 0:
        div = div + 1

if div == 2:
    print('Número {} é primo '.format(a))
else:
    print('Número {} não é primo '.format(a))