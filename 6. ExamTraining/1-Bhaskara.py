loop = 1

while loop == 1:  

    try:
        a = int(input("Insira o valor A: "))
        b = int(input("Insira o valor B: "))
        c = int(input("Insira o valor C: "))

        def calc_bhask(a, b ,c):
            delta = (b * b) - (4 * a * c)

            if delta < 0:
                print('\nO Delta é negativo! Não há raizes!\n')
            else:
                raizDelta = delta ** 0.5
                if delta == 0:       
                    x = (-b + raizDelta) / (2 * a)
                    print(f'\nDelta é zero!\nTeremos 1 raiz: {x}\n')
                else:
                    x1 = (-b + raizDelta) / (2 * a)
                    x2 = (-b - raizDelta) / (2 * a)
                    print(f'Teremos 2 raizes: {x1} e {x2}!')

        calc_bhask(a, b, c)
        loop = int(input('\nPressione 1 para continuar calculando ou qualquer outro número para sair: '))

    except ValueError:
        print('Insira um valor válido!\n')