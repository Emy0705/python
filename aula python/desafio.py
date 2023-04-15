# Escreva um programa que solicite vários números ao usuário,
# sendo um de cada vez, possibilitando encerrar a entrada de
# dados informando zero. Armazene os números em uma lista,
# depois percorra esta lista alimentando outras duas listas, uma
# com números pares e outra com números ímpares. Ordene e
# imprima os números em ordem crescente e some os valores e

lista = []
listaPar = []
listaImpar = []
somaPar = 0
somaImpar = 0
while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    lista.append(num)
# Percorrendo a lista

for x in lista:
    if x%2 == 0:
        listaPar.append(x)
        somaPar +=x
    else:
        listaImpar.append(x)
        somaImpar +=x
# Imprimindo os resultados

listaPar.sort () #coloca em ordem crescente
listaImpar.sort () #coloca em ordem crescente
print(f"Os numeros pares são:{listaPar} e sua somatória é {somaPar}")
print(f"Os numeros ímpares são:{listaImpar} e sua somatória é {somaImpar}")