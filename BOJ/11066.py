import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    prefix = [0]
    for i in range(n):
        prefix.append(prefix[-1] + nums[i])
    for d in range(1, n):
        for i in range(1, n - d + 1):
            dp[i][i + d] = 4242424242
            for k in range(i, i + d):
                dp[i][i + d] = min(dp[i][i + d],
                                   dp[i][k] + dp[k + 1][i + d] + prefix[i + d] - prefix[i - 1])
    print(dp[1][n])
