import functools
import itertools
p1Start = 0
p2Start = 0

with open('day21input.txt') as f:
    lines = f.read().splitlines()
    p1Start = int(lines[0].split(': ')[1])
    p2Start = int(lines[1].split(': ')[1])

# Part 1: First to 1000 score

die = 100
p1Score = 0
p2Score = 0
p1StartingDieTotal = 6
p2StartingDieTotal = 15

'''
Player 1 rolls 1+2+3 and moves to space 10 for a total score of 10.
Player 2 rolls 4+5+6 and moves to space 3 for a total score of 3.
Player 1 rolls 7+8+9 and moves to space 4 for a total score of 14.
Player 2 rolls 10+11+12 and moves to space 6 for a total score of 9.
Player 1 rolls 13+14+15 and moves to space 6 for a total score of 20.
Player 2 rolls 16+17+18 and moves to space 7 for a total score of 16.
Player 1 rolls 19+20+21 and moves to space 6 for a total score of 26.
Player 2 rolls 22+23+24 and moves to space 6 for a total score of 22.
Player 1 rolls 25+26+27 and moves to space 4 for a total score of 30.
'''
for i in range(1000):
    p1NewPosition = ( p1Start + p1StartingDieTotal ) % 10
    if p1NewPosition == 0:
        p1NewPosition = 10
    p1Score += p1NewPosition
    if p1Score >= 1000 or p2Score >= 1000:
        break
    p2NewPosition = ( p2Start + p2StartingDieTotal ) % 10
    if p2NewPosition == 0:
        p2NewPosition = 10
    p2Score += p2NewPosition
    if p1Score >= 1000 or p2Score >= 1000:
        break
    p1Start = p1NewPosition
    p2Start = p2NewPosition
    p1StartingDieTotal += 18
    p2StartingDieTotal += 18

print(p1Score, p2Score, i*3*2+3)
print("Part 1:", (i*3*2+3)*p2Score)
# Part 1: 916083

# Part 2 Recursion
@functools.lru_cache(maxsize=None)
def play(p1Start, p1Score, p2Start, p2Score):
    p1Wins = p2Wins = 0

    for dice1, dice2, dice3 in itertools.product((1,2,3),(1,2,3),(1,2,3)):
        p1NewPosition = (p1Start+dice1+dice2+dice3) % 10 if (p1Start+dice1+dice2+dice3) % 10 else 10
        newP1Score = p1Score + p1NewPosition
        if newP1Score >= 21:
            p1Wins += 1
        else:
            p2NewWins, p1NewWins = play(p2Start, p2Score, p1NewPosition, newP1Score)
            p1Wins += p1NewWins
            p2Wins += p2NewWins
    return p1Wins, p2Wins

p1Start = int(lines[0].split(': ')[1])
p2Start = int(lines[1].split(': ')[1])
print("Part 2:", max(play(p1Start, 0, p2Start, 0))) # 49982165861983