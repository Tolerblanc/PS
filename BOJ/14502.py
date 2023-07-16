import sys, copy
from itertools import combinations

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
walls = []
virus = []
for i in range(n):
    inp = list(map(int, input().split()))
    graph.append(inp)
    for j in range(m):
        if inp[j] == 0:
            walls.append((i, j))
        if inp[j] == 2:
            virus.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
comb_walls = list(combinations(walls, 3))

def check_safety(maps):
    safe = 0
    for ma in maps:
        for m in ma:
            if m == 0:
                safe += 1
    return safe

def dfs(x, y, maps):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if maps[nx][ny] == 0:
            maps[nx][ny] = 2
            dfs(nx, ny, maps)
        
result = 0
for wall in comb_walls:
    newmap = copy.deepcopy(graph)
    for x, y in wall:
        newmap[x][y] = 1
    for x, y in virus:
        dfs(x, y, newmap)
    result = max(result, check_safety(newmap))

print(result)