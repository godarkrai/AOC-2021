with open('day2input.txt') as f:
    lines = f.read().splitlines()


x = 0
y = 0
aim = 0 # Part 2

# Since we are in a submarine, down = + and up = -
# Part 1 - 1855814
# for line in lines:
#     direction, amount = line.split()
#     if direction == 'forward':
#         x += int(amount)
#     if direction == 'down':
#         y += int(amount)
#     if direction == 'up':
#         y -= int(amount)

# Part 2 - 1845455714
for line in lines:
    direction, amount = line.split()
    amount = int(amount)
    if direction == 'forward':
        x += amount
        y += aim * amount
    if direction == 'down':
        aim += amount
    if direction == 'up':
        aim -= amount
print(x,y, x*y)