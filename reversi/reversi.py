import random

EMPTY = '⋅'
TILES = ['○', '●']

def getNewBoard() -> list:
    '''Создает новую доску'''
    board = []
    for i in range(8):
        board.append([EMPTY] * 8)
    board[3][3] = TILES[0]
    board[4][4] = TILES[0]
    board[4][3] = TILES[1]
    board[3][4] = TILES[1]
    return board

def printBoard(board: list) -> None:
    '''Печатает доску'''
    print('  a b c d e f g h')
    for i in range(8):
        print(8 - i, *board[i], 8 - i)
    print('  a b c d e f g h')

def getTilesToFlip(x: int, y: int, tile: str) -> list:
    '''Создает список фишек, которые будут перевернуты, если сделать ход в x, y'''
    otherTile = TILES[(TILES.index(tile) + 1) % 2]
    directions = [
        [-1, 0],
        [-1, 1],
        [0, 1],
        [1, 1],
        [1, 0],
        [1, -1],
        [0, -1],
        [-1, -1]
    ]
    ans = []
    for dx, dy in directions:
        i, j = x, y
        while 0 <= i < 8 and 0 <= j < 8:
            i += dx
            j += dy
            if i < 0 or i > 7 or j < 0 or j > 7:
                break
            if board[i][j] == EMPTY:
                break
            if board[i][j] == otherTile:
                continue
            i -= dx
            j -= dy
            while (i, j) != (x, y):
                ans.append([i, j])
                i -= dx
                j -= dy
            break
    return ans
        
def getUserMove() -> list:
    '''Получает ход игрока с проверкой корректности'''
    while True:
        s = input('Ваш ход. Используйте шахматную нотацию (например, b6): ')
        if len(s) != 2:
            print('Ожидается ровно два символа')
            continue
        if not s[0] in 'abcdefgh' or not s[1] in '12345678':
            print('Используйте шахматную нотацию')
            continue
        row = 8 - int(s[1])
        column = 'abcdefgh'.find(s[0])
        if board[row][column] != EMPTY:
            print('Это поле занято')
            continue
        if len(getTilesToFlip(row, column, userTile)) == 0:
            print('В результате хода должны быть перевернуты фишки')
            continue
        return [row, column]

def makeMove(x: int, y: int, tile: str) -> None:
    tilesToFlip = getTilesToFlip(x, y, tile)
    for i, j in tilesToFlip:
        board[i][j] = tile
    board[x][y] = tile

def getValidMoves(tile: str) -> list:
    res = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == EMPTY and len(getTilesToFlip(i, j, tile)) > 0:
                res.append([i, j])
    return res

def getComputerMove() -> list:
    validMoves = getValidMoves(computerTile)
    if validMoves:
        return random.choice(validMoves)

board = getNewBoard()
printBoard(board)
userTile, computerTile = TILES

gameOn = True
turn = 'user'
while gameOn:
    if turn == 'user' and getValidMoves(userTile):
        i, j = getUserMove()
        makeMove(i, j, userTile)
        turn = 'computer'
    else:
        i, j = getComputerMove()
        makeMove(i, j, computerTile)
        turn = 'user'
    printBoard(board)