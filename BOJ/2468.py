import sys

#sys.stdin = open('input.txt')
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input().rstrip())
graph = []
max_height = 0
for _ in range(n):
    inp = list(map(int, input().rstrip().split()))
    max_height = max(max_height, max(inp))
    graph.append(inp)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, level):
    visited[x][y] = True
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if visited[nx][ny] or graph[nx][ny] <= level:
            continue
        dfs(nx, ny, level)

answer = 0
for i in range(max_height + 1):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y] > i and not visited[x][y]:
                dfs(x, y, i)
                cnt += 1
    answer = max(answer, cnt)
print(answer)