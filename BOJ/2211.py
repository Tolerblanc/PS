import sys, heapq

#sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = 100001

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q = [(0, 1)]
prev = [0 for _ in range(n + 1)]
dist = [INF for _ in range(n + 1)]
dist[1] = 0

while q:
    cost, now = heapq.heappop(q)
    if dist[now] < cost:
        continue
    for next in graph[now]:
        temp = cost + next[1]
        if dist[next[0]] > temp:
            heapq.heappush(q, (temp, next[0]))
            prev[next[0]] = now
            dist[next[0]] = temp

print(n - 1)
for i in range(2, n + 1):
    print(prev[i], i)