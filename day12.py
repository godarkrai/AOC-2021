# import sys
# sys.setrecursionlimit(20000)
from collections import defaultdict

graph = defaultdict(list)

visited = {}

with open('day12input.txt') as f:
    for edge in f.read().splitlines():
        fromNode, toNode = edge.split('-')
        if fromNode.islower() and fromNode not in visited:
            visited[fromNode] = 0
        if toNode.islower() and toNode not in visited:
            visited[toNode] = 0
        graph[fromNode].append(toNode)
        graph[toNode].append(fromNode)

startNode = 'start'
endNode = 'end'
paths = []

def dfs(node, path):
    if node == endNode:
        if path not in paths:
            paths.append(path)
        return
    for neighbour in graph[node]:
        if neighbour == startNode:
            continue
        if neighbour in visited:
            # Change >= 1 for Part 1
            if visited[neighbour] + 1 >= 2 and 2 in visited.values():
                continue
            visited[neighbour] += 1
        dfs(neighbour, path+'-'+neighbour)
        if neighbour in visited:
            visited[neighbour] -= 1

dfs(startNode, startNode)
print(len(paths)) # Part 1 - 5920, Part 2 - 155477