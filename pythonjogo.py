import random

num = random.randint(1, 1000)
chance = 10

while chance != 0:
    tentativa = int(input("Tente advinhar um número: "))
    if tentativa == num: 
        break
    elif tentativa > num:
        print("O número é menor")
    elif tentativa < num:
        print("O número é maior")
    chance -= 1

if chance == 0:
    print("Você não tem mais chances, o numero era", num)
else:
    print("Parabéns esse é o número! Você levou",chance, "tentativas para acertar")
    