seu_nome = input("Por favor, digite seu nome: ")

print("Bem vindo,", seu_nome, "ao jogo de adivinhação")
print("-------------------------------------------", "\n")

numero_da_sorte = 42
numero_escolhido = int(input("Escolha um número: "))

print("Você digitou", numero_escolhido)

acertou = numero_escolhido == numero_da_sorte
maior = numero_escolhido > numero_da_sorte
menor = numero_escolhido < numero_da_sorte

if(acertou):
    print("Você acertou", "\n")
else:
    if(maior):
        print("Você errou! o seu chute foi maior do que o número secreto")
    elif(menor):
        print("Você errou! o seu chute foi menor do que o número secreto")
print("fim do jogo")