
top = [' ',' ','1',' ',' ',' ','2',' ',' ',' ','3',' ',' ',' ','4',' ',' ',' ','5',' ',' ',' ','6',' ',' ',' ','7',' ',' ']
li1 = ['|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|']
li2 = ['|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|']
li3 = ['|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|']
li4 = ['|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|']
li5 = ['|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|']
li6 = ['|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|']

board = [li1,li2,li3,li4,li5,li6]

lines = len(board)
cols = len(board[0])
player = 0
loop = 1

print(f'======Bem Vindo ao LIG-4======')

def printBoard(): #Imprime o tabuleiro.
    print(f'{''.join(top)}\n{''.join(li1)}\n{''.join(li2)}\n{''.join(li3)}\n{''.join(li4)}\n{''.join(li5)}\n{''.join(li6)}')

def getList(position): #Caso o index desejado esteja ocupado, muda a linha.
    if li6[position] == ' ':
        list = li6
    elif li6[position] != ' ':
        if li5[position] == ' ':
            list = li5
        elif li5[position] != ' ':
            if li4[position] == ' ':
                list = li4
            elif li4[position] != ' ':
                if li3[position] == ' ':
                    list = li3
                elif li3[position] != ' ':
                    if li2[position] == ' ':
                        list = li2
                    elif li2[position] != ' ':
                        if li1[position] == ' ': 
                            list = li1
                        elif li1[position] != ' ':
                            print('Coluna Cheia!')
    return list

def catchList(num): #Passa a lista de acordo com o número.
    if num == 1:
        return li1
    elif num == 2:
        return li2
    elif num == 3:
        return li3
    elif num == 4:
        return li4
    elif num == 5:
        return li5
    elif num == 6:
        return li6


def symbol(player): #Define qual símbolo será desenhado de acordo com o jogador.
    if player == 1:
        symbol = 'x'
    else:
        symbol = 'o'
    return symbol

def getIndex(position): #Função para pegar o index certo de acordo com coluna desejada.
    
    if position == 1: # Preenchiveis: 2 6 10 14 18 22 26
        i = 2
    elif position == 2:
        i = 6
    elif position == 3:
        i = 10
    elif position == 4:
        i = 14
    elif position == 5:
        i = 18
    elif position == 6:
        i = 22
    elif position == 7:
        i = 26
    else:
        print('Inválido!')
    return i


def verifyLine(symbol):
    for line in range(lines):
        for col in range(1,4):
            if (board[line][getIndex(col)] == symbol) and (board[line][getIndex(col+1)] == symbol) and (board[line][getIndex(col+2)] == symbol) and (board[line][getIndex(col+3)] == symbol):
                print(f'Vitória por {board[line][getIndex(col)]}')
                win(symbol)

def verifyColumn(symbol):
    for line in range(1,3):
        for col in range(1,7):
            if (board[line][getIndex(col)] == symbol) and (board[line+1][getIndex(col)] == symbol) and (board[line+2][getIndex(col)] == symbol) and (board[line+3][getIndex(col)] == symbol):
                print(f'Vitória por {board[line][getIndex(col)]}')
                win(symbol)

def verifyDiagonal1(symbol):
    for line in range(lines):
        for col in range(1,7):
            if (board[line][getIndex(col)] == symbol) and (board[line+1][getIndex(col+1)] == symbol) and (board[line+2][getIndex(col+2)] == symbol) and (board[line+3][getIndex(col+3)] == symbol):
                print(f'Vitória por {board[line][getIndex(col)]}')
                win(symbol)

def verifyDiagonal2(symbol):
    for line in range(lines):
        for col in range(1,7):
            if (board[line][getIndex(col)] == symbol) and (board[line+1][getIndex(col-1)] == symbol) and (board[line+2][getIndex(col-2)] == symbol) and (board[line+3][getIndex(col-3)] == symbol):
                print(f'Vitória por {board[line][getIndex(col)]}')
                win(symbol)
            
def verifyAll(symbol): #Chama todas as funções de verificação.
    verifyLine(symbol)
    verifyColumn(symbol)
    verifyDiagonal1(symbol)
    verifyDiagonal2(symbol)

def win(symbol):
    if symbol == 'x':
        print('Jogador 1 venceu!')
        return True
    elif symbol == 'o':
        print('Jogador 2 venceu!')
        return False

def redPlay(): #Jogador Vermelho
    player = 1
    print('----------Jogador 1----------')
    printBoard()
    print('-----------------------------')
    position = int(input('Jogada:'))
    list = getList(getIndex(position))
    list[getIndex(position)] = f'{symbol(player)}'

def bluePlay(): #Jogador Azul
    player = 2
    print('----------Jogador 2----------')
    printBoard()
    print('-----------------------------')
    position = int(input('Jogada:'))
    list = getList(getIndex(position))
    list[getIndex(position)] = f'{symbol(player)}'

while True:
    redPlay()
    verifyAll('x')
    bluePlay()
    verifyAll('o')