import random

def printBoard():
    for j in range(WIDTH):
        print(j // 10, end='')
    print()
    for j in range(WIDTH):
        print(j % 10, end='')
    print()
    for i in range(HEIGHT):
        print("%2d" % i, '|', *board[i], sep='')

def makeBoard():
    board = []
    for i in range(HEIGHT):
        line = []
        for j in range(WIDTH):
            line.append(random.choice(EMPTY))
        board.append(line)
    return board

WIDTH = 20
HEIGHT = 11
EMPTY = '~-'
board = makeBoard()
printBoard()