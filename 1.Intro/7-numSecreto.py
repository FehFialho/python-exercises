#Aula 2 (14/02/2025)

num = 7
loop = 1

while loop == 1:
    escolha = int(input('Chute um valor: '))
    if escolha == num:
        print('Parabéns! Você acertou o número!')
        loop = 0
    else:
        if escolha > num:
            print('O número é menor!')
        else:
            print('O número é maior!')