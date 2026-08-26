import random
import math

numero = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1

    if palpite == numero:
        print("Parabéns! Você acertou.")
        break
    elif palpite < numero:
        print("O número é maior.")
    else:
        print("O número é menor.")

print("Tentativas:", tentativas)
print("Raiz quadrada do número:", math.sqrt(numero))