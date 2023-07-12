class Conta():
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
    def setNome(self, nome):
        self.nome = nome
    def deposito(self, valor):
        self.saldo += valor
    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            
j = Conta(123, "José", 100.0)
print(vars(j))
j.setNome("Pedro")
j.deposito(50)
print(vars(j))
j.saque(110)
print(vars(j))