import sys
sys.setrecursionlimit(10**6)
#sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input().rstrip())
graph = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for i in range(n):
    inp = input().rstrip()
    for j in range(n):
        if inp[j] == '1':
            graph[i][j] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = []
cnt = 0

def dfs(x, y):
    visited[x][y] = True
    global cnt
    cnt += 1
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == 0:
            continue
        if visited[nx][ny] == False:
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            dfs(i, j)
            answer.append(cnt)
            cnt = 0

answer.sort()
print(len(answer))
for a in answer:
    print(a)