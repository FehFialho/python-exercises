#Aula 5 (19/02/2025)
class InvalidNumber(Exception):
    pass

loop = 1

while loop == 1:
    try:
        num = int(input('Insira um número maior do que 0: '))
        
        if num < 1:
            raise InvalidNumber

        def turnArray(num):
            soma = 0
            array = [int(i) for i in str(num)]
            print(array)
            for i in array:
                print(i)
                soma += i  # Agora soma o valor de i diretamente, sem usar como índice
            return soma

    except InvalidNumber:
        print('Insira um valor maior do que 0!')

    print(f'A soma dos algarismos de {num} é {turnArray(num)}!')
    loop = int(input("Pressione 1 para continuar ou outro número para sair!"))