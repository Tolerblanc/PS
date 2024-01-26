import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

time = 0
while True:
    visited = [[False] * m for _ in range(n)]
    melt = [[0] * m for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                if flag:
                    print(time)
                    exit()
                flag = True
                visited[i][j] = True
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                            melt[x][y] += 1
    total_melt = 0
    for i in range(n):
        for j in range(m):
            total_melt += melt[i][j]
            graph[i][j] = max(0, graph[i][j] - melt[i][j])
    if total_melt == 0:
        print(0)
        break
    time += 1
