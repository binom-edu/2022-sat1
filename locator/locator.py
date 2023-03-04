import random
from copy import deepcopy

def printBoard(showChests=False):
    bc = deepcopy(board)
    if showChests:
        for i, j in chests:
            bc[i][j] = '@'
    print('   ', end='')
    for j in range(WIDTH):
        print(j // 10, end='')
    print()
    print('   ', end='')
    for j in range(WIDTH):
        print(j % 10, end='')
    print()

    for i in range(HEIGHT):
        print("%2d" % i, '|', *bc[i], '|', i, sep='')
    
    print('   ', end='')
    for j in range(WIDTH):
        print(j // 10, end='')
    print()
    print('   ', end='')
    for j in range(WIDTH):
        print(j % 10, end='')
    print()

def makeBoard():
    board = []
    for i in range(HEIGHT):
        line = []
        for j in range(WIDTH):
            line.append(random.choice(EMPTY))
        board.append(line)
    return board

def makeChests():
    chests = []
    while len(chests) < MAX_CHESTS:
        i = random.randrange(0, HEIGHT)
        j = random.randrange(0, WIDTH)
        if not (i, j) in chests:
            chests.append((i, j))
    return chests

def getUserMove():
    while True:
        s = input('Ваш ход (номер строки и столбца через пробел): ').split()
        

WIDTH = 20
HEIGHT = 11
MAX_CHESTS = 3
EMPTY = '~-'
board = makeBoard()
chests = makeChests()
printBoard(showChests=True)
print(chests)