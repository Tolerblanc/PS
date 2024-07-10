import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
visited = [[False] * C for _ in range(R)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
graph = [list(input().rstrip()) for _ in range(R)]


def bfs(r, c):
    wolf = 0 if graph[r][c] != 'v' else 1
    sheep = 0 if graph[r][c] != 'o' else 1
    visited[r][c] = True
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nc < 0 or nr >= R or nc >= C:
                continue
            if graph[nr][nc] == '#' or visited[nr][nc]:
                continue
            if graph[nr][nc] == 'v':
                wolf += 1
            if graph[nr][nc] == 'o':
                sheep += 1
            visited[nr][nc] = True
            q.append((nr, nc))
    if sheep > wolf:
        wolf = 0
    else:
        sheep = 0
    return wolf, sheep


wolf, sheep = 0, 0
for i in range(R):
    for j in range(C):
        if graph[i][j] != '#' and not visited[i][j]:
            w, s = bfs(i, j)
            wolf += w
            sheep += s

print(sheep, wolf)
