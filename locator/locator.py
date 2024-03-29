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
        if len(s) != 2:
            print('Некорректный ввод')
            continue
        if not (s[0].isdigit() and s[1].isdigit()):
            print('Требуется ввести два числа')
            continue
        x = int(s[0])
        y = int(s[1])
        if not(0 <= x < HEIGHT and 0 <= y < WIDTH):
            print('Введенные координаты за пределами поля')
            continue
        return x, y

def getDistance(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    c = (a ** 2 + b ** 2) ** 0.5
    return int(c)

def getMinDistance(x1, y1):
    ans = 10
    for x2, y2 in chests:
        d = getDistance(x1, y1, x2, y2)
        if d < ans:
            ans = d
    return ans


WIDTH = 20
HEIGHT = 11
MAX_CHESTS = 3
EMPTY = '~-'
MAX_MOVES = 30

print(f'На карте спрятаны сундуки с сокровищами. У вас есть {MAX_MOVES} ходов, чтобы их найти. Используйте локаторы, чтобы узнать расстояние до ближайшего сундука.')

board = makeBoard()
chests = makeChests()

for moves in range(MAX_MOVES, 0, -1):
    printBoard(showChests=False)
    print(f'Осталось ходов: {moves}, сундуков: {len(chests)}')
    x, y = getUserMove()
    dist = getMinDistance(x, y)
    if dist == 0:
        print('Сундук найден!')
        board[x][y] = '@'
        chests.remove((x, y))
        if len(chests) == 0:
            print('Победа! Все сундуки найдены!')
            printBoard()
            break
    elif dist < 10:
        print(f'До ближайшего сундука {dist}')
        board[x][y] = dist
    else:
        print('Ничего не найдено')
        board[x][y] = 'X'
else:
    print('Ходы закончились. Вы проиграли')
    printBoard(showChests=True)