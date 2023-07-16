import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)
indegree = [0] * (n + 1)
answer = [0] * (n + 1)
for i in range(1, n + 1):
    *lst, _ = map(int, input().split())
    time[i] = lst[0]
    if len(lst) == 1:
        continue
    for l in lst[1:]:
        graph[l].append(i)
        indegree[i] += 1

q = deque()
topology = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        answer[i] = time[i]
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
        answer[next] = max(answer[next], answer[now] + time[next])

for i in range(1, n + 1):
    print(answer[i])