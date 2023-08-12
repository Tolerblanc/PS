import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

graph = []
n = int(input().rstrip())
for _ in range(n):
	graph.append(list(map(int, input().split())))
dp = [[-1] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# dp[i][j] : 해당 지점에서 이동할 수 있는 최대 칸 수
def dfs(r, c):
	if (dp[r][c] != -1):
		return dp[r][c]
	dp[r][c] = 1
	for i in range(4):
		nr = r + dx[i]
		nc = c + dy[i]
		if (nr < 0 or nc < 0 or nr >= n or nc >= n):
			continue
		if (graph[nr][nc] <= graph[r][c]):
			continue
		dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)
	return dp[r][c]


for i in range(n):
	for j in range(n):
		if dp[i][j] == -1:
			dfs(i, j)

answer = -1
for k in dp:
	print(*k)
	answer = max(k) if answer < max(k) else answer
print(answer)