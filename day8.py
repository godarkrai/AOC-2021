signals = open('day8input.txt').read().splitlines()

def getNumberFromWord(word, d):
    if len(word) == 2:
        return 1
    if len(word) == 3:
        return 7
    if len(word) == 4:
        return 4
    if len(word) == 7:
        return 8
    if len(word) == 5:
        s = set(word)
        if   len(s & d[2]) == 2: return 3
        elif len(s & d[4]) == 2: return 2
        else:                    return 5
    else: # l == 6
        s = set(word)
        if   len(s & d[2]) == 1: return 6
        elif len(s & d[4]) == 4: return 9
        else:                    return 0
'''
fdgacbe cefdb cefbgd gcbe: 8394 c
fcgedb cgb dgebacf gc: 9781 c
cg cg fdcagb cbg: 1197 c
efabcd cedba gadfec cb: 9361 c
gecf egdcabf bgf bfgea: 4873 c
gebdcfa ecba ca fadegcb: 8418 c
cefg dcbef fcge gbcadfe: 4548 c
ed bcgafe cdgba cbgef: 1625 x 1952
gbdfcae bgc cg cgb: 8717 c
fgae cfgab fg bagce: 4315 x 4312
'''
count = 0
total = 0
for signal in signals:
    decoded, code = signal.split(' | ')
    d = {
        l: set(s)
        for s in decoded.split()
        if (l := len(s)) in (2, 4)
    }
    curTotal = 0
    for word in code.split():
        curTotal = curTotal * 10 + getNumberFromWord(word, d)
        if len(word) in [2,3,4,7]:
            count += 1
    print(curTotal)
    total += curTotal

print("Part 1:", count)
print("Part 2:", total)
