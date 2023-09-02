def executar():
    dias_iteracoes = [
        "1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 | 19 | 21 | 23 | 25 | 27 | 29 | 31",
        "2 | 3 | 6 | 7 | 10 | 11 | 14 | 15 | 18 | 19 | 22 | 23 | 26 | 27 | 30 | 31",
        "4 | 5 | 6 | 7 | 12 | 13 | 14 | 15 | 20 | 21 | 22 | 23 | 28 | 29 | 30 | 31",
        "8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31",
        "16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31"
    ]
    meses_iteracoes = [
        "1 | 3 | 5 | 7 | 9 | 11",
        "2 | 3 | 6 | 7 | 10 | 11",
        "4 | 5 | 6 | 7 | 12",
        "8 | 9 | 10 | 11 | 12"
    ]
    dia_encontrado = 0
    mes_encontrado = 0
    i = 0

    print("Adivinhando o dia...")
    while (i < 5):
        print("Seu dia de nascimento está entre os números abaixo?")
        print(dias_iteracoes[i])
        resposta = input("Pressione 1 para Sim e 2 para Não: ")

        if (resposta == "1"):
            match i:
                case 0:
                    dia_encontrado += 1
                case 1:
                    dia_encontrado += 2
                case 2:
                    dia_encontrado += 4
                case 3:
                    dia_encontrado += 8
                case 4:
                    dia_encontrado += 16
                case _:
                    print("Ocorreu algum erro")
            i += 1
        elif (resposta != "2"):
            print("Resposta inválida!")
        else:
            i += 1

    i = 0
    print("Adivinhando o mês...")
    while (i < 4):
        print("Seu mês de nascimento está entre os números abaixo?")
        print(meses_iteracoes[i])
        resposta = input("Pressione 1 para Sim e 2 para Não: ")

        if (resposta == "1"):
            match i:
                case 0:
                    mes_encontrado += 1
                case 1:
                    mes_encontrado += 2
                case 2:
                    mes_encontrado += 4
                case 3:
                    mes_encontrado += 8
                case _:
                    print("Ocorreu algum erro")
            i += 1
        elif (resposta != "2"):
            print("Resposta inválida!")
        else:
            i += 1

    print("Sua data de nascimento é {:02d}/{:02d}".format(dia_encontrado, mes_encontrado))

if (__name__ == "__main__"):
    executar()