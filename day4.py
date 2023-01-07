with open('day4input.txt') as f:
    lines = f.read().splitlines()

calls = lines[0].split(',')
boards = {}
i = 0
for line in lines[2:]:
    numbers = line.split()
    if len(numbers) == 0:
        continue
    board = i//5
    i += 1
    if board in boards:
        boards[board].append(numbers)
    else:
        boards[board] = [numbers]

def checkRow(board):
    for row in range(len(board)):
        sum = 0
        for col in range(len(board[0])):
            sum += int(board[row][col])
        if sum == -5:
            return True
    return False

def checkCol(board):
    for col in range(len(board[0])):
        sum = 0
        for row in range(len(board)):
            sum += int(board[row][col])
        if sum == -5:
            return True
    return False

def checkWinner(call):
    for i, board in boards.items():
        # Don't check winning if the board has already won
        if i in winningBoards:
            continue
        if checkRow(board) or checkCol(board):
            winningBoards.append(i)
            winningBoardsWithCalls.append((i, call, board))

def markNumber(board, number):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == number:
                board[row][col] = -1
                # Number found, just return because number is unique in Bingo board
                return

winningBoards = []
winningBoardsWithCalls = []

def solve(part):
    for call in calls:
        for i, board in boards.items():
            # Skip winning boards
            if i in winningBoards:
                continue
            markNumber(board, call)
            checkWinner(call)
            if part == 1 and len(winningBoards) > 0:
                return

solve(1)
board = winningBoardsWithCalls[-1][2]
winningNumber = int(winningBoardsWithCalls[-1][1])
unmarkedTotal = 0
for row in range(len(board)):
    for col in range(len(board[0])):
        if board[row][col] != -1:
            unmarkedTotal += int(board[row][col])
print("Part 1:", winningNumber * unmarkedTotal) # 27027

solve(2)
board = winningBoardsWithCalls[-1][2]
winningNumber = int(winningBoardsWithCalls[-1][1])
unmarkedTotal = 0
for row in range(len(board)):
    for col in range(len(board[0])):
        if board[row][col] != -1:
            unmarkedTotal += int(board[row][col])
print("Part 2:", winningNumber * unmarkedTotal) # 36975