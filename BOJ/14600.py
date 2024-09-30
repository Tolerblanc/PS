import sys
input = sys.stdin.readline

k = int(input())
graph = [[1] * (k * 2) for _ in range(k * 2)]
x, y = map(int, input().split())
graph[2 * k - y][x - 1] = -1
visited = [[False] * (k * 2) for _ in range(k * 2)]
visited[2 * k - y][x - 1] = True
start_row = range(k, 2 * k) if 2 * k - y >= k else range(0, k)
start_col = range(k, 2 * k) if x - 1 >= k else range(0, k)

for r in start_row:
    for c in start_col:
        visited[r][c] = True


def plus_unvisited():
    for r in range(2 * k):
        for c in range(2 * k):
            if not visited[r][c]:
                graph[r][c] += 1


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

if k == 2:
    plus_unvisited()
    edges = [(0, 0), (0, 3), (3, 0), (3, 3)]
    for r, c in edges:
        if visited[r][c]:
            continue
        visited[r][c] = True
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
                continue
            visited[nr][nc] = True
        plus_unvisited()


for g in graph:
    print(*g)
