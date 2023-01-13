amatrix = []

with open('day15input.txt') as f:
    for lines in f.read().splitlines():
        amatrix.append(list(map(int, [*lines])))

#Dijkstra

from collections import deque
import heapq

def bfs(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    start = (0,(0,0))
    end = (len(matrix)-1, len(matrix[0])-1)

    heap = []
    heap.append(start)
    visited = set()
    visited.add((start[0], start[1]))
    while heap:
        risk, coords = heapq.heappop(heap)
        row, col = coords
        if (row, col) == end:
            return risk
        for newRow, newCol in [(row+1,col), (row, col+1), (row-1, col), (row, col-1)]:
            if (newRow, newCol) in visited:
                continue
            visited.add((newRow, newCol))
            if 0 <= newRow < rows and 0 <= newCol < cols:
                heapq.heappush(heap, (risk + matrix[newRow][newCol], (newRow, newCol)))
    return risk

print("Part 1:", bfs(amatrix))

rows = len(amatrix)
cols = len(amatrix[0])

# For part 2 duplicate the matrix
newMatrix = []
for row in range(rows):
    for i in range(4):
        matrixCopy = amatrix[row][i*cols:].copy()
        for digit in matrixCopy:
            if digit + 1 <= 9:
                amatrix[row].append(digit+1)
            else:
                amatrix[row].append(1)
    newMatrix.append(amatrix[row])

for i in range(4):
    for row in range(i*rows, len(newMatrix)):
        matrixCopy = newMatrix[row].copy()
        newRow = []
        for digit in matrixCopy:
            if digit + 1 <= 9:
                newRow.append(digit+1)
            else:
                newRow.append(1)
        newMatrix.append(newRow)

print("Part 2:", bfs(newMatrix))
