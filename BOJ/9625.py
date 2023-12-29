import sys
input = sys.stdin.readline

k = int(input())
dp = [[0, 0] for _ in range(k + 1)]
dp[1][0], dp[1][1] = 0, 1
for i in range(2, k + 1):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = dp[i-1][0] + dp[i-1][1]

print(*dp[k])
