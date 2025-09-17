#Aula 5 (19/02/2025)
loop = 1

while loop == 1: 
    print('=================\n   CALCULADORA \n=================\n 1- Soma \n 2- Subtração \n 3- Multiplicação \n 4- Divisão \n 5- Sair\n ================\n')
    
    try:
        num1 = int(input('Escolha o primeiro número: '))
        num2 = int(input('Escolha o segundo número: '))
        operacao = int(input('Escolha a operação desejada: '))

        def consultaZero(divisor):
            if divisor == 0:
                raise ZeroDivisionError
            return divisor

        def operacoes(operacao, num1, num2):
            if operacao == 1:
                print(f' {num1} + {num2} = {num1 + num2}')
            elif operacao == 2:
                print(f' {num1} - {num2} = {num1 - num2}')
            elif operacao == 3:
                print(f' {num1} * {num2} = {num1 * num2}')
            elif operacao == 4:
                try:
                    consultaZero(num2)
                    print(f' {num1} / {num2} = {num1 / num2}')
                except ZeroDivisionError:
                    print('Não é possível dividir por zero. Faça a operação novamente!')
            elif operacao == 5:
                print('Saindo da calculadora...')
                global loop
                loop = 0
            else:
                print('Operação inválida!')

        operacoes(operacao, num1, num2)

    except ValueError:
        print('Inválido! Digite apenas números.')