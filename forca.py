def jogar():

    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************")
    enforcou = False

    acertou = False

    palavra_secreta = "Banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    letras_faltando = 0
    print("A palavra é:")
    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:

            if (chute.lower() == letra.lower()):
                letras_acertadas[index] = letra
                letras_faltando = str(letras_acertadas.count('_'))
            index = index + 1

        print(letras_acertadas)
        print(letras_faltando)
    print("Fim do jogo!")


if (__name__ == "__main__"):
    jogar()
