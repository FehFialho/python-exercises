#Aula 5 (19/02/2025)
import random

class InvalidChoice(Exception):
    pass

loop = 1
score = 0  

def perde():
    print('            Você Perdeu!')

def ganha():
    global score  
    print('            Você Venceu!')
    score += 1 

while loop == 1:
    try:
        player = int(input('\n===============JOKEMPO==============\n'
                           '          Escolha sua Jogada\n'
                           ' 1 - Pedra | 2 - Papel | 3 - Tesoura\n'
                           '====================================\n'))
        
        if (player > 3) or (player < 1): 
            raise InvalidChoice

        computer = random.randint(1, 3)
        print(f'       Computador escolheu: {computer}')

        if player == computer:
            print('              Empate!')

        elif computer == 1:
            if player == 2:
                ganha()
            elif player == 3:
                perde()
        elif computer == 2:
            if player == 3:
                ganha()
            elif player == 1:
                perde()
        elif computer == 3:
            if player == 1:
                ganha()
            elif player == 2:
                perde()

    except InvalidChoice:
        print('======================================\n   Escolha inválida, tente novamente!')
    except ValueError:
        print('======================================\n   Digite um número!')

    loop = int(input('\n--------------------------------------\n'
                     '     Deseja continuar jogando?\n'
                     '          1 - Sim | 2 - Não\n'
                     '--------------------------------------'))

print(f'======================================\n         VOCÊ VENCEU {score} VEZES!\n======================================')