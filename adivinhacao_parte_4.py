import random

seu_nome = input("Por favor, digite seu nome: ")

print("Bem vindo,", seu_nome, "ao jogo de adivinhação")
print("-------------------------------------------", "\n")

numero_da_sorte = round(random.randrange(1, 101))
total_tentativas = 3

for tentativas in range(1, total_tentativas + 1):
    numero_escolhido = input("Escolha um número: ")
    print("Você digitou", numero_escolhido)
    print("Você está na tentativa {} de {}".format(tentativas, total_tentativas))

    if(int(numero_escolhido) < 1 or int(numero_escolhido) > 100):
        print("Digite um número de 1 a 100")
        continue

    acertou = int(numero_escolhido) == numero_da_sorte
    maior = int(numero_escolhido) > numero_da_sorte
    menor = int(numero_escolhido) < numero_da_sorte

    if(acertou):
        print("Você acertou", "\n")
        break
    elif(maior):
        print("Você errou! o seu chute foi maior do que o número secreto", "\n")
    elif(menor):
        print("Você errou! o seu chute foi menor do que o número secreto", "\n")

    tentativas += 1

print("fim do jogo")