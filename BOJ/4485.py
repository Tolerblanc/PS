import sys
import heapq
input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

tc = 0
while (n := int(input())) != 0:
    tc += 1
    graph = [list(map(int, input().split())) for _ in range(n)]
    q = [(graph[0][0], 0, 0)]
    dist = [[10001] * n for _ in range(n)]
    dist[0][0] = graph[0][0]
    while q:
        cost, r, c = heapq.heappop(q)
        if dist[r][c] < cost:
            continue
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue
            if dist[nr][nc] <= cost + graph[nr][nc]:
                continue
            dist[nr][nc] = cost + graph[nr][nc]
            heapq.heappush(q, (cost + graph[nr][nc], nr, nc))
    print(f'Problem {tc}: {dist[-1][-1]}')
