#Aula 3 (17/02/2025)
while True:
    array = []
    num = int(input('Digite um número: '))

    for i in range(1, num+1):
        if num % i == 0:
            array.append(i)
    
    print(array)

    if len(array) == 2:
        print(f'O número {num} é primo!')
    else:
        print(f'O número {num} não é primo!')