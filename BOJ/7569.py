import sys
from collections import deque

input = sys.stdin.readline

n, m, h = map(int, input().split())
graph = [[] for _ in range(h)]
for i in range(h):
    for _ in range(m):
        graph[i].append(list(map(int, input().split())))

dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dh = [0,0,0,0,1,-1]
q = deque()

def bfs():
    for i in range(h):
        for a in range(m):
            for b in range(n):
                if graph[i][a][b] == 1:
                    q.append((i, a, b, 0))
    if not q:
        return -1
    while q:
        hh, y, x, day = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nh = hh + dh[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or nh < 0 or nh >= h:
                continue
            if graph[nh][ny][nx] == 0:
                graph[nh][ny][nx] = 1
                q.append((nh, ny, nx, day + 1))
    for i in range(h):
        for a in range(m):
            for b in range(n):
                if graph[i][a][b] == 0:
                    return -1
    return day
    
print(bfs())