import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
answer = []

for _ in range(m):
    a, b = map(int, input().split()) #a->b
    indegree[b] += 1
    graph[a].append(b)
    
q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
    
while q:
    now = q.popleft()
    answer.append(now)
    for x in graph[now]:
        indegree[x] -= 1
        if indegree[x] == 0:
            q.append(x)
print(*answer)