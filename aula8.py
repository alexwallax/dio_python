
# acessar aula7_3
from aula7_3 import Televisao

# acessando aula8_2
from aula8_2 import contador_letras, teste


if __name__ == '__main__':
    # instanciar a class Televisao da aula7_3
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    #acessando aula8_2
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavra de lista: {}'.format(total_letras))
    print(teste())



