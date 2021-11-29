a = int(input('Digite um numero ')) #receber valor do usuário
b = int(input('Digite um numero ')) 

#a = 5
#b = 10

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b


resultado = ('Soma: {soma} \nSubtracao: {subtracao}' 
'\nMultiplicacao: {multiplicacao}'
'\nDivisao:  {divisao}'
'\nResto: {resto}' .format(soma=soma, 
                           subtracao=subtracao,
                           multiplicacao=multiplicacao,
                           divisao=divisao,
                           resto=resto ))

print (resultado)

#print('\n\n')
#print('\n\nsoma: ' + soma)
#print('subtracao: ' + str(sub))
#print('mult: ' + str(mult))
#print('divisao: ' + str(div))
#print('resto: ' + str(resto))

#x = '3'
#soma2 = int(x) + 7
#print(soma2)
