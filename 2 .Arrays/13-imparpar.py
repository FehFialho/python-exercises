#Aula 3 (17/02/2025)
import random

streak = True

while streak == True:

    x = random.randint(0,10)
    print(x)
    wins = 0

    num = int(input('Insira um número: '))
    player = int(input('1 - Par | 2 - Impar '))

    if player == 1:
        computer = 2
    else:
        computer = 1

    soma = x + num

    if soma % 2 == 0:
        if player == 1:  
            print(f"{soma} é par! O jogador venceu!")
            wins += 1
        else:
            print(f"{soma} é par! O computador venceu!")
            streak = False
            print(f'Você venceu {wins} vezes!')

    elif soma % 2 == 1:
        if player == 2:  
            print(f"{soma} é ímpar! O jogador venceu!")
            wins += 1
        else:
            print(f"{soma} é par! O computador venceu!")
            streak = False
            print(f'Você venceu {wins} vezes!')