import random

def printBoard(board):
    print(board[7], '|', board[8], '|', board[9])
    print('-' * 9)
    print(board[4], '|', board[5], '|', board[6])
    print('-' * 9)
    print(board[1], '|', board[2], '|', board[3])

def getUserMove(board):
    alf = '123456789'
    while True:
        s = input('Ваш ход: ').lower()
        if len(s) != 1:
            print('Нужно ввести ровно один символ!')
            continue
        if not s in alf:
            print('Требуется ввести цифру')
            continue
        s = int(s)
        if board[s] != ' ':
            print('Это поле уже занято')
            continue
        return s

def makeMove(board, tile, move):
    board[move] = tile

def checkVictory(board, tile):
    if  board[1] == tile and board[2] == tile and board[3] == tile or \
        board[4] == tile and board[5] == tile and board[6] == tile or \
        board[7] == tile and board[8] == tile and board[9] == tile or \
        board[1] == tile and board[4] == tile and board[7] == tile or \
        board[2] == tile and board[5] == tile and board[8] == tile or \
        board[3] == tile and board[6] == tile and board[9] == tile or \
        board[1] == tile and board[5] == tile and board[9] == tile or \
        board[3] == tile and board[5] == tile and board[7] == tile:
        return True
    return False

def checkDraw(board):
    if checkVictory(board, userTile) or checkVictory(board, computerTile):
        return False
    for i in board:
        if i == ' ':
            return False
    return True

def getComputerMove(board):
    valid_moves = []
    for i in range(1, 10):
        if board[i] == ' ':
            valid_moves.append(i)
    return random.choice(valid_moves)

print('Крестики-нолики')
print('Используйте цифровую клавиатуру, чтобы сделать ход.')

tiles = ['X', 'O']
random.shuffle(tiles)
userTile = tiles[0]
computerTile = tiles[1]
print('Вы играете за', userTile)
ans = input('Поменять (y / n)? ')
if ans.lower().startswith('y'):
    userTile, computerTile = computerTile, userTile
    print('Теперь вы играете за', userTile)


board = [' '] * 10

turn = random.choice(['user', 'computer'])
print('Первым ходит:', turn)

gameOn = True
while gameOn:
    printBoard(board)
    if turn == 'user':
        userMove = getUserMove(board)
        makeMove(board, userTile, userMove)
        if checkVictory(board, userTile):
            print('Вы победили!')
            gameOn = False
        turn = 'computer'
    else:
        print('Ход компьютера')
        computerMove = getComputerMove(board)
        makeMove(board, computerTile, computerMove)
        if checkVictory(board, computerTile):
            print('Победил компьютер')
            gameOn = False
        turn = 'user'