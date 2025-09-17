print(f'======Bem Vindo ao LIG-4======')

def reset():
    global board, loop, lines, cols, player
    loop = 1
    board = [
    ['-','-','-','-','-','-','-','-'], [' ',' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' ',' '], 
    [' ',' ',' ',' ',' ',' ','',''], [' ',' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' ',' ']
    ]

    lines = len(board)
    cols = len(board[0])
    player = 0

def printBoard(): #Imprime o tabuleiro.

    print(f'1 2 3 4 5 6 7\n')

    #for i in range(5):
    #    for j in range(6):
    #        print(f'|{''.join(board[i][j])}')

    print(f'\n{''.join(board[0])}\n{''.join(board[1])}\n{''.join(board[2])}\n{''.join(board[3])}\n{''.join(board[4])}\n{''.join(board[5])}')

def getLine(position): #Caso o index desejado esteja ocupado, muda a linha.
    if board[5][position] == ' ':
        line = 5
    elif board[5][position] != ' ':
        if board[4][position] == ' ':
            line = 4
        elif board[4][position] != ' ':
            if board[3][position] == ' ':
                line = 3
            elif board[3][position] != ' ':
                if board[2][position] == ' ':
                    line = 2
                elif board[2][position] != ' ':
                    if board[1][position] == ' ':
                        line = 1
                    elif board[1][position] != ' ':
                        if board[0][position] == ' ': 
                            line = 0
                        elif board[0][position] != ' ':
                            print('Coluna Cheia!')
    return line


def verifyLine(symbol):
    for line in range(lines):
        for col in range(cols - 3):
            if all(board[line][col + i] == symbol for i in range(4)):
                win(symbol)


def verifyColumn(symbol):
    for line in range(lines - 3):
        for col in range(cols):
            if all(board[line + i][col] == symbol for i in range(4)):
                win(symbol)

def verifyDiagonal1(symbol):
    for line in range(lines - 3):
        for col in range(cols -3):
            if all(board[line + i][col+i] == symbol for i in range(4)):
                win(symbol)

def verifyDiagonal2(symbol):
    for line in range(3, lines):
        for col in range(cols -3):
            if all(board[line - i][col+i] == symbol for i in range(4)):
                win(symbol)
            
def verifyAll(symbol): #Chama todas as funções de verificação.
    verifyLine(symbol)
    verifyColumn(symbol)
    verifyDiagonal1(symbol)
    verifyDiagonal2(symbol)

def symbol(player): #Define qual símbolo será desenhado de acordo com o jogador.
    if player == 1:
        symbol = 'x'
    else:
        symbol = 'o'
    return symbol

def win(symbol):
    global loop 
    if symbol == 'x':
        print('Jogador 1 venceu!')
    elif symbol == 'o':
        print('Jogador 2 venceu!')
    loop = 0

def redPlay(): #Jogador Vermelho
    player = 1
    print('----------Jogador 1----------')
    printBoard()
    print('-----------------------------')

    position = int(input('Jogada:'))
    line = getLine(position)
    board[line][position] = f'{symbol(player)}'

def bluePlay(): #Jogador Azul
    player = 2
    print('----------Jogador 2----------')
    printBoard()
    print('-----------------------------')
    
    position = int(input('Jogada:'))
    line = getLine(position)
    board[line][position] = f'{symbol(player)}'

def game():
    while loop == 1:
        redPlay()
        verifyAll('x')
        bluePlay()
        verifyAll('o')

    playAgain = int(input("Deseja jogar novamente?\n 1 - Sim | 2 - Não"))
    if playAgain == 1:
        reset()
        game()

    else:
        print('Até a próxima...')

reset()
game()