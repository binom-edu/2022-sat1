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

board = getNewBoard()
printBoard(board)