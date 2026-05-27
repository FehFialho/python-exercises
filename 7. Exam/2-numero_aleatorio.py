import random
random_num = random.randint(1, 1000)
tries = 1
#print(f'Número aleatório para facilitar correção: {random_num}')

while True: 
    guess = int(input('Tente acertar o número sorteado: '))    
    print('-' * 40)

    if guess == random_num:
        print((f'Você acertou! O número era {random_num}!\n').center(40))
        print((f'Número de tentativas: {tries}').center(40))
        print('-' * 40)
        break
    else:
        if guess > random_num:
            print('O número é menor! ')
        else:
            print('O número é maior! ')

        if guess > (random_num - 4) and guess < (random_num + 4):
            print('Quase lá!')
            tries += 1
        else:
            print('Está longe!')
            tries += 1
    print('-' * 40)