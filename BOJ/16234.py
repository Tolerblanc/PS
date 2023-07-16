import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(x, y, idx):
    united = [(x, y)]
    q = deque()
    pop = graph[x][y]
    q.append((x, y))
    union[x][y] = idx
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if (union[nx][ny] == -1) and (l <= abs(graph[x][y] - graph[nx][ny]) <= r):
                united.append((nx, ny))
                union[nx][ny] = idx
                pop += graph[nx][ny]
                q.append((nx, ny))
    pop = pop // len(united)
    for x, y in united:
        graph[x][y] = pop

cnt = 0

while True:
    union =[[-1] * n for _ in range(n)]
    idx = 0
    for a in range(n):
        for b in range(n):
            if union[a][b] == -1:
                move(a, b, idx)
                idx += 1
    if idx == n * n:
        break
    cnt += 1
print(cnt)