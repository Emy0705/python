def positivo_negativo(numero):
    if numero > 0:
        return "Positivo(P)"
    else:
        return "Negativo(P)"
    
x = int(input("Digite um número: "))    
print (positivo_negativo(x))