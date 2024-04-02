import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0] * 201 for _ in range(201)]

for i in range(2):
    for j in range(1, k + 1):
        dp[i][j] = 1 if i == 0 else j

for i in range(n + 1):
    dp[i][1] = 1

for i in range(2, n + 1):
    for j in range(2, k + 1):
        for l in range(i, -1, -1):
            dp[i][j] += dp[l][j - 1] % 1000000000

print(dp[n][k] % 1000000000)
