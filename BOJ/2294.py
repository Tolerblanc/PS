import sys

input = sys.stdin.readline

INF = 100001
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()
dp = [INF for _ in range(k + 1)]
for coin in coins:
    if k >= coin:
        dp[coin] = 1
    for i in range(coin + 1, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

answer = -1 if dp[k] == INF else dp[k]
print(answer)