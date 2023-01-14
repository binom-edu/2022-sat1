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
board[8] = 'O'
board[5] = 'X'
printBoard(board)

turn = random.choice(['user', 'computer'])
print('Первым ходит:', turn)

userMove = getUserMove(board)
makeMove(board, userTile, userMove)
printBoard(board)