import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]
q = deque()

def bfs():
    for a in range(m):
        for b in range(n):
            if graph[a][b] == 1:
                q.append((a, b, 0))
    if not q:
        return -1
    while q:
        y, x, day = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = 1
                q.append((ny, nx, day + 1))
    for a in range(m):
        for b in range(n):
            if graph[a][b] == 0:
                return -1
    return day
    
print(bfs())