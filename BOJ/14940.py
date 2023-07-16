import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))
	for j in range(m):
		if (graph[i][j] == 2):
			start = (i, j, 0)

visited = [[False] * m for _ in range(n)]
q = deque([start])
row, col, d = start
visited[row][col] = True
graph[row][col] = d
move = {(1, 0), (-1, 0), (0, 1), (0, -1)}

while (len(q) != 0):
	row, col, d = q.popleft()
	for dx, dy in move:
		nx = row + dx
		ny = col + dy
		if (nx < 0 or ny < 0 or nx >= n or ny >= m):
			continue
		if (graph[nx][ny] == 0 or visited[nx][ny] == True):
			continue
		q.append((nx, ny, d + 1))
		visited[nx][ny] = True
		graph[nx][ny] = d + 1

for i in range(n):
	for j in range(m):
		if (visited[i][j] == False and graph[i][j] != 0):
			graph[i][j] = -1

for l in graph:
	print(*l)
