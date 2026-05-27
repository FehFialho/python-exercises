#Aula 2 (14/02/2025)

while True: 
    print('=================\n   CALCULADORA \n=================\n 1- Soma \n 2- Subtração \n 3- Multiplicação \n 4- Divisão\n ===============\n')
    num1 = int(input('Escolha o primeiro número: '))
    num2 = int(input('Escolha o segundo número: '))
    operacao = int(input('Escolha a operação desejada: '))
    resultado = 0

    if operacao == 1:
        print(f' {num1} + {num2} = {num1 + num2}')
        break
    elif operacao == 2:
        resultado = num1 - num2
        break
    elif operacao == 3:
        resultado == num1 * num2
        break
    elif operacao == 4:
        resultado = num1 / num2
        break