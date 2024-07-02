from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

for tc in range(int(input())):
    n = int(input())
    graph = []
    q = deque()
    for i in range(n):
        graph.append([int(x) for x in input().rstrip()])
        for j in range(n):
            if graph[-1][j] == 2:
                graph[i][j] = 1
                q.append((i, j))
            elif graph[-1][j] == 3:
                end = (i, j)

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= n or graph[nr][nc] == 1:
                continue
            graph[nr][nc] = 1
            q.append((nr, nc))

    print(f'#{tc + 1} {1 if graph[end[0]][end[1]] == 1 else 0}')
