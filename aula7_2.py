#--------------------------------
# class

class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

if __name__ == '__main__':

    # instanciar uma class
    calculadora = Calculadora()
    print(calculadora.soma(2, 3))
    print(calculadora.subtracao(2, 4))
    print(calculadora.multiplicacao(5, 6))
    print(calculadora.divisao(8, 2))


