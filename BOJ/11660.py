import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[1][1] = board[0][0]
for i in range(2, n + 1):
    dp[i][1] = dp[i - 1][1] + board[i - 1][0]
    dp[1][i] = dp[1][i - 1] + board[0][i - 1]
    
for i in range(2, n + 1):
    for j in range(2, n + 1):
        dp[i][j] = board[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])