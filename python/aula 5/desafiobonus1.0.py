while True:
    num = int(input("Digite o número para treinar a tabuada: "))
    acertos = 0

    for i in range(1, 11):
        resp = int(input(f"{num} x {i} = "))
        if resp == num * i:
            acertos += 1
            print("CORRETO")
        else:
            print(f"QUE PENA, VOCÊ ERROU, O VALOR CORRETO É {num * i}")

    print(f"Total de acertos: {acertos}")
    print(f"Total de erros: {10 - acertos}")

    novo_jogo = input("Deseja jogar novamente? ")
    if novo_jogo == "não":
        break