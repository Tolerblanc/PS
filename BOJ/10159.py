import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

INF = 1000
n = int(input().rstrip())
graph = [[False] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = True

m = int(input().rstrip())
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a][b] = True
    
for k in range(1, n + 1):
    for x in range(1, n + 1):
        for y in range(1, n + 1): 
            graph[x][y] = True if (graph[x][k] and graph[k][y]) else graph[x][y]

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if not (graph[i][j] or graph[j][i]):
            cnt += 1
    print(cnt)