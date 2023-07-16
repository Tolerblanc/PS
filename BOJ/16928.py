import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

visited = [False] * 101
graph = [0] * 101

n, m = map(int, input().split())
for _ in range(n + m):
    x, y = map(int, input().split())
    graph[x] = y

q = deque([(1,1),(2,1),(3,1),(4,1),(5,1),(6,1)])
visited[1] = True
while q:
    roll, now = q.popleft()
    if now == 100:
        print(roll - 1)
        break
    for i in range(1, 7):
        next = now + i
        if next > 100:
            continue
        if graph[next] != 0:
            next = graph[next]
        if not visited[next]:
            visited[next] = True
            q.append((roll + 1, next))