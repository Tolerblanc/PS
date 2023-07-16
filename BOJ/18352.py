from collections import deque

#input
n, m, k, x = map(int, input().split())

#graph (index 0 unused) / adjacency list
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    if b in graph[a]: #check
        continue
    graph[a].append(b) 
dist = [-1] * (n + 1) #distance from x to index (index 0 unused)
dist[x] = 0
def bfs(start, graph):
    q = deque()
    q.append(start)
    while q:
        r = q.popleft()
        for i in graph[r]:
            if dist[i] == -1: #if not visited
                q.append(i) #push i to q
                dist[i] = dist[r] + 1 #update distance

bfs(x, graph)

for i in range(n + 1):
    if dist[i] == k:
        print(i)
        dist[0] = 0
if dist[0] == -1:
    print(-1)