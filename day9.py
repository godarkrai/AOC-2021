with open('day9input.txt') as f:
    flows = f.read().splitlines()

flowsToMatrix = []

for flow in flows:
    curLine = [*flow] # * converts 123 into 1 2 3 and [] coverts it into [1,2,3]
    flowsToMatrix.append(list(map(int, curLine)))

rows = len(flowsToMatrix)
cols = len(flowsToMatrix[0])

def lowestPoint(row, col, point):
    # Check Right
    if col + 1 < cols:
        if flowsToMatrix[row][col+1] <= point:
            return False
    if row + 1 < rows:
        if flowsToMatrix[row+1][col] <= point:
            return False
    if row - 1 >= 0:
        if flowsToMatrix[row-1][col] <= point:
            return False 
    if col - 1 >= 0:
        if flowsToMatrix[row][col-1] <= point:
            return False
    return True

lowestPoints = []
lpCords = []
for row in range(rows):
    for col in range(cols):
        # Right, Left, Top and Bottom
        if lowestPoint(row, col, flowsToMatrix[row][col]):
            lowestPoints.append(flowsToMatrix[row][col])
            lpCords.append((row, col))

def increaseByOne(element):
    return element + 1

print("Part 1:", sum(list(map(increaseByOne, lowestPoints)))) # 607

# Simple DFS, start from the smallest points calculated above (lpCords)

# Part 2:
def dfs(x, y, prevValue):
    if ( x < 0 or x == rows or y < 0 or y == cols or flowsToMatrix[x][y] <= prevValue or flowsToMatrix[x][y] == 9 or flowsToMatrix[x][y] == -1):
        return 0

    value = flowsToMatrix[x][y]
    flowsToMatrix[x][y] = -1
    total = 1
    total += dfs(x+1, y, value)
    total += dfs(x-1, y, value)
    total += dfs(x, y+1, value)
    total += dfs(x, y-1, value)
    return total

points = []
for lowestPoint in lpCords:
    x, y = lowestPoint
    total = dfs(x, y, -2)
    points.append(total)

product = 1
for point in sorted(points)[::-1][:3]:
    product *= point
print("Part 2:", product) # 900864

    

    

