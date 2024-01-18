import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [[] for _ in range(n + 1)]
max_dist, max_node = 0, 0

for _ in range(n):
    v, *edges, _ = map(int, input().split())
    for i in range(0, len(edges), 2):
        graph[v].append((edges[i], edges[i + 1]))


def dfs(v, dist=0):
    global max_dist, max_node
    if dist > max_dist:
        max_dist = dist
        max_node = v
    for node, d in graph[v]:
        if not visited[node]:
            visited[node] = True
            dfs(node, dist + d)


visited = [False] * (n + 1)
visited[1] = True
dfs(1)

visited = [False] * (n + 1)
visited[max_node] = True
dfs(max_node)

print(max_dist)
