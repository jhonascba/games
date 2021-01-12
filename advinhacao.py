from random import randint


def jogar():
    print("**********Bem-Vindo ao Desafio da Advinhação**********")

    numero_secreto = randint(1, 100)
    pontos = 1000

    print("""Escolha um dos níveis abaixo:
    [ 1 ] Fácil
    [ 2 ] Médio
    [ 3 ] Difícil""")
    nivel = int(input("Nível Escolhido: "))

    chances = 0

    if nivel == 1:
        chances = 20
    elif nivel == 2:
        chances = 10
    elif nivel == 3:
        chances = 5
    else:
        print("Valor incorreto!")

    for tentativas in range(1, chances + 1):
        print(f"Tentativa {tentativas} de {chances}")
        chute = int(input("Escolha um número entre 1 e 100: "))
        print(f"Você digitou {chute}")

        if chute < 1 or chute > 100:
            print("Digite um valor válido!")
            tentativas += 1
            continue

        acertou = chute == numero_secreto

        if acertou:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            print(f"Você acertou o número secreto e fez {pontos} pontos!")
            break
        else:
            if chute > numero_secreto:
                print("Seu chute foi maior que o número secreto!")
                tentativas += 1
            elif chute < numero_secreto:
                print("Seu chute foi menor que o número secreto!")
                tentativas += 1

    print("Fim do jogo!")


if __name__ == '__main__':
    jogar()
