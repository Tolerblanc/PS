import sys

input = sys.stdin.readline

INF = 100000001
v, e = map(int, input().split())
graph = [[INF] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v + 1):
    for x in range(1, v + 1):
        for y in range(1, v + 1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

answer = INF
for i in range(1, v + 1):
    for j in range(1, v + 1):
        if graph[i][j] != INF and graph[j][i] != INF:
            answer = min(answer, graph[i][j] + graph[j][i])

if answer == INF:
    print(-1)
else:
    print(answer)