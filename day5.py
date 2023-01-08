with open('day5input.txt') as f:
    lines = f.read().splitlines()

overlappingPoints = []
ranges = []
for line in lines:
    firstPoint, secondPoint = line.split(' -> ')
    x1, y1 = map(int, firstPoint.split(','))
    x2, y2 = map(int, secondPoint.split(','))
    if y1 == y2:
        minX = int(min(x1, x2))
        maxX = int(max(x1, x2))
        for x in range(minX, maxX + 1):
            if (x, y1) in ranges:
                if (x,y1) not in overlappingPoints:
                    overlappingPoints.append((x,y1))
            else:
                ranges.append((x, y1))
    elif x1 == x2:
        minY = int(min(y1, y2))
        maxY = int(max(y1, y2))
        for y in range(minY, maxY + 1):
            if (x1, y) in ranges:
                if (x1,y) not in overlappingPoints:
                    overlappingPoints.append((x1,y))
            else:
                ranges.append((x1, y))
    else: # Diagonal 6,4 -> 2,0
        # 2,0 -> 3,1 -> 4,2 -> 5,3 -> 6,4
        if x1 < x2 and y1 < y2: # 2,3 -> 3,4 Diagonal Down Right
            while x1 <= x2 and y1 <= y2:
                if (x1, y1) in ranges and (x1, y1) not in overlappingPoints:
                    overlappingPoints.append((x1, y1))
                else:
                    ranges.append((x1, y1))
                x1 += 1
                y1 += 1
        elif x1 > x2 and y1 < y2: # 8,0 -> 0,8 Diagonal Down Left x-, y+
            while x1 >= x2 and y1 <= y2:
                if (x1, y1) in ranges and (x1, y1) not in overlappingPoints:
                    overlappingPoints.append((x1, y1))
                else:
                    ranges.append((x1, y1))
                x1 -= 1
                y1 += 1
        elif x1 < x2 and y1 > y2: # 5,5 -> 8,2 x+, y- # Diagonal Up Right
            while x1 <= x2 and y1 >= y2:
                if (x1, y1) in ranges and (x1, y1) not in overlappingPoints:
                    overlappingPoints.append((x1, y1))
                else:
                    ranges.append((x1, y1))
                x1 += 1
                y1 -= 1
        else: # Diagonal Up Left x-, y-
            while x1 >= x2 and y1 >= y2:
                if (x1, y1) in ranges and (x1, y1) not in overlappingPoints:
                    overlappingPoints.append((x1, y1))
                else:
                    ranges.append((x1, y1))
                x1 -= 1
                y1 -= 1
print(len(overlappingPoints)) # Part 1: 7142 # Part 2: 20012
# TODO: TOO SLOW