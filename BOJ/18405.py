import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
virus = []
check = [False] * (k + 1)
for i in range(n):
    inp = list(map(int, input().split()))
    graph.append(inp)
    for j in range(n):
        if inp[j] != 0:
            virus.append((inp[j], 0, i, j))

sec, retX, retY = map(int, input().split())

virus.sort()
q = deque(virus)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(q, graph):
    while q:
        spec, s, x, y = q.popleft()
        if s == sec:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = spec
                q.append((spec, s + 1, nx, ny))

bfs(q, graph)
print(graph[retX - 1][retY - 1])