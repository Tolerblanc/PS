import sys
from collections import deque

#sys.stdin = open('input.txt')
input = sys.stdin.readline

tc = int(input().rstrip())
for _ in range(tc):
    n, k = map(int, input().rstrip().split())
    builds = list(map(int, input().rstrip().split()))
    indegree = [0 for _ in range(n + 1)]
    result = [0] + [b for b in builds]
    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        indegree[b] += 1
    w = int(input().rstrip())
    
    q = deque()
    topology = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        topology.append(now)
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    
    while topology:
        now = topology.popleft()
        for next in graph[now]:
            result[next] = max(result[next], result[now] + builds[next - 1])
    print(result[w])