import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
dp = [0 for _ in range(k + 1)]
dp[0] = 1
for coin in coins:
    for c in range(coin, k + 1, 1):
        dp[c] += dp[c - coin]
print(dp[k])