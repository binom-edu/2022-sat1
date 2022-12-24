import random

def printBoard(board):
    print(board[7], '|', board[8], '|', board[9])
    print('-' * 9)
    print(board[4], '|', board[5], '|', board[6])
    print('-' * 9)
    print(board[1], '|', board[2], '|', board[3])

def getUserMove(board):
    pass

board = [' '] * 10
board[8] = 'O'
board[5] = 'X'
printBoard(board)

turn = random.choice(['user', 'computer'])
print('Первым ходит:', turn)