while True:
    try:

        print('-' * 30)
        data_digit = input('Insira uma data (dd/mm/aaaa): ')
        data_array = data_digit.split('/')

        meses = {
            '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril', '05': 'Maio', '06': 'Junho', 
            '07': 'Julho', '08': 'Agosto', '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'
        }

        print(f'A data final é {data_array[0]} de {meses[data_array[1]]} de {data_array[2]}')
        print('-' * 30)
        break
    except KeyError:
        print('Insira o mês corretamente!')
        print('-' * 30, '\n')
        continue
    except IndexError: 
        print('Insira uma data válida!')
        print('-' * 30, '\n')
        continue