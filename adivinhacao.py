import random


def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhacao!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3
    pontos = 100

    print("Qual o nível de dificuldade?")
    print("(1)Fácil  (2)Médio  (3)Difícil")
    # print(numero_secreto)
    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas+1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi MAIOR do que o número secreto")
            elif(menor):
                print("Você errou! O seu chute foi MENOR do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)  # numero absoluto
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogar()
