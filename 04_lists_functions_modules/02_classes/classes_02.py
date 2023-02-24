# FEITO PELO PROFESSOR
# strings sao objetos do tipo 'str'
# nome = "Erick"
# print(nome)
# print(type(nome))
#
# print(nome.upper())

class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def somar(self, outro_ponto):
        p = Ponto(self.x + outro_ponto.x, self.y + outro_ponto.y)
        return p



p1 = Ponto(1, 2)
p2 = Ponto(2, 3)

p3 = p1.somar(p2)
print(p3.x, p3.y)
