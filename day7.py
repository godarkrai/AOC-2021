
positions = list(map(int, open('day7input.txt').read().split(',')))

minCost = float("inf")
for i in range(len(positions)):
    cost = 0
    for position in positions:
        cost += abs( position - i ) # 16 to 0 = 16 - 0 = 0
    minCost = min(minCost, cost)
print(minCost) # Part 1: 347449

# Part 2: Arithmatic Sum n/2[2a+(n-1)d]
# So if we are moving from 16 to 0, a = 1, n = (16-0) and d = 1
# So (16/2)*(2*1 + (16-1)*1) => (8)*(15+2) = 136
# If we are moving from 16 to 5, a = 1 n = 16-5 and d = 1
# (11/2)*(2*1 + (11-1)*1) => (11/2) * (2+10) => 66
# If we are moving from 14 to 5, a = 1, n = 14-5 and d = 1
# (9/2) * (2*1 + (9-1)*1) => (9/2)*(2+8) => 45

def aSum( n, a = 1, d = 1):
    return (n/2)*((2*a)+(n-1)*d)
minCost = float("inf")
for i in range(len(positions)):
    cost = 0
    for position in positions:
        cost += aSum( abs(position - i) )
    minCost = min(minCost, cost)
print(minCost) # Part 2: 98039527
