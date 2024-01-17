import sys
input = sys.stdin.readline
sys.setrecursionlimit(10001)

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

max_dist, max_node = 0, 0


def dfs(visited, curr, depth):
    global max_dist, max_node
    for next_node, cost in graph[curr]:
        if visited[next_node]:
            continue
        if max_dist < depth + cost:
            max_dist = depth + cost
            max_node = next_node
        visited[next_node] = True
        dfs(visited, next_node, depth + cost)


visited = [False] * (n + 1)
visited[1] = True
dfs(visited, 1, 0)

visited = [False] * (n + 1)
visited[max_node] = True
dfs(visited, max_node, 0)

print(max_dist)
