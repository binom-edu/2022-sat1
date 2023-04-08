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
    for i in range(8):
        print(*board[i])


board = getNewBoard()
printBoard(board)