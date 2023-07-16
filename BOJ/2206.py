import sys
from collections import deque
#sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append([int(x) for x in input().rstrip()])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs():
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while q:
        row, col, v = q.popleft()
        if row == n - 1 and col == m - 1:
            return visited[row][col][v]
        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny][v] == 0:
                visited[nx][ny][v] = visited[row][col][v] + 1
                q.append((nx, ny, v))
            if v == 0 and graph[nx][ny] == 1:
                visited[nx][ny][1] = visited[row][col][v] + 1
                q.append((nx, ny, 1))
    return -1

print(bfs())