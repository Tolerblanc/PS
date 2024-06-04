import sys
from collections import deque
input = sys.stdin.readline

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[False] * n for _ in range(n)]
q = deque([(r1, c1, 0)])
visited[r1][c1] = True
while q:
    r, c, m = q.popleft()
    for i in range(6):
        nr, nc = r + dx[i], c + dy[i]
        if nr < 0 or nc < 0 or nr >= n or nc >= n or visited[nr][nc]:
            continue
        if nr == r2 and nc == c2:
            print(m + 1)
            exit()
        q.append((nr, nc, m + 1))
        visited[nr][nc] = True
print(-1)
