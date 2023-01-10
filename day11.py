matrix = []
with open('day11input.txt') as f:
    for numbers in f.read().splitlines():
        numberLine = [*numbers]
        matrix.append(list(map(int, numberLine)))


rows = len(matrix)
cols = len(matrix[0])

def dfs(x, y):
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return
    
    for nx, ny in [(x,y+1), (x+1,y), (x,y-1), (x-1,y), (x+1,y+1), (x+1,y-1), (x-1,y+1), (x-1,y-1)]:
        if 0 <= nx < rows and 0 <= ny < cols:
            if matrix[nx][ny] < 9 and (nx, ny) not in flashed:
                matrix[nx][ny] += 1
            elif matrix[nx][ny] == 9:
                flashed.add((nx,ny))
                matrix[nx][ny] = 0
                dfs(nx, ny)
    
totalFlashes = 0
for i in range(1000):
    flashed = set()
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] < 9 and (row, col) not in flashed:
                matrix[row][col] += 1
            elif matrix[row][col] == 9:
                flashed.add((row, col))
                matrix[row][col] = 0
                dfs(row, col)
    if len(flashed) == rows * cols: # Part 2
        break
    totalFlashes += len(flashed) # Part 1 (Only loop for 100)

print("Part 1:", totalFlashes) # 1601
print("Part 2:", i+1) # 368
