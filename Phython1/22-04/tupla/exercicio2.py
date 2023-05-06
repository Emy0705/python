p1 = [2.5,6,7,7.5,8,9,10]
p2 = [3,6.5,7.5,8.5,9,10]

media_p1 = sum(p1) / len(p1)
media_P2 = sum(p2) / len(p2)

if media_p1 > media_P2:
    print("A turma teve melhor média na prova 1: %.2f" % media_p1)
elif media_P2 > media_p1:
    print("A turma teve melhor média na prova 2: %.2f" % media_P2)
else:
    print("A turma teve a mesma média nas duas provas: %.2f" % media_p1)

