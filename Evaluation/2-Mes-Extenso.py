loop = 1

while loop == 1:                                
    try:   

        data_extenso = input('Insira a data em extenso: ').upper()

        data_array = data_extenso.split(' DE ')

        month = data_array[1]

        get_month = {
            "JANEIRO": "01",
            "FEVEREIRO": "02",
            "MARÇO": "03",
            "ABRIL": "04",
            "MAIO": "05",
            "JUNHO": "06",
            "JULHO": "07",
            "AGOSTO": "08",
            "SETEMBRO": "09",
            "OUTUBRO": "10",
            "NOVEMBRO": "11",
            "DEZEMBRO": "12"
        }

        print(f'A data é: {data_array[0]}/{get_month[month]}/{data_array[2]}')
    except ValueError:
        print('\nInsira uma data válida!')
    except IndexError:
        print('\nInsira uma data válida!')
    except KeyError:
        print('\nInsira uma data válida!')