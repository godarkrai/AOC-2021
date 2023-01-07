with open('day3input.txt') as f:
    lines = f.read().splitlines()

gammaRate = ''
cols = len(lines[0])
for col in range(cols):
    numberOfOnes = 0
    for row in range(len(lines)):
        numberOfOnes += int(lines[row][col])
    numberOfZeroes = len(lines) - numberOfOnes
    gammaRate += str(int(numberOfOnes > numberOfZeroes))

epsilon = ''
for bit in gammaRate:
    epsilon += '0' if bit == '1' else '1'

gammaRateToDecimal = 0
epsilonToDecimal = 0
i = 0
for j in range(len(gammaRate) - 1, -1, -1):
    gammaRateToDecimal += int(gammaRate[j]) * 2**i
    epsilonToDecimal += int(epsilon[j]) * 2**i
    i += 1
print("Part 1:", gammaRateToDecimal * epsilonToDecimal) # 3633500

# Part 2
oxygenGenerator = lines.copy()
cols = len(lines[0])
while len(oxygenGenerator) != 1:
    for col in range(cols):
        if len(oxygenGenerator) == 1:
            break
        numberOfOnes = 0
        numberOfZeroes = 0
        for row in range(len(oxygenGenerator)):
            numberOfOnes += int(oxygenGenerator[row][col])
        numberOfZeroes = len(oxygenGenerator) - numberOfOnes
        if numberOfOnes >= numberOfZeroes:
            dominatingBit = '1'
        else:
            dominatingBit = '0'
        tempOG = oxygenGenerator.copy()
        for code in tempOG:
            if code[col] != dominatingBit:
                oxygenGenerator.remove(code)
carbonGenerator = lines.copy()
while len(carbonGenerator) != 1:
    for col in range(cols):
        if len(carbonGenerator) == 1:
            break
        numberOfOnes = 0
        numberOfZeroes = 0
        for row in range(len(carbonGenerator)):
            numberOfOnes += int(carbonGenerator[row][col])
        numberOfZeroes = len(carbonGenerator) - numberOfOnes
        if numberOfZeroes == numberOfOnes:
            dominatingBit = '0'
        elif numberOfZeroes > numberOfOnes:
            dominatingBit = '1' # Take the fewer bits
        else:
            dominatingBit = '0'
        tempCG = carbonGenerator.copy()
        for code in tempCG:
            if code[col] != dominatingBit:
                carbonGenerator.remove(code)
oxygenGeneratorToDecimal = 0
carbonGeneratorToDecimal = 0
i = 0
for j in range(len(oxygenGenerator[0]) - 1, -1, -1):
    oxygenGeneratorToDecimal += int(oxygenGenerator[0][j]) * 2**i
    carbonGeneratorToDecimal += int(carbonGenerator[0][j]) * 2**i
    i += 1
print("Part 2:", oxygenGeneratorToDecimal * carbonGeneratorToDecimal) # 4550283