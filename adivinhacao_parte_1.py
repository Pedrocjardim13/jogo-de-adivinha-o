seu_nome = input("Por favor, digite seu nome: ")

print("Bem vindo,", seu_nome, "ao jogo de adivinhação")
print("-------------------------------------------", "\n")

numero_da_sorte = 42
numero_escolhido = input("Escolha um número: ")

if (int(numero_escolhido) == numero_da_sorte):
    print("Parabéns, você acertou", "\n")
elif (int(numero_escolhido) < numero_da_sorte):
    print("Você errou, o número escolhido é menor", "\n")
else:
    print("Você errou, número escolhido é maior", "\n")

print("Fim de jogo")