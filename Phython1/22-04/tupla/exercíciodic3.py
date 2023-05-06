filmes = {}

filmes['A Escolha Perfeita'] = {'vilão': 'Beca Mitchell', 'ano': 2012}
filmes['A Escolha Perfeita 2'] = {'vilão': 'Das Sound Machine', 'ano': 2015}
filmes['A Escolha Perfeita 3'] = {'vilão': 'Evermoist', 'ano': 2017}
while True:
    filmeNovo = input("Digite o nome do filme: ")
    if filmeNovo == "0":
        break
    vilaoNovo = input("Digite o nome do vilão: ")
    anoNovo = input("Digite o ano do filme: ")
    filmes[filmeNovo] = {"vilão": vilaoNovo, "ano": anoNovo}
print(filmes)
pesquisa = input("Digite o Filme Procurado")
if pesquisa in filmes:
    print(filmes[pesquisa])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    /;/;