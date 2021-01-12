from time import sleep
import forca
import advinhacao


def game():
    print("Seja bem vindo!")
    sleep(0.8)
    print("Escolha uma das opções abaixo:")
    print("[ 1 ] FORCA")
    print("[ 2 ] ADVINHAÇÃO")

    escolha_usuario = int(input("Digite a sua escolha: "))

    if escolha_usuario == 1:
        print("Jogando Forca...")
        forca.jogar()
    elif escolha_usuario == 2:
        print("Jogando Advinhação...")
        advinhacao.jogar()
    else:
        print("Escolha Inválida!")


if __name__ == '__main__':
    game()
