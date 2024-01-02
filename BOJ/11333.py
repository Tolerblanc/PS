import sys
input = sys.stdin.readline
INF = 1_000_000_007

dp = [0] * 10001
dp[0] = 1
dp[3] = 3
for i in range(6, 10001, 3):
    dp[i] = dp[i - 3] * 3
    for j in range(6, i + 1, 3):
        dp[i] += dp[i - j] * j * 2 // 3
    dp[i] %= INF

T = int(input())
for _ in range(T):
    print(dp[int(input())])