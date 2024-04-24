from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 0, 0, -1, 1, -1, 1, -1]
dy = [0, 1, -1, 0, 1, -1, -1, 1]


def bfs(r, c, graph, n, m):
    q = deque([(r, c)])
    graph[r][c] = 0
    while q:
        r, c = q.popleft()
        for i in range(8):
            nr, nc = r + dx[i], c + dy[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue
            if not graph[nr][nc]:
                continue
            graph[nr][nc] = 0
            q.append((nr, nc))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    count = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j]:
                bfs(i, j, graph, h, w)
                count += 1
    print(count)
