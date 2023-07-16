import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
graph = [[] for _ in range(n + 1)]
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    for g in graph[v]:
        if not visited[g]:
            dfs(g)
    
dfs(1)
print(visited.count(True) - 1)