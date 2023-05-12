seu_nome = input("Por favor, digite seu nome: ")

print("Bem vindo,", seu_nome, "ao jogo de adivinhação")
print("-------------------------------------------", "\n")

numero_da_sorte = 42
total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
    numero_escolhido = input("Escolha um número: ")
    print("Você digitou", numero_escolhido)
    print("Você está na tentativa {} de {}".format(rodada, total_tentativas))

    acertou = int(numero_escolhido) == numero_da_sorte
    maior = int(numero_escolhido) > numero_da_sorte
    menor = int(numero_escolhido) < numero_da_sorte

    if(acertou):
        print("Você acertou", "\n")
    elif(maior):
        print("Você errou! o seu chute foi maior do que o número secreto", "\n")
    elif(menor):
        print("Você errou! o seu chute foi menor do que o número secreto", "\n")

    rodada += 1

print("fim do jogo")