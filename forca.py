import random


def imprime_bem_vindo():
    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************")


def car_palavra_secreta():
    palavras = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            palavras.append(linha)
    num = random.randrange(0, len(palavras))
    palavra_secreta = palavras[num].lower()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def chuta():
    chute = input("Qual letra? ")
    chute = chute.strip().lower()
    return chute


def marca_chute_certo(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:

        if (chute.lower() == letra.lower()):
            letras_acertadas[index] = letra
            letras_faltando = str(letras_acertadas.count('_'))
        index += 1


def imprime_correto():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def que_pena_voce_errou(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
    imprime_bem_vindo()

    palavra_secreta = car_palavra_secreta()
    enforcou = False
    acertou = False
    erros = 0
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    letras_faltando = len(palavra_secreta)
    tent_falt = 7
    print("A palavra é:")
    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = chuta()

        if (chute in palavra_secreta):
            marca_chute_certo(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            tent_falt -= 1
            desenha_forca(erros)
            print(f"Você possui {tent_falt} tentativas")
            print("Letra incorreta, tente novamente")

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)
        print(f"Faltam {letras_faltando} letras")

    if (acertou):
        imprime_correto()
    else:
        que_pena_voce_errou(palavra_secreta)


if (__name__ == "__main__"):
    jogar()
