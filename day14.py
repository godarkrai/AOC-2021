polymer = ''
instructions = {}
rules = {}
with open('day14input.txt') as f:
    for i, line in enumerate(f.read().splitlines()):
        if i == 0:
            polymer = line
        elif line == '':
            continue
        else:
            wordPair, insertWhat = line.split(' -> ')
            rules[wordPair] = insertWhat
            instructions[wordPair] = wordPair[0] + insertWhat + wordPair[1]

from collections import Counter, deque, defaultdict
# Brute Force worked
def part1(polymer):
    for i in range(10):
        newPolymer = ''
        queue = deque()
        for ch in polymer:
            if len(queue) == 2:
                word = ''.join(queue)
                if word in instructions:
                    newWord = instructions[word]
                    newPolymer += newWord[:-1]
                queue.popleft()
            queue.append(ch)
        word = ''.join(queue)
        if word in instructions:
            newWord = instructions[word]
            newPolymer += newWord
        polymer = newPolymer
    maxLetter = max(Counter(polymer).items(), key=lambda x: x[1])
    minLetter = min(Counter(polymer).items(), key=lambda x: x[1])
    return maxLetter[1] - minLetter[1]

print("Part 1:", part1(polymer)) # 3555

# For part 2 count the number of pairs
def part2(polymer):

    steps = 4

    atomCount = defaultdict(int)
    for atom in polymer:
        atomCount[atom] += 1
    
    # Count pair
    pairCount = defaultdict(int)
    for i in range(len(polymer) - 1):
        pairCount[polymer[i:i+2]] += 1

    for _ in range(40):
        # Create a copy beacuse the value of pairCount keeps on changing but we would want to deal
        # with the original values
        pairCountCopy = pairCount.copy()
        for pair, value in rules.items():
            oldCountValue = pairCountCopy[pair]
            if oldCountValue == 0:
                continue
            newPair1 = pair[0] + value
            newPair2 = value + pair[1]
            pairCount[pair] -= oldCountValue
            pairCount[newPair1] += oldCountValue
            pairCount[newPair2] += oldCountValue
            atomCount[value] += oldCountValue
    maxLetter = max(atomCount.items(), key=lambda x:x[1])
    minLetter = min(atomCount.items(), key=lambda x:x[1])
    return maxLetter[1] - minLetter[1]
print("Part 2:", part2(polymer)) # 4439442043739




    

