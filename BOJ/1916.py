import sys, heapq

#sys.stdin = open('input.txt')
input = sys.stdin.readline

INF = int(1e9 + 1)
n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b,c))
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
            nextcost = cost + next[1]
            if nextcost < dist[next[0]]:
                dist[next[0]] = nextcost
                heapq.heappush(q, (nextcost, next[0]))
    return dist[end]

print(dijkstra(x, y))