import sys, heapq

sys.stdin = open('input.txt')
input = sys.stdin.readline

INF = int(1e9)
n, e = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
k = int(input().rstrip())
for _ in range(e):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b,c))
dist = [INF] * (n + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for next in graph[now]:
            temp = cost + next[1]
            if temp < dist[next[0]]:
                dist[next[0]] = temp
                heapq.heappush(q, (temp, next[0]))

dijkstra(k)
for i in range(1, n + 1):
    if dist[i] >= INF:
        print('INF')
    else:
        print(dist[i])