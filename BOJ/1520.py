import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

m, n = map(int, input().split())
graph = []
for _ in range(m):
	graph.append(list(map(int, input().split())))

visited = [[-1] * n for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(r, c):
	if r == m - 1 and c == n - 1:
		return 1
	if visited[r][c] != -1:
		return visited[r][c]
	cnt = 0
	for i in range(4):
		nr = r + dx[i]
		nc = c + dy[i]
		if nr >= m or nc >= n or nr < 0 or nc < 0:
			continue
		if graph[nr][nc] >= graph[r][c]:
			continue
		cnt += dfs(nr, nc)
	visited[r][c] = cnt
	return visited[r][c]

print(dfs(0, 0))