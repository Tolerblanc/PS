import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    l, *order = list(map(int, input().split()))
    for i in range(l - 1):
        graph[order[i]].append(order[i + 1])
        indegree[order[i + 1]] += 1

def topology():
    result = []
    q = deque()
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    
    if len(result) == n:
        for r in result:
            print(r)
    else:
        print(0)

topology()