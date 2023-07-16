import sys
from collections import deque

input = sys.stdin.readline

result_bfs = []
result_dfs = []
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph:
    i.sort()

def dfs(graph, start, visited):
    visited[start] = True
    result_dfs.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)
    
def bfs(graph, start, visited):
    q = deque()
    visited[start] = True
    q.append(start)
    result_bfs.append(start)
    while q:
        now = q.popleft()
        for n in graph[now]:
            if not visited[n]:
                q.append(n)
                visited[n] = True
                result_bfs.append(n)
    

dfs(graph, v, visited)
visited = [False] * (n + 1)
bfs(graph, v, visited)

for d in result_dfs:
    print(d, end=' ')
print()
for b in result_bfs:
    print(b, end=' ')