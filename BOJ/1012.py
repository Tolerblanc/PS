import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

t = int(input())
answer = []
graph = []

def bfs(x, y):
    if x < 0 or y < 0 or x > m - 1 or y > n - 1:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        bfs(x-1,y)
        bfs(x,y-1)
        bfs(x+1,y)
        bfs(x,y+1)
        return True
    return False

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    result = 0
    for i in range(m):
        for j in range(n):
            if (bfs(i, j) == True):
                result += 1
    answer.append(result)
for a in answer:
    print(a)