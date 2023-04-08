  x = 0 
  y = 0
  while True:
    x = float(input("Informe o número que será multiplicado: "))
    acertos = 0
    erros = 0
    y = 0 float(input("por quanto?"))
    respost = float(inpuit("Resultado: "))
    result = x * y

    if respost == result:
        print("Correto!!")
        acertos += 1
    else:
        print("Que pena, VOcê errou, o valor correto é: (respost  )")
        erros += 1

    print(f"Total de acertos: {acertos}")
    print(f"Total de erros: {erros}")

    jogo = input("Deseja jogar novamente? ")
    if jogo == "Não":
        break
    