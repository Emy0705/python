while True:
    var = str(input("Você gosta de Python? "))
    var = var.upper()
    if var == "SIM":
        print("Resposta correta! ")
        break
    else:
        print("Esta não é a resposta correta, tente novamente!")