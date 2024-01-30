import sys
input = sys.stdin.readline

n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))


def solve(n, wine):
    if n < 3:
        return sum(wine)
    dp = [0] * n
    dp[0], dp[1] = wine[0], wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], dp[1])
    for i in range(3, n):
        dp[i] = max(dp[i - 3] + wine[i] + wine[i - 1],
                    wine[i] + dp[i - 2], dp[i - 1])
    return dp[-1]


print(solve(n, wine))
