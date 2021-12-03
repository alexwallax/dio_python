class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    
    def aumanta_canal(self):
        if self.ligada:
            self.canal += 1
    
    def diminue_canal(self):
        if self.ligada:
            self.canal -= 1

# instanciar
televisao = Televisao()
print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.power() # ligando a tv
print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.power() # desligando a tv
print('Televisão está ligada: {}'.format(televisao.ligada))
print('Canal: {}'.format(televisao.canal))
televisao.power() # ligando a tv
print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.aumanta_canal() # aumentando o canal
televisao.aumanta_canal() # aumentando o canal
print('Canal: {}'.format(televisao.canal))
televisao.diminue_canal() # diminuindo o canal
print('Canal: {}'.format(televisao.canal))
