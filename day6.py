with open('day6input.txt') as f:
    fishes = f.read().splitlines()

fishes = list(map(int, fishes[0].split(',')))

# Part 1: 380243
# Part 2: 1708791884591

def solve(days):
    currentState = {
        0: fishes.count(0),
        1: fishes.count(1),
        2: fishes.count(2),
        3: fishes.count(3),
        4: fishes.count(4),
        5: fishes.count(5),
        6: fishes.count(6),
        7: fishes.count(7),
        8: fishes.count(8),
    }

    for i in range(days):
        newState = {
            0: currentState[1],
            1: currentState[2],
            2: currentState[3],
            3: currentState[4],
            4: currentState[5],
            5: currentState[6],
            6: currentState[7] + currentState[0],
            7: currentState[8],
            8: currentState[0],
        }
        currentState = newState
    total = 0
    for fish in currentState:
        total += currentState[fish]
    return total

print("Part 1:", solve(80))
print("Part 2:", solve(256))
