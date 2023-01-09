signals = open('day8input.txt').read().splitlines()

'''
The letter 8:
    1
2       3
    4
5       6
    7
'''

def getNumberFromWord(word, dictionary):
    if len(word) == 2:
        return 1
    if len(word) == 3:
        return 7
    if len(word) == 4:
        return 4
    if len(word) == 7:
        return 8
    if len(word) == 5:
        # Letter 3 = All letters of 7 are in 3 so and 3 is the only length 5 word to have it
        hasAll = all([char in word for char in dictionary[7]])
        if hasAll:
            return 3
        elif len(set(word) & set(dictionary[4])) == 2:
            return 2
        else:
            return 5
    elif len(word) == 6: #either 6 or 9
        if len(set(word) & set(dictionary[1])) == 1:
            return 6
        elif len(set(word) & set(dictionary[4])) == 4:
            return 9
        else:
            return 0
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
    wordDictionary = {}
    # First make this dictionary because we are making other words from it
    for word in decoded.split():
        if len(word) == 2:
            wordDictionary[1] = word
        if len(word) == 3:
            wordDictionary[7] = word
        if len(word) == 4:
            wordDictionary[4] = word
        if len(word) == 7:
            wordDictionary[8] = word
    curTotal = 0
    for word in code.split():
        curTotal = curTotal * 10 + getNumberFromWord(word, wordDictionary)
        if len(word) in [2,3,4,7]:
            count += 1
    total += curTotal

print("Part 1:", count)
print("Part 2:", total)
