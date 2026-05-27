times = ['1_palmeiras','2_coritiba','1_corintians','3_juventude','2_fluminense','3_bahia','1_cuiaba','2_cascavel','3_ponte preta','2_parana clube', '3_volta redonda']

primeira_divisao = []
segunda_divisao = []
terceira_divisao = []

for time in times:
    timeSplit = time.split('_')
    if timeSplit[0] == '1':
        primeira_divisao.append(timeSplit[1])
    elif timeSplit[0] == '2':
        segunda_divisao.append(timeSplit[1])
    elif timeSplit[0] == '3':
        terceira_divisao.append(timeSplit[1])

print(f'Primeira Divisão: {primeira_divisao}\nSegunda Divisão: {segunda_divisao}\nTerceira Divisão: {terceira_divisao}')