import sys, heapq

input = sys.stdin.readline

n, m = map(int, input().split())
q = []
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

answer = []
while q:
    now = heapq.heappop(q)
    answer.append(now)
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            heapq.heappush(q, next)
print(*answer)