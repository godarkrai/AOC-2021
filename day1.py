from collections import deque

with open('day1input.txt') as f:
    lines = f.read().splitlines()

# Part 1 - 1532
# prevNum = int(lines[0])
# totalIncreased = 0
# for num in lines[1:]:
#     num = int(num)
#     if num > prevNum:
#         totalIncreased += 1
#     prevNum = num
# print(totalIncreased)

# Part 2 - 1571
queue = deque()
prevSum = None
totalIncreased = 0
for num in lines:
    queue.append(int(num))
    if len(queue) >= 3:
        queueSum = sum(queue)
        if prevSum is not None and queueSum > prevSum:
            totalIncreased += 1
        prevSum = queueSum
        queue.popleft()
print(totalIncreased)
