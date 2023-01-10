with open('day10input.txt') as f:
    brackets = f.read().splitlines()

for i in range(len(brackets)):
    brackets[i] = [*brackets[i]] # * converts 123 into 1 2 3 and [] coverts it into [1,2,3]

bracketMap = {
    '}': '{',
    ']': '[',
    '>': '<',
    ')': '('
}
bracketMapReversed = {v:k for k,v in bracketMap.items()}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

points2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

total = 0
scores = []
for bracketString in brackets:
    stack = []
    illegalBracket = ''
    for bracket in bracketString:
        if bracket in ')}>]':
            if stack:
                if stack[-1] == bracketMap[bracket]:
                    stack.pop()
                    continue
                else:
                    illegalBracket = bracket
                    break
        stack.append(bracket)
    if illegalBracket != '':
        total += points[illegalBracket]
    else: # Incomplete
        toComplete = []
        for bracket in stack[::-1]:
            toComplete.append(bracketMapReversed[bracket])
            stack.pop()
        score = 0
        for b in toComplete:
            score *= 5
            score += points2[b]
        scores.append(score)

midValue = ( 0 + len(scores) ) // 2
print("Part 1:", total)
print("Part 2:", sorted(scores)[midValue])