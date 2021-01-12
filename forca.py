from random import randrange


def jogar():

    print("**********Seja Bem-Vindo a Forca**********")

    # Abre o arquivo
    arquivo = open("palavras.txt", "r")
    palavras = []

    # Escolhe uma palavra secreta dentro do arquivo, e fecha o mesmo
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    # Escolhe uma palavra do arquivo palavras.txt
    numero = randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    # print(palavra_secreta)

    # Insere caracteres de acordo com a quantidade de letras da palavra escolhida através de um list comprehension
    palavra_correta = ["_" for letra in palavra_secreta]
    print(palavra_correta)

    enforcou = False
    venceu = False
    erros = 0

    # início do jogo
    while not enforcou and not venceu:
        chute = str(input("Digite uma letra: ")).strip().upper()

        # Verifica se o chute do usuário está correto ou não
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    palavra_correta[index] = letra
                index += 1
        else:
            erros += 1
        print(palavra_correta)

        # Variáveis para definir se o usuário ganhou ou perdeu
        venceu = "_" not in palavra_correta
        enforcou = erros == 7

    # Verifica se o usuário venceu ou perdeu o jogo
    if venceu:
        print("Parabéns, você venceu!")
    else:
        print("Você perdeu!")


if __name__ == '__main__':
    jogar()
