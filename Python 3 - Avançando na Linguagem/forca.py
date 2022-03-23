import random

#Função para realizar a abertura do jogo
def abertura_jogo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

#Função que carrega e retorna a palavra secreta do arquivo de palavras
def carrega_palavra_secreta():
    arquivo = open("palavras.txt","r") #Abre arquivo de palavras
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip().upper())

    arquivo.close()

    palavra_secreta = palavras[random.randrange(0,len(palavras))]

    return palavra_secreta

#Função para criar palavra com letras vazias a serem acertadas
def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

#Funcao para solicitar o chute do usuário
def chute_usuario():
    chute = str(input("Qual letra? "))
    chute = chute.strip().upper()
    return chute

#Funcao que marca as letras acertadas na palavra
def marca_letras_acertadas(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra

        index += 1

    print(letras_acertadas)

def enforcou(erros):
    return erros == 7

def acertou(letras_acertadas):
    return "_" not in letras_acertadas

def resultado(enforcou,acertou,palavra_secreta):
    if enforcou and not acertou:
        imprime_perdedor(palavra_secreta)

    elif acertou and not enforcou:
        imprime_ganhador()


def imprime_perdedor(palavra_secreta):
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

def imprime_ganhador():
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

def imprime_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
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

    abertura_jogo()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcado = False
    acertado = False
    erros = 0

    while not enforcado and not acertado:
        chute = chute_usuario()

        if chute in palavra_secreta:
            marca_letras_acertadas(chute,letras_acertadas,palavra_secreta)

        else:
            erros += 1
            imprime_forca(erros)

        enforcado = enforcou(erros)
        acertado =  acertou(letras_acertadas)

    resultado(enforcado,acertado,palavra_secreta)

if __name__ == "__main__":
    jogar()
