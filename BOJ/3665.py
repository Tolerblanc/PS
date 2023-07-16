import sys
from collections import deque

#sys.stdin = open('input.txt')
input = sys.stdin.readline

tc = int(input().rstrip())
for i in range(tc):
    n = int(input().rstrip())
    last = list(map(int, input().rstrip().split()))
    this = []
    graph = [[] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]
    for i in range(n):
        for k in range(i + 1, n):
            graph[last[i]].append(last[k])
            indegree[last[k]] += 1
    m = int(input().rstrip())
    if m == 0:
        print(*last)
        continue
    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        if b in graph[a]:
            graph[a].remove(b)
            graph[b].append(a)
            indegree[b] -= 1
            indegree[a] += 1 
        else:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[b] += 1
            indegree[a] -= 1
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    if not q:
        print('IMPOSSIBLE')
        continue
    while q:
        now = q.popleft()
        this.append(now)
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
        if len(q) > 2:
            print('?')
            break
        if len(q) == 0 and len(this) < n:
            print('IMPOSSIBLE')
            break
    if len(this) == n:
        print(*this)