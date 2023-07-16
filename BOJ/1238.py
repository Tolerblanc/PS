import sys, heapq

#sys.stdin = open('input.txt')
input = sys.stdin.readline

INF = int(1e9)
answer = 0
n, m, x = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next, cost in graph[now]:
            if dist + cost < distance[next]:
                distance[next] = dist + cost
                heapq.heappush(q, (distance[next], next))
            
dijkstra(x)
back = []
for d in distance:
    back.append(d)

for i in range(1, n + 1):
    if i == x:
        continue
    distance = [INF] * (n + 1)
    dijkstra(i)
    answer = max(answer, distance[x] + back[i])
    
    
print(answer)