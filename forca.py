import random


def imprime_abertura():
    print('********************************')
    print("Bem vindo ao jogo de Forca")
    print('********************************')


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r", encoding="UTF-8")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    numero = random.randrange(0, len(palavras))
    arquivo.close()
    print(palavras)
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicia_letras(palavra):
    return ["_" for letra in palavra]
    # for letra in palavra_secreta:
    # letras_acertadas.append()


def chuta():
    chute = input("Qual letra?").upper().strip()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


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


def ganhador():
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


def perdedor(palavra_secreta):
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


def jogar():
    imprime_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicia_letras(palavra_secreta)
    print(letras_acertadas)

    erros = 0
    enforcou = False
    acertou = False
    # Enquanto (True)
    while (not enforcou and not acertou):
        chute = chuta()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
        if (erros == 7):
            enforcou = True
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if (acertou):
        ganhador()
    else:
        perdedor(palavra_secreta)
    print("Fim do jogo.")


if (__name__ == "__main__"):
    jogar()
