class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self, anos):
        self.idade += anos
        if (self.idade < 21):
            self.crescer(0.5)
    def engordar(self, peso):
        self.peso += peso
    def emagrecer(self, peso):
        self.peso -= peso
        def crescer(self, altura):
            self.altura += altura
            
a = Pessoa("Amanda", 18, 75, 180)
print(vars(a))
a.engordar(5)
print(vars(a))
a.emagrecer(10)
print(vars(a))
a.crescer(3)
print(vars(a))
a.envelhecer(1)
print(vars(a))