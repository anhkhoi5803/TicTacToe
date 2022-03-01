XO = 'X'
gameBoard = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]


def draw(array):
    for x in range(len(array)):
        for y in range(len(array[0])):
            if y == 2:
                print(array[x][y])
                break
            print(array[x][y], end="|")
        if x != 2:
            print("-----")


def isValid(board, p):
    for x in range(len(board)):
        for y in range(len(board[0])):
            # if p == board[x][y] and p != 'X' and p != 'O':
            if p == board[x][y]:
                return True
    return False


def move(board, p, player):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if p == board[x][y]:
                board[x][y] = player
    return board


def gameOver(board):
    for x in range(3):
        if winbyrow(board, x) or winbycolumn(board, x):
            return True

    for x in range(3):
        check = board[0][0]
        if board[x][x] != check:
            break
        if x == 2:
            return True

    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return True

    return False


def winbyrow(board, row):
    if board[row][0] == board[row][1] and board[row][0] == board[row][2]:
        return True
    return False


def winbycolumn(board, col):
    if board[0][col] == board[1][col] and board[0][col] == board[2][col]:
        return True
    return False


run = True

while run:
    draw(gameBoard)
    print("Player ", XO, " turn please enter position(1-9)!\n")
    pos = input()

    if not isValid(gameBoard, pos):
        print("Invalid position")
        continue

    gameBoard = move(gameBoard, pos, XO)
    if gameOver(gameBoard):
        print("Player", XO, "win!!! \n")
        run = False

    if XO == 'X':
        XO = 'O'
    else:
        XO = 'X'
