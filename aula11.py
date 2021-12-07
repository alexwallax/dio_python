
lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]

except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))


# o Exception trata todos os erros
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))

else:
    print('\nExecuta quando não ocorre exceção\n')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()