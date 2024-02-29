# Pypy3

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for d in range(1, n):
    for i in range(n - d):
        if nums[i] == nums[i + d]:
            dp[i][i + d] = dp[i + 1][i + d - 1]
        else:
            dp[i][i + d] = min(dp[i + 1][i + d], dp[i][i + d - 1]) + 1

print(dp[0][n - 1])
