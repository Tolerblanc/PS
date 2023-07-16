import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
visited = [0 for _ in range(f + 1)]

q = deque()
q.append(s)
visited[s] = 1
while q:
    now = q.popleft()
    if now == g:
        print(visited[now] - 1)
        break
    if now + u <= f and visited[now + u] == 0:
        visited[now + u] = visited[now] + 1
        q.append(now + u)
    if now - d > 0 and visited[now - d] == 0:
        visited[now - d] = visited[now] + 1
        q.append(now - d)
if visited[g] == 0:
    print("use the stairs")