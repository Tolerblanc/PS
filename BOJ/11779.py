import sys, heapq

#sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = int(1e9) + 1

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
start, end = map(int, input().rstrip().split())

prev = [0 for _ in range(n + 1)]
dist = [INF for _ in range(n + 1)]
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
            prev[next[0]] = now
            heapq.heappush(q, (temp, next[0]))

answer = []
curr = end
while curr != start:
    answer.append(curr)
    curr = prev[curr]
answer.append(start)
print(dist[end])
print(len(answer))
print(*answer[::-1])