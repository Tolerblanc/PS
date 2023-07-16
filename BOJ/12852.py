import sys

n = int(sys.stdin.readline().rstrip())
dp = [[0, 0] for _ in range(10 ** 6 + 1)]
for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][0] + 1
    dp[i][1] = i - 1
    if i % 2 == 0:
        dp[i][0] = min(dp[i][0], dp[i//2][0] + 1)
        if dp[i][0] == dp[i//2][0] + 1:
            dp[i][1] = i//2
    if i % 3 == 0:
        dp[i][0] = min(dp[i][0], dp[i//3][0] + 1)
        if dp[i][0] == dp[i//3][0] + 1:
            dp[i][1] = i//3
print(dp[n][0])

temp = n
while True:
    if temp == 1:
        print(temp, end = '')
        break
    else:
        print(temp, end = ' ')
    temp = dp[temp][1]