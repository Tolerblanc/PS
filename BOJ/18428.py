import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
graph = []
teachers = []
ground = []

for i in range(n):
    inp = list(input().split())
    graph.append(inp)
    for j in range(n):
        if inp[j] == 'T':
            teachers.append((i, j))
        if inp[j] == 'X':
            ground.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def watch(graph, teachers):
    for x, y in teachers:
        for i in range(4):
            j = 1
            while True:
                nx = x + (dx[i] * j)
                ny = y + (dy[i] * j)
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    break
                if graph[nx][ny] == 'S':
                    return False
                if graph[nx][ny] == 'O':
                    break
                j += 1
    else:
        return True

walls = list(combinations(ground, 3))
for wall in walls:
    for x, y in wall:
        graph[x][y] = 'O'
    if watch(graph, teachers):
        print("YES")
        break
    for x, y in wall:
        graph[x][y] = 'X'
else:
    print("NO")