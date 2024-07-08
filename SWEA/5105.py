from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def solve(n, graph):
    q = deque()
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                q.append((i, j, 0))
                visited[i][j] = True
    while q:
        r, c, cost = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue
            if visited[nr][nc] or graph[nr][nc] == 1:
                continue
            if graph[nr][nc] == 3:
                return cost
            visited[nr][nc] = True
            q.append((nr, nc, cost + 1))
    return 0


for tc in range(int(input())):
    n = int(input())
    answer = solve(n, [[int(i) for i in input().rstrip()] for _ in range(n)])
    print(f'#{tc + 1} {answer}')
