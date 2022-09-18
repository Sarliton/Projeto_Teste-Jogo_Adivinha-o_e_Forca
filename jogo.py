import forca
import advinhação

def escolhe_jogo():
    print("***************************")
    print("*****Escolha seu jogo!*****")
    print("***************************")

    print(" 1.Forca \n 2.Advinhação")

    jogo = int(input("Dfina seu jogo: "))

    if(jogo == 1):
        print("Jogando forca!")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Advinhação!")
        advinhação.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()