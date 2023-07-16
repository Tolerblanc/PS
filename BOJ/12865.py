import sys

input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(tuple(map(int, input().split())))
lst.sort()
dp = [[0] * (k + 1) for _ in range(n + 1)] #row : weight, col : value
answer = 0
for i in range(1, n + 1):
    w, v = lst[i - 1]
    for j in range(1, k + 1):
        if w > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i-1][j - w] + v)
        answer = max(answer, dp[i][j])
print(answer)