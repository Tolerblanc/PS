import sys
from collections import deque
#sys.stdin = open('input.txt')
input = sys.stdin.readline

tile = {'.' : 0, '*' : -1, 'X' : 1, 'D' : 3, 'S' : 2}
r, c = map(int, input().rstrip().split())
graph = []
water = deque()
hedge = deque()
for i in range(r):
    temp = [tile[x] for x in input().rstrip()]
    graph.append(temp)
    for j in range(c):
        if temp[j] == 2:
            hedge.append((i, j, 0))
        if temp[j] == 3:
            dst = (i, j)
        if temp[j] == -1:
            water.append((i, j, 0))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
flag = True
while flag:
    if len(hedge) < 1:
        print("KAKTUS")
        break
    for _ in range(len(water)):
        row, col, t = water.popleft()
        for i in range(4):
            nr = row + dx[i]
            nc = col + dy[i]
            if nr < 0 or nc < 0 or nr >= r or nc >= c:
                continue
            if graph[nr][nc] == 0 or graph[nr][nc] == 2:
                graph[nr][nc] = -1
                water.append((nr, nc, t + 1))
    for _ in range(len(hedge)):
        row, col, t = hedge.popleft()
        if row == dst[0] and col == dst[1]:
            print(t)
            flag = False
            break
        for i in range(4):
            nr = row + dx[i]
            nc = col + dy[i]
            if nr < 0 or nc < 0 or nr >= r or nc >= c:
                continue
            if graph[nr][nc] == 0 or graph[nr][nc] == 3:
                graph[nr][nc] = 2
                hedge.append((nr, nc, t + 1))