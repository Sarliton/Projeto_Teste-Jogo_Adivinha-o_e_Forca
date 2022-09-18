def jogar():
    import random
    print("********************************")
    print("Bem vindo ao jovo de Adivinhação")
    print("********************************")
    numero_random = random.randrange(1, 101)

    sec_num = round(numero_random)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000
    print("Qual nivel de dificuldade?")
    print(" 1.Facil \n 2.Medio \n 3.Dificil \n")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")

        print("Você digitou ", chute_str)

        chute = int(chute_str)
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = sec_num == chute
        maior = chute > sec_num
        menor = chute < sec_num

        if (acertou):
            print(f"Você acertou e fez {pontos} pontos")

            break

        else:
            pontos_perdidos = abs(sec_num - chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("Seu chute foi maior que o numero correto")
                if(rodada == total_de_tentativas):
                    print(f"O número secreto era {sec_num} e você fez {pontos} pontos")
            elif(menor):
                print("Seu chute foi menor que o numero secreto.")
                if (rodada == total_de_tentativas):
                    print(f"O número secreto era {sec_num} e você fez {pontos} pontos")


    print("Fim do jogo")
    print(f'A resposta erá {sec_num}')

if(__name__ == "__main__"):
    jogar()
