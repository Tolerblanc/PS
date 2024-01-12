import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
dist = [-1] * (n + 1)

a, b = map(int, input().split())
m = int(input())
dist[a] = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(curr, end, depth):
    if curr == end:
        return
    for dst in graph[curr]:
        if dist[dst] == -1:
            dist[dst] = depth + 1
            dfs(dst, end, depth + 1)


dfs(a, b, 0)
print(dist[b])
