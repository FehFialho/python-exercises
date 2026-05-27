import random

def divisao():
    print('-' * 45)

def gerar_matriz(col_num, row_num): 
    for row in range(row_num):
        matriz.append([])
        for col in range(col_num): 
            matriz[row].append(random.randint(0,9))
            if matriz[row][col] % 2 == 0:
                global soma
                soma += matriz[row][col]
                pares.append(matriz[row][col])

soma = 0
pares = []
matriz = []
divisao()
col_num = int(input('Insira o número de Colunas: '))
row_num = int(input('Insira o número de Linhas: '))
gerar_matriz(col_num, row_num)

divisao()
print('Matriz Gerada:')
for linha in matriz:
    linha_formatada = ''.join(str(linha))
    print(linha_formatada)
    
divisao()
print(f'Soma dos númeors pares: {soma}')
print(f'Números pares: {pares}')
divisao()