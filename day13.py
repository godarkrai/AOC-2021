points = set()
instructions = []
maxY = float("-inf")
maxX = float("-inf")
minX = float("inf")
minY = float("inf")
with open('day13input.txt') as f:
    inputs = f.read().splitlines()
    for i, input in enumerate(inputs):
        if input == "":
            break
        x, y = input.split(',')
        points.add((int(x), int(y)))
    for j in range(i+1, len(inputs)):
        instructions.append(inputs[j])

for instruction in instructions:
    _, _, whereToFold = instruction.split(' ')
    axis, point = whereToFold.split('=')
    point = int(point)
    newPoints = set()
    if axis == 'y':
        for p in points:
            x, y = p
            x = int(x)
            y = int(y)
            if y <= point:
                newPoints.add((x,y))
            else:
                newPoints.add((x,y-2*(y - point)))
    else:
        for p in points:
            x, y = p
            x = int(x)
            y = int(y)
            if x <= point:
                newPoints.add((x, y))
            else:
                newPoints.add((x-2*(x-point),y))
    points = newPoints
# DRAWING!
maxY = max([p[1] for p in points])
maxX = max([p[0] for p in points])
print()
for y in range(maxY+1):
    for x in range(maxX+1):
        if (x,y) in points:
            print('#',end='')
        else:
            print('.',end='')
    print()
print()

'''
Part 1: 785
Part 2:
####...##..##..#..#...##..##...##..#..#
#.......#.#..#.#..#....#.#..#.#..#.#..#
###.....#.#..#.####....#.#....#..#.####
#.......#.####.#..#....#.#.##.####.#..#
#....#..#.#..#.#..#.#..#.#..#.#..#.#..#
#.....##..#..#.#..#..##...###.#..#.#..#
'''

