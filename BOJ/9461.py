import sys

input = sys.stdin.readline

dp = [1, 1, 1, 2] + [0 for _ in range(97)]
for i in range(4, 101):
    dp[i] = dp[i-3] + dp[i-2]
T = int(input())
for _ in range(T):
    print(dp[int(input()) - 1])
