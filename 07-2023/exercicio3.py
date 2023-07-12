class Quadrado():
    def __init__(self, lado):
        self.setLado(lado)
    def setLado(self, lado):
        self.lado = lado
    def getLado(self):
        return self.lado
    def area(self):
        return self.lado * self.lado
        
q = Quadrado(5)
print(q.area())