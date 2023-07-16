import sys, heapq

sys.stdin = open('input.txt')
input = sys.stdin.readline

INF = int(1e9)
n, e = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
x, y = map(int, input().rstrip().split())

def dijkstra(start, end):
    if start == end:
        return 0    
    q = []
    dist = [INF] * (n + 1)
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
    return dist[end]

answer = min(dijkstra(1, x) + dijkstra(x, y) + dijkstra(y, n), dijkstra(1, y) + dijkstra(y, x) + dijkstra(x, n))

if answer >= INF:
    print(-1)
else: 
    print(answer)